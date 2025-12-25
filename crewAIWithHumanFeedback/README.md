# CrewAI 营销战略 + Human Feedback 案例

本案例展示了如何使用 **CrewAI** 构建一个带有人类反馈 (Human Feedback) 机制的营销战略协作智能体。

## 1. 简介

本项目是一个进阶案例，在营销战略协作的基础上，引入了 **Human Feedback (HF)** 机制。通过人类反馈，AI 模型能够更好地理解人类意图，提供更符合预期的响应。

*   **核心功能**: 在任务执行中集成 Human Feedback。
*   **Human Feedback (RLHF)**: 通过人类的评估和反馈来优化模型输出。
*   **视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV1qcxgeVEuF/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/ltu34eawkvA)

## 2. Agent 设计

本项目沿用了[营销战略案例](../crewAIWithMarketingStrategy)中的三个核心 Agent：

| Agent | 角色 | 目标 | 背景故事 |
| :--- | :--- | :--- | :--- |
| **lead_market_analyst** | 首席市场分析师 | 对产品和竞争对手进行深入剖析。 | 敏锐的市场洞察力，擅长分析产品和竞争对手。 |
| **chief_marketing_strategist** | 首席营销战略师 | 制定令人惊喜的营销战略。 | 擅长制定成功的定制营销战略。 |
| **creative_content_creator** | 首席创意内容创作师 | 开发有吸引力的创新内容。 | 擅长将战略转化为引人入胜的故事和视觉内容。 |

## 3. Task 设计

本案例包含以下任务，并在关键环节可能涉及人类反馈：

| 任务名称 | 负责 Agent | 描述 | 期望输出 |
| :--- | :--- | :--- | :--- |
| **research_task** | lead_market_analyst | 深入剖析产品和竞品。 | 完整的分析报告。 |
| **project_understanding_task** | chief_marketing_strategist | 了解项目和受众。 | 项目摘要。 |
| **marketing_strategy_task** | chief_marketing_strategist | 制定全面的营销战略。 | 营销战略文件。 |
| **campaign_idea_task** | creative_content_creator | 开发创意营销活动。 | 5 个活动设想。 |
| **copy_creation_task** | creative_content_creator | 制作营销文案。 | 营销副本。 |

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
    cd crewAIWithHumanFeedback
    ```
3.  安装依赖包：
    ```bash
    pip install -r requirements.txt
    ```

### 5.2 配置 Main.py

打开 `main.py`，根据您的实际情况修改以下配置 (OpenAI, OneAPI, Ollama)，具体参考代码注释。

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
