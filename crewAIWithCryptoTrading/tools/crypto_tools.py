# 加密货币交易分析工具
# 提供K线数据获取和新闻搜索功能

import os
import requests
from datetime import datetime, timedelta
from typing import Optional, Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class GetKlineDataInput(BaseModel):
    """获取K线数据的输入参数"""
    symbol: str = Field(..., description="交易对符号，例如 BTCUSDT, ETHUSDT")
    interval: str = Field(default="1d", description="K线时间间隔，例如 1h, 4h, 1d")
    limit: int = Field(default=30, description="获取K线数量，默认30根")


class GetKlineDataTool(BaseTool):
    """获取加密货币K线数据的工具"""
    name: str = "get_kline_data"
    description: str = "获取指定加密货币交易对的K线数据，返回包含开盘价、最高价、最低价、收盘价、成交量的OHLCV数据。"
    args_schema: Type[BaseModel] = GetKlineDataInput

    def _run(self, symbol: str, interval: str = "1d", limit: int = 30) -> str:
        """
        调用Binance API获取K线数据
        """
        try:
            url = "https://api.binance.com/api/v3/klines"
            params = {
                "symbol": symbol.upper(),
                "interval": interval,
                "limit": limit
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # 格式化K线数据
            klines = []
            for kline in data:
                klines.append({
                    "time": datetime.fromtimestamp(kline[0] / 1000).strftime("%Y-%m-%d %H:%M"),
                    "open": float(kline[1]),
                    "high": float(kline[2]),
                    "low": float(kline[3]),
                    "close": float(kline[4]),
                    "volume": float(kline[5])
                })
            
            # 计算一些基本统计
            closes = [k["close"] for k in klines]
            current_price = closes[-1]
            price_change = ((closes[-1] - closes[0]) / closes[0]) * 100
            high_price = max(k["high"] for k in klines)
            low_price = min(k["low"] for k in klines)
            avg_volume = sum(k["volume"] for k in klines) / len(klines)
            
            # 简单的趋势判断
            ma7 = sum(closes[-7:]) / 7 if len(closes) >= 7 else sum(closes) / len(closes)
            ma20 = sum(closes[-20:]) / 20 if len(closes) >= 20 else sum(closes) / len(closes)
            
            result = f"""
=== {symbol} K线数据分析 ===
时间范围: {klines[0]['time']} 至 {klines[-1]['time']}
K线数量: {len(klines)} 根 ({interval})

【价格概览】
当前价格: ${current_price:,.2f}
期间涨跌幅: {price_change:+.2f}%
最高价: ${high_price:,.2f}
最低价: ${low_price:,.2f}
平均成交量: {avg_volume:,.2f}

【均线参考】
MA7: ${ma7:,.2f} {'(价格在MA7上方)' if current_price > ma7 else '(价格在MA7下方)'}
MA20: ${ma20:,.2f} {'(价格在MA20上方)' if current_price > ma20 else '(价格在MA20下方)'}
MA7 vs MA20: {'金叉(MA7>MA20, 看涨信号)' if ma7 > ma20 else '死叉(MA7<MA20, 看跌信号)'}

【最近5根K线详情】
"""
            for k in klines[-5:]:
                change = ((k["close"] - k["open"]) / k["open"]) * 100
                result += f"  {k['time']}: O=${k['open']:,.2f} H=${k['high']:,.2f} L=${k['low']:,.2f} C=${k['close']:,.2f} ({change:+.2f}%)\n"
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"获取K线数据失败: {str(e)}"
        except Exception as e:
            return f"处理K线数据时出错: {str(e)}"


class GetCryptoNewsInput(BaseModel):
    """获取加密货币新闻的输入参数"""
    symbol: str = Field(..., description="加密货币符号，例如 BTC, ETH, SOL")


class GetCryptoNewsTool(BaseTool):
    """获取加密货币相关新闻的工具"""
    name: str = "get_crypto_news"
    description: str = "搜索指定加密货币最近3天的相关新闻，用于分析市场情绪和重大事件。"
    args_schema: Type[BaseModel] = GetCryptoNewsInput

    def _run(self, symbol: str) -> str:
        """
        使用Serper API搜索加密货币新闻
        """
        try:
            api_key = os.environ.get("SERPER_API_KEY", "")
            if not api_key:
                return "错误: 未设置 SERPER_API_KEY 环境变量"
            
            # 构建搜索查询
            # 获取币种全名
            symbol_names = {
                "BTC": "Bitcoin",
                "ETH": "Ethereum",
                "SOL": "Solana",
                "BNB": "BNB",
                "XRP": "Ripple",
                "ADA": "Cardano",
                "DOGE": "Dogecoin",
                "DOT": "Polkadot",
            }
            
            coin_name = symbol_names.get(symbol.upper().replace("USDT", ""), symbol)
            search_query = f"{coin_name} cryptocurrency news"
            
            url = "https://google.serper.dev/news"
            headers = {
                "X-API-KEY": api_key,
                "Content-Type": "application/json"
            }
            payload = {
                "q": search_query,
                "num": 10,
                "tbs": "qdr:d3"  # 最近3天
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            news_items = data.get("news", [])
            
            if not news_items:
                return f"未找到与 {symbol} 相关的最近3天新闻"
            
            result = f"""
=== {symbol} ({coin_name}) 最近3天新闻 ===
搜索时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}
新闻数量: {len(news_items)} 条

"""
            for i, news in enumerate(news_items[:10], 1):
                title = news.get("title", "无标题")
                snippet = news.get("snippet", "无摘要")
                source = news.get("source", "未知来源")
                date = news.get("date", "未知时间")
                link = news.get("link", "")
                
                result += f"""【新闻 {i}】
标题: {title}
来源: {source} | {date}
摘要: {snippet}
链接: {link}

"""
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"获取新闻数据失败: {str(e)}"
        except Exception as e:
            return f"处理新闻数据时出错: {str(e)}"
