# CrewAI + FastAPI 基础案例

本案例展示了如何使用 **CrewAI** 和 **FastAPI** 构建一个多 Agent 协作应用，并将其封装为 API 服务。同时支持 **OpenAI (GPT)**、**通义千问 (OneAPI)** 和 **Ollama (本地模型)** 的对比测试。

## 1. 简介

本项目旨在帮助开发者熟悉 CrewAI 的整体开发环境搭建及业务流程。

*   **视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV1N44reDEt3/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/2TE5DlYlvGw)

## 2. Agent 设计

本项目定义了两个核心 Agent：

| Agent | 角色 | 目标 | 背景故事 |
| :--- | :--- | :--- | :--- |
| **研究员** | `{topic}` 高级数据研究员 | 探索 `{topic}` 的前沿发展 | 经验丰富的研究员，擅长发现最新发展，并以简洁明了的方式呈现信息。 |
| **报告分析员** | `{topic}` 报告分析员 | 根据 `{topic}` 数据分析和研究结果创建详细报告 | 一丝不苟的分析师，能将复杂数据转化为简洁明了的报告。 |

## 3. Task 设计

| 任务名称 | 负责 Agent | 描述 | 期望输出 |
| :--- | :--- | :--- | :--- |
| **研究任务** | 研究员 | 对 `{topic}` 进行深入研究，寻找 2024 年的相关信息。 | 一份包含 10 个要点的清单，列出与 `{topic}` 最相关的信息。 |
| **报告任务** | 报告分析员 | 根据研究结果完整扩展每个主题。 | 一份包含主要主题的完整报告 (Markdown 格式)。 |

## 4. 环境准备

在开始之前，请确保您已安装以下工具：

*   **Anaconda**: 用于管理 Python 虚拟环境。
*   **PyCharm** (可选): 集成开发环境。
*   **CrewAI**: `pip install crewai` (本项目依赖中包含)。
*   **LLM 环境**:
    *   **OpenAI**: 需要 API Key。
    *   **OneAPI**: 用于支持国产大模型 (如通义千问)。
    *   **Ollama**: 用于运行本地开源模型 (如 Llama 3.1, Qwen2)。

## 5. 安装与配置

### 5.1 安装依赖

1.  克隆或下载本项目。
2.  进入项目目录：
    ```bash
    cd crewaitest
    ```
3.  安装依赖包：
    ```bash
    pip install -r requirements.txt
    ```

### 5.2 配置 Main.py

打开 `main.py`，根据您的实际情况修改以下配置：

*   **OpenAI 配置**:
    ```python
    OPENAI_API_BASE = "https://api.wlai.vip/v1"
    OPENAI_CHAT_API_KEY = "your-api-key"
    OPENAI_CHAT_MODEL = "gpt-4o-mini"
    ```
*   **OneAPI (国产模型) 配置**:
    ```python
    ONEAPI_API_BASE = "http://your-oneapi-address:port/v1"
    ONEAPI_CHAT_API_KEY = "your-oneapi-key"
    ONEAPI_CHAT_MODEL = "qwen-max"
    ```
*   **Ollama (本地模型) 配置**:
    ```python
    OLLAMA_API_BASE = "http://localhost:11434/v1"
    OLLAMA_CHAT_API_KEY = "ollama"
    OLLAMA_CHAT_MODEL = "llama3.1:latest"
    ```
*   **模型切换**:
    ```python
    # 可选值: "openai", "oneapi", "ollama"
    MODEL_TYPE = "openai"
    ```

## 6. 运行与测试

### 6.1 启动 API 服务

```bash
python main.py
```
服务默认运行在 `http://localhost:8012`。

### 6.2 测试 API

使用 `apiTest.py` 脚本进行测试：

1.  修改 `apiTest.py` 中的 `url` 确保端口一致。
2.  运行脚本：
    ```bash
    python apiTest.py
    ```

或者使用 Postman 等工具发送 POST 请求。
