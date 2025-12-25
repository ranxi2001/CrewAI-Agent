# 导入依赖包
import os
import sys
import re
import uuid
import time
import json
import asyncio
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
import uvicorn
from langchain_openai import ChatOpenAI
from crew import CryptoTradingCrew



# 模型全局参数配置  根据自己的实际情况进行调整
# openai模型相关配置 根据自己的实际情况进行调整
OPENAI_API_BASE = "https://api.wlai.vip/v1"
OPENAI_CHAT_API_KEY = "your-openai-api-key"
OPENAI_CHAT_MODEL = "gpt-4o-mini"
# 非gpt大模型相关配置(oneapi方案 通义千问为例) 根据自己的实际情况进行调整
ONEAPI_API_BASE = "http://your-oneapi-address:3000/v1"
ONEAPI_CHAT_API_KEY = "your-oneapi-key"
ONEAPI_CHAT_MODEL = "qwen-max"
# 本地大模型相关配置(Ollama方案 llama3.1:latest为例) 根据自己的实际情况进行调整
OLLAMA_API_BASE = "http://localhost:11434/v1"
OLLAMA_CHAT_API_KEY = "ollama"
OLLAMA_CHAT_MODEL = "llama3.1:latest"
# 谷歌搜索引擎API Key (用于新闻搜索)
SERPER_API_KEY = "your-serper-api-key"


# 初始化LLM模型
model = None
# API服务设置相关  根据自己的实际情况进行调整
PORT = 8012  # 服务访问的端口
# openai:调用gpt大模型;oneapi:调用非gpt大模型;ollama:调用本地大模型
MODEL_TYPE = "openai"



# 定义Message类
class RequestMessage(BaseModel):
    role: str
    symbol: str  # 加密货币交易对，如 BTCUSDT


class ResponseMessage(BaseModel):
    role: str
    content: str


# 定义ChatCompletionRequest类
class ChatCompletionRequest(BaseModel):
    messages: List[RequestMessage]
    stream: Optional[bool] = False


# 定义ChatCompletionResponseChoice类
class ChatCompletionResponseChoice(BaseModel):
    index: int
    message: ResponseMessage
    finish_reason: Optional[str] = None


# 定义ChatCompletionResponse类
class ChatCompletionResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{uuid.uuid4().hex}")
    object: str = "chat.completion"
    created: int = Field(default_factory=lambda: int(time.time()))
    choices: List[ChatCompletionResponseChoice]
    system_fingerprint: Optional[str] = None


# 定义了一个异步函数lifespan，管理应用的生命周期
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    global MODEL_TYPE, model
    global ONEAPI_API_BASE, ONEAPI_CHAT_API_KEY, ONEAPI_CHAT_MODEL
    global OPENAI_API_BASE, OPENAI_CHAT_API_KEY, OPENAI_CHAT_MODEL
    global OLLAMA_API_BASE, OLLAMA_CHAT_API_KEY, OLLAMA_CHAT_MODEL
    global SERPER_API_KEY
    
    try:
        print("正在初始化模型...")
        # 设置google搜索引擎API Key
        os.environ["SERPER_API_KEY"] = SERPER_API_KEY
        
        # 根据MODEL_TYPE选择初始化对应的模型
        if MODEL_TYPE == "oneapi":
            model = ChatOpenAI(
                base_url=ONEAPI_API_BASE,
                api_key=ONEAPI_CHAT_API_KEY,
                model=ONEAPI_CHAT_MODEL,
                temperature=0.7,
            )
        elif MODEL_TYPE == "ollama":
            os.environ["OPENAI_API_KEY"] = "NA"
            model = ChatOpenAI(
                base_url=OLLAMA_API_BASE,
                api_key=OLLAMA_CHAT_API_KEY,
                model=OLLAMA_CHAT_MODEL,
                temperature=0.7,
            )
        else:
            model = ChatOpenAI(
                base_url=OPENAI_API_BASE,
                api_key=OPENAI_CHAT_API_KEY,
                model=OPENAI_CHAT_MODEL,
            )

        print("LLM初始化完成")

    except Exception as e:
        print(f"初始化过程中出错: {str(e)}")
        raise

    yield
    # 关闭时执行
    print("正在关闭...")


# lifespan 参数用于在应用程序生命周期的开始和结束时执行一些初始化或清理工作
app = FastAPI(lifespan=lifespan)


# POST请求接口，与大模型进行知识问答
@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    if not model:
        print("服务未初始化")
        raise HTTPException(status_code=500, detail="服务未初始化")
    try:
        print(f"已经进入到请求中")
        symbol = request.messages[-1].symbol
        print(f"接收到的交易对: {symbol}")
        
        # 执行crew
        inputs = {
            "symbol": symbol,
        }
        # 传入model，指定crew中的Agent使用什么大模型
        result = CryptoTradingCrew(model).crew().kickoff(inputs=inputs)
        # 将返回的数据转成string类型
        formatted_response = str(result)
        print(f"LLM最终回复结果: {formatted_response}")

        # 处理流式响应
        if request.stream:
            async def generate_stream():
                chunk_id = f"chatcmpl-{uuid.uuid4().hex}"
                lines = formatted_response.split('\n')
                for i, line in enumerate(lines):
                    chunk = {
                        "id": chunk_id,
                        "object": "chat.completion.chunk",
                        "created": int(time.time()),
                        "choices": [
                            {
                                "index": 0,
                                "delta": {"content": line + '\n'},
                                "finish_reason": None
                            }
                        ]
                    }
                    yield f"{json.dumps(chunk)}\n"
                    await asyncio.sleep(0.5)
                
                final_chunk = {
                    "id": chunk_id,
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "choices": [
                        {
                            "index": 0,
                            "delta": {},
                            "finish_reason": "stop"
                        }
                    ]
                }
                yield f"{json.dumps(final_chunk)}\n"

            return StreamingResponse(generate_stream(), media_type="text/event-stream")
        
        # 处理非流式响应
        else:
            response = ChatCompletionResponse(
                choices=[
                    ChatCompletionResponseChoice(
                        index=0,
                        message=ResponseMessage(role="assistant", content=formatted_response),
                        finish_reason="stop"
                    )
                ]
            )
            return JSONResponse(content=response.model_dump())

    except Exception as e:
        print(f"处理聊天完成时出错:\n\n {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    print(f"在端口 {PORT} 上启动服务器")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
