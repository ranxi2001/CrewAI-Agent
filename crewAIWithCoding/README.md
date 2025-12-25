# CrewAI 高效软件编码案例

本案例展示了如何使用 **CrewAI** 构建一个高效的软件编码团队。该案例包含三个协作 Agent：高级软件工程师、QA 工程师和首席 QA 工程师，共同完成代码编写、审查和质量评估。

## 1. 简介

本项目是一个进阶案例，演示了多 Agent 如何协作完成复杂的软件开发任务，确保代码质量和功能完整性。

*   **视频教程**:
    *   [Bilibili](https://www.bilibili.com/video/BV1cNtJeJEPA/?vd_source=30acb5331e4f5739ebbad50f7cc6b949)
    *   [YouTube](https://youtu.be/U_CzuyKNKkY)

## 2. Agent 设计

本项目定义了三个核心 Agent：

| Agent | 角色 | 目标 | 背景故事 |
| :--- | :--- | :--- | :--- |
| **senior_engineer_agent** | 高级软件工程师 | 根据具体需求完成软件开发 | 高科技头部企业的高级工程师，擅长写出完美的代码。 |
| **qa_engineer_agent** | 软件质量控制工程师 | 分析代码错误，确保代码质量 | 专门负责检查代码错误（语法、逻辑、安全）的高级工程师。 |
| **chief_qa_engineer_agent** | 首席软件质量控制工程师 | 确保代码完成它应该完成的工作 | 专注于代码质量，认为程序员总是只做一般的工作。 |

## 3. Task 设计

| 任务名称 | 负责 Agent | 描述 | 期望输出 |
| :--- | :--- | :--- | :--- |
| **code_task** | senior_engineer_agent | 使用 Python 编写一个游戏：`{game}`。 | 完整的 Python 代码。 |
| **review_task** | qa_engineer_agent | 对代码进行错误检查（逻辑、语法、安全等）。 | 经过检查和修正的完整 Python 代码。 |
| **evaluate_task** | chief_qa_engineer_agent | 仔细检查代码，确保功能完整。 | 最终的完整 Python 代码。 |

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
    cd crewAIWithCoding
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
