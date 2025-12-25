# CrewAI Flows 工作流案例

本案例是在“营销战略协作智能体”项目的基础上，深度解析并实操 **CrewAI Flows** 功能。

## 1. 简介

**Flows** 为构建复杂的 AI 自动化工作流提供了一个强大的框架。它支持简化工作流创建、状态管理、事件驱动架构以及灵活的条件控制。

*   **核心功能**: CrewAI Flows (复杂工作流编排).
*   **视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV1jgyeYgEyb/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/RfnQHdDVg68)

## 2. 核心概念 (Flows)

*   **装饰器**:
    *   `@start()`: 标记流程起点 (支持并行)。
    *   `@listen()`: 标记监听器 (等待特定方法完成)。
    *   `@router()`: 路由控制 (根据输出决定下一步)。
*   **条件控制**:
    *   `or_()`: 任意一个完成即执行。
    *   `and_()`: 全部完成才执行。
*   **状态管理**: 支持非结构化和结构化状态管理。

## 3. Agent 与 Task 设计

本项目复用了[营销战略案例](../crewAIWithMarketingStrategy)中的 Agent 和 Task 定义：
*   **Agents**: 首席市场分析师, 首席营销战略师, 首席创意内容创作师。
*   **Tasks**: 市场调研, 项目理解, 营销战略制定, 创意构思, 文案创作。

## 4. 环境准备

在开始之前，请确保您已安装以下工具：

*   **Anaconda**: 用于管理 Python 虚拟环境。
*   **PyCharm** (可选): 集成开发环境。
*   **CrewAI**: 需使用支持 Flows 的最新版本 (建议 `0.74.2` 或更高)。
    ```bash
    pip install --upgrade crewai crewai-tools
    ```
*   **LLM 环境配置**: 支持 OpenAI, OneAPI, Ollama。

## 5. 安装与配置

### 5.1 安装依赖

1.  克隆或下载本项目。
2.  进入项目目录：
    ```bash
    cd crewAIWithFlows
    ```
3.  安装依赖包：
    ```bash
    pip install -r requirements.txt
    ```

### 5.2 配置 Main.py 和 MyLLM.py

打开 `main.py` 和 `utils/myLLM.py`，根据您的实际情况修改 LLM 配置。

## 6. 运行与测试

### 6.1 测试 Flows 功能

1.  **官方模版测试**:
    ```bash
    crewai create flow flowsTest
    # 配置 .env 后运行 python main.py
    ```
2.  **本项目 Flows 测试**:
    运行 `flowsTest.py` 脚本：
    ```bash
    python flowsTest.py
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
