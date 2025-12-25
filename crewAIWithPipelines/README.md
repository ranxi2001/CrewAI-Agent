# CrewAI Pipelines 工作流案例

本案例是在“营销战略协作智能体”项目的基础上，深度解析并实操 **CrewAI Pipelines** 功能。

## 1. 简介

**Pipeline** 代表一种结构化的工作流程，允许多个 Crew 顺序或并行执行。它提供了一种组织涉及多个阶段 (Stage) 的复杂流程的方法，其中一个 Stage 的输出可作为后续 Stage 的输入。

*   **核心功能**: CrewAI Pipelines (串行/并行编排).
*   **视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV18LCdYpE5Z/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/BhXZn2NaJYs)

## 2. 核心概念 (Pipelines)

*   **Stage**: Pipeline 中的一个独立部分，用于编排 Crew。可以是一个顺序编排，也可以是一个并行编排 (Branch)。
    *   Example: `stages = [crew1 >> [crew2, crew3] >> crew4]`
*   **Kickoff**: 启动 Pipeline。
*   **Branch**: Stage 内的并行执行 Crew。
*   **Trace**: 单个输入在整个 Pipeline 中的运行轨迹。

## 3. Agent 与 Task 设计

本项目复用了[营销战略案例](../crewAIWithMarketingStrategy)中的 Agent 和 Task 定义：
*   **Agents**: 首席市场分析师, 首席营销战略师, 首席创意内容创作师。
*   **Tasks**: 市场调研, 项目理解, 营销战略制定, 创意构思, 文案创作。

## 4. 环境准备

在开始之前，请确保您已安装以下工具：

*   **Anaconda**: 用于管理 Python 虚拟环境。
*   **PyCharm** (可选): 集成开发环境。
*   **CrewAI**: 需升级到支持 Pipelines 的版本 (建议 `0.74.2` 或更高)。
    ```bash
    pip install --upgrade crewai crewai-tools
    ```
*   **LLM 环境配置**: 支持 OpenAI, OneAPI, Ollama。

## 5. 安装与配置

### 5.1 安装依赖

1.  克隆或下载本项目。
2.  进入项目目录：
    ```bash
    cd crewAIWithPipelines
    ```
3.  安装依赖包：
    ```bash
    pip install -r requirements.txt
    ```

### 5.2 配置 Main.py 和 MyLLM.py

打开 `main.py` 和 `utils/myLLM.py`，根据您的实际情况修改 LLM 配置。

## 6. 运行与测试

### 6.1 单独测试 Pipeline

运行 `crewPipeline.py` 脚本测试 Pipeline 逻辑：
```bash
python crewPipeline.py
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
