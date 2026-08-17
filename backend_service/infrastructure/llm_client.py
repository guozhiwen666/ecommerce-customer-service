"""
通过LangChain定义LLM客户端
模块之间的组件导入的标准写法：
1.导入sdk自带的
2.导入第三方的
3.导入自己定义
"""
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from backend_service.config.settings import settings

llm_client: BaseChatModel = init_chat_model(
    model_provider="openai",
    model=settings.llm_model,
    api_key=settings.llm_api_key,
    base_url=settings.llm_base_url
)