# CrewAI 健康档案助手 (RAG 案例)

本案例展示了如何使用 **CrewAI** 构建一个健康档案助手智能体。该案例包含两个 Agent，利用 **RAG (Retrieval-Augmented Generation)** 技术从私有健康档案库中检索信息，并生成专业的健康建议报告。

## 1. 简介

本项目是一个进阶案例，演示了智能体如何结合 RAG 技术，从离线知识库中检索信息来增强回答的准确性和专业性。

*   **RAG 流程**: 文档加载 -> 切分 -> 向量化 -> 检索 -> 增强 Prompt -> LLM 生成。
*   **相关视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV1j94oe7ESy/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/YYxgE4i7-OE)
    *   [RAG 基础原理视频](https://www.bilibili.com/video/BV1ryHxesEHs/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)

## 2. Agent 设计

本项目定义了两个核心 Agent：

| Agent | 角色 | 目标 | 背景故事 |
| :--- | :--- | :--- | :--- |
| **retrieval_agent** | 健康档案检索专家 | 根据健康问题 `{topic}`，从档案中检索相关记录。 | 擅长在庞大的健康档案库中快速找到相关历史记录的专家。 |
| **report_agent** | 健康报告撰写专家 | 分析检索到的数据，结合问题 `{topic}` 撰写健康建议报告。 | 医学背景的报告撰写专家，擅长生成简洁且医学严谨的建议报告。 |

## 3. Task 设计

| 任务名称 | 负责 Agent | 描述 | 期望输出 |
| :--- | :--- | :--- | :--- |
| **retrieval_task** | retrieval_agent | 使用外部工具从健康档案库中检索与 `{topic}` 相关的信息。 | 与用户健康问题密切相关的健康档案记录。 |
| **report_task** | report_agent | 根据检索内容和问题 `{topic}`，撰写健康建议报告并保存为 PDF。 | 一份包含健康状况分析和实际健康建议的报告。 |

## 4. 环境准备

在开始之前，请确保您已安装以下工具：

*   **Anaconda**: 用于管理 Python 虚拟环境。
*   **PyCharm** (可选): 集成开发环境。
*   **CrewAI**: `pip install crewai`。
*   **LLM 环境配置**: 支持 OpenAI, OneAPI, Ollama。

## 5. 安装与配置

### 5.1 安装依赖

1.  克隆或下载本项目。
2.  进入项目目录：
    ```bash
    cd crewAIWithRag
    ```
3.  安装依赖包：
    ```bash
    pip install -r requirements.txt
    ```

### 5.2 字体配置 (重要)

本应用需要使用中文字体，请下载后将文件放置在工程文件夹内：
*   **下载地址**: [百度网盘](https://pan.baidu.com/s/1fhg2ac2UUjdEXbWjJT2kuQ?pwd=1234) (提取码: 1234)

### 5.3 配置 Main.py

打开 `main.py`，根据您的实际情况修改以下配置 (OpenAI, OneAPI, Ollama)，具体参考代码注释。

## 6. 运行与测试

### 6.1 测试外部工具 (RAG 工具)

进入 `unitTest` 文件夹，对 RAG 工具进行独立测试：
```bash
cd unitTest
# 运行相关测试脚本 (如有)
```

### 6.2 启动 API 服务

```bash
python main.py
```
服务默认运行在 `http://localhost:8012`。

### 6.3 测试 API

使用 `apiTest.py` 脚本进行测试：

1.  修改 `apiTest.py` 中的 `url` 确保端口一致。
2.  运行脚本：
    ```bash
    python apiTest.py
    ```
