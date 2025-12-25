# CrewAI 营销战略协作案例 (JSON 输出)

本案例展示了如何使用 **CrewAI** 构建一个营销战略协作智能体。该案例重点演示了如何让 Task 以自定义 JSON 格式输出数据。

## 1. 简介

本项目是一个进阶案例，包含三个 Agent：首席市场分析师、首席营销战略师和首席创意内容创作师，共同协作完成从市场分析到营销文案创作的全流程。

*   **核心功能**: 自定义 Task 的 JSON 输出格式。
*   **视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV1i5bAeAEWn/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/w8uxBuVQVlg)

## 2. Agent 设计

本项目定义了三个核心 Agent：

| Agent | 角色 | 目标 | 背景故事 |
| :--- | :--- | :--- | :--- |
| **lead_market_analyst** | 首席市场分析师 | 对产品和竞争对手进行深入剖析，提供指导。 | 敏锐的市场洞察力，擅长分析产品和竞争对手。 |
| **chief_marketing_strategist** | 首席营销战略师 | 基于分析制定令人惊喜的营销战略。 | 擅长制定成功的定制营销战略。 |
| **creative_content_creator** | 首席创意内容创作师 | 开发有吸引力的创新内容，创建高影响力广告文案。 | 擅长将战略转化为引人入胜的故事和视觉内容。 |

## 3. Task 设计

| 任务名称 | 负责 Agent | 描述 | 期望输出 |
| :--- | :--- | :--- | :--- |
| **research_task** | lead_market_analyst | 基于 `{customer_domain}` 对产品和竞品进行剖析 (2024年数据)。 | 关于客户、产品和竞品的完整报告 (包含指标、偏好等)。 |
| **project_understanding_task** | chief_marketing_strategist | 了解 `{project_description}` 和目标受众。 | 项目摘要和目标受众简介。 |
| **marketing_strategy_task** | chief_marketing_strategist | 制定全面的营销战略 (含名称、策略、渠道、KPI)。 | 详细的营销战略文件。 |
| **campaign_idea_task** | creative_content_creator | 开发 5 个富有创意的营销活动构思。 | 5 个活动设想清单。 |
| **copy_creation_task** | creative_content_creator | 为获批的活动创意制作营销文案。 | 每个活动创意的营销副本。 |

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
    cd crewAIWithMarketingStrategy
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
