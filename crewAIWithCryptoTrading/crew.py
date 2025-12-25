# 核心功能:在CrewAI中定义Agent和Task，并通过Crew来管理这些Agent和Task的执行流程

# 导入相关的依赖包
from typing import List
from crewai import Agent, Crew, Process, Task
# CrewBase是一个装饰器，标记一个类为CrewAI项目。agent、task和crew装饰器用于定义agent、task和crew
from crewai.project import CrewBase, agent, crew, task
# 导入自定义工具
from tools.crypto_tools import GetKlineDataTool, GetCryptoNewsTool
from pydantic import BaseModel, Field


# 定义输出数据模型
class TechnicalAnalysis(BaseModel):
    """技术分析报告模型"""
    trend: str = Field(..., description="趋势判断: 上涨/下跌/震荡")
    support_level: str = Field(..., description="支撑位")
    resistance_level: str = Field(..., description="阻力位")
    signals: List[str] = Field(..., description="技术信号列表")
    summary: str = Field(..., description="分析总结")


class NewsAnalysis(BaseModel):
    """新闻分析报告模型"""
    sentiment: str = Field(..., description="市场情绪: 看涨/看跌/中性")
    major_events: List[str] = Field(..., description="重大事件列表")
    news_summary: List[str] = Field(..., description="关键新闻摘要")


class TradingRecommendation(BaseModel):
    """交易建议模型"""
    action: str = Field(..., description="操作建议: 买入/卖出/持有")
    entry_price: str = Field(..., description="建议入场价位")
    stop_loss: str = Field(..., description="建议止损价位")
    target_price: str = Field(..., description="目标价位")
    confidence: str = Field(..., description="信心等级: 高/中/低")
    risk_warning: str = Field(..., description="风险提示")
    reasoning: str = Field(..., description="建议理由")


# 定义了一个CryptoTradingCrew类并应用了@CrewBase装饰器初始化项目
@CrewBase
class CryptoTradingCrew():
    # agents_config和tasks_config分别指向agent和task的配置文件
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, model):
        # Agent使用的大模型
        self.model = model

    # K线技术分析Agent
    @agent
    def kline_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['kline_analyst'],
            verbose=True,
            llm=self.model,
            tools=[GetKlineDataTool()],
        )

    # 新闻分析Agent
    @agent
    def news_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['news_analyst'],
            verbose=True,
            llm=self.model,
            tools=[GetCryptoNewsTool()],
        )

    # 交易顾问Agent
    @agent
    def trading_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['trading_advisor'],
            verbose=True,
            llm=self.model,
        )

    # K线分析任务
    @task
    def kline_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['kline_analysis_task'],
        )

    # 新闻分析任务
    @task
    def news_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_analysis_task'],
        )

    # 交易建议任务
    @task
    def trading_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['trading_recommendation_task'],
            context=[self.kline_analysis_task(), self.news_analysis_task()],
        )

    # Crew定义
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
