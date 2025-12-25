# 用于测试API服务
import requests
import json


# 设置服务器地址
url = "http://localhost:8012/v1/chat/completions"

# 设置是否使用流式输出
stream_flag = False

# 请求数据
data = {
    "messages": [
        {
            "role": "user",
            "symbol": "BTCUSDT"  # 可以修改为其他交易对，如 ETHUSDT, SOLUSDT
        }
    ],
    "stream": stream_flag
}

# 请求头
headers = {
    "Content-Type": "application/json"
}


def test_non_stream():
    """非流式请求测试"""
    print("=" * 50)
    print("非流式请求测试")
    print("=" * 50)
    print(f"请求交易对: {data['messages'][0]['symbol']}")
    print("正在分析，请稍候...")
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        print("\n" + "=" * 50)
        print("分析结果:")
        print("=" * 50)
        print(content)
    else:
        print(f"请求失败: {response.status_code}")
        print(response.text)


def test_stream():
    """流式请求测试"""
    print("=" * 50)
    print("流式请求测试")
    print("=" * 50)
    print(f"请求交易对: {data['messages'][0]['symbol']}")
    print("正在分析，请稍候...")
    print("\n" + "=" * 50)
    print("分析结果 (流式输出):")
    print("=" * 50)
    
    response = requests.post(url, json=data, headers=headers, stream=True)
    
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode('utf-8'))
                    if chunk["choices"][0]["delta"].get("content"):
                        print(chunk["choices"][0]["delta"]["content"], end="")
                except json.JSONDecodeError:
                    pass
        print()
    else:
        print(f"请求失败: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    if stream_flag:
        test_stream()
    else:
        test_non_stream()
