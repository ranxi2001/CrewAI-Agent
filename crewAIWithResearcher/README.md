# CrewAI 技术研究员案例

本案例展示了如何使用 **CrewAI** 构建一个技术研究员智能体。该智能体包含两个协作 Agent，分别负责研究最新技术趋势并进行详细分析，最终撰写报告并调用外部工具将其保存为 PDF 文件。

## 1. 简介

本项目是一个进阶案例，演示了 Agent 如何调用外部工具来实现具体的文件操作。

*   **视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV1Sy4HeiEBn/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/MGEdzUUKISw)

## 2. Agent 设计

本项目定义了两个核心 Agent：

| Agent | 角色 | 目标 | 背景故事 |
| :--- | :--- | :--- | :--- |
| **researcher** | 高级技术研究员 | 研究 `{topic}` 的最新技术趋势并进行详细分析。 | 该领域的技术专家，擅长探索技术前沿动态，深入挖掘最新技术发展趋势。 |
| **reporting_writer** | 技术趋势报告撰写者 | 撰写关于 `{topic}` 技术趋势的全面报告。 | 擅长撰写技术文章的作家，能够将复杂的技术概念用简单的语言解释清楚。 |

## 3. Task 设计

| 任务名称 | 负责 Agent | 描述 | 期望输出 |
| :--- | :--- | :--- | :--- |
| **research_task** | researcher | 研究 `{topic}` 的最新技术趋势，评估优缺点。 | 一份包含 5 个要点的清单，介绍 `{topic}` 的技术前沿动态。 |
| **reporting_task** | reporting_writer | 根据分析撰写技术趋势报告。 | 一份详细的四段报告，解释 `{topic}` 技术趋势及其影响。 |

## 4. 环境准备

在开始之前，请确保您已安装以下工具：

*   **Anaconda**: 用于管理 Python 虚拟环境。
*   **PyCharm** (可选): 集成开发环境。
*   **CrewAI**: `pip install crewai` (本项目依赖中包含)。
*   **LLM 环境配置**: 支持 OpenAI, OneAPI (通义千问等), Ollama (本地模型)。

## 5. 安装与配置

### 5.1 安装依赖

1.  克隆或下载本项目。
2.  进入项目目录：
    ```bash
    cd crewAIWithResearcher
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
