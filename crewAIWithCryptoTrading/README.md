# CrewAI 加密货币交易分析案例

本案例展示了如何使用 **CrewAI** 构建一个加密货币交易分析智能体。该项目包含三个协作 Agent：K线技术分析师、新闻分析师和首席交易顾问，共同完成从技术分析到投资建议的全流程。

## 1. 简介

本项目综合运用技术分析和新闻情绪分析，为加密货币交易提供智能决策支持。

*   **核心功能**:
    *   K线数据获取与技术分析
    *   加密货币新闻搜索与情绪分析
    *   综合投资建议生成

## 2. Agent 设计

| Agent | 角色 | 目标 | 工具 |
| :--- | :--- | :--- | :--- |
| **kline_analyst** | K线技术分析师 | 分析K线数据，识别趋势、支撑/阻力位 | `get_kline_data` |
| **news_analyst** | 加密新闻分析师 | 分析最近3天新闻，判断市场情绪 | `get_crypto_news` |
| **trading_advisor** | 首席交易顾问 | 综合分析，给出投资建议 | - |

## 3. Task 设计

| 任务 | Agent | 描述 | 期望输出 |
| :--- | :--- | :--- | :--- |
| **kline_analysis_task** | kline_analyst | 获取K线，分析趋势 | 技术分析报告 |
| **news_analysis_task** | news_analyst | 获取新闻，分析情绪 | 新闻情绪报告 |
| **trading_recommendation_task** | trading_advisor | 综合分析，给出建议 | 交易建议报告 |

## 4. 自定义工具

*   **`GetKlineDataTool`**: 调用 Binance API 获取 K 线 OHLCV 数据。
*   **`GetCryptoNewsTool`**: 调用 Serper API 搜索最近 3 天的加密货币新闻。

## 5. 环境准备

*   **Anaconda**: Python 虚拟环境管理。
*   **CrewAI**: `pip install crewai crewai-tools`。
*   **Serper API Key**: 用于新闻搜索 (在 `main.py` 中配置)。
*   **LLM 配置**: 支持 OpenAI, OneAPI, Ollama。

## 6. 安装与配置

### 6.1 安装依赖

```bash
cd crewAIWithCryptoTrading
pip install -r requirements.txt
```

### 6.2 配置 Main.py

打开 `main.py`，修改以下配置：

```python
# OpenAI 配置
OPENAI_API_BASE = "https://api.wlai.vip/v1"
OPENAI_CHAT_API_KEY = "your-api-key"
OPENAI_CHAT_MODEL = "gpt-4o-mini"

# Serper API Key (新闻搜索)
SERPER_API_KEY = "your-serper-api-key"

# 模型类型: "openai", "oneapi", "ollama"
MODEL_TYPE = "openai"
```

## 7. 运行与测试

### 7.1 启动 API 服务

```bash
python main.py
```
服务默认运行在 `http://localhost:8012`。

### 7.2 测试 API

修改 `apiTest.py` 中的交易对 (默认 `BTCUSDT`)，然后运行：

```bash
python apiTest.py
```

### 7.3 请求示例

```json
{
  "messages": [
    {
      "role": "user",
      "symbol": "BTCUSDT"
    }
  ],
  "stream": false
}
```

## 8. 输出示例

分析结果将包含：
1.  **技术分析**: 趋势、支撑/阻力位、MA交叉信号
2.  **新闻情绪**: 看涨/看跌/中性 + 关键新闻摘要
3.  **交易建议**: 买入/卖出/持有 + 入场点、止损点、目标价
