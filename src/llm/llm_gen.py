from langchain_ollama.chat_models import ChatOllama  # 导入 ChatOllama 模型
from langchain_openai import ChatOpenAI
from config.config import Config # 导入配置类


def llm_gen(config_client: Config):
    llm_type = config_client.get_llm_config()["llm_type"]
    # 初始化 ChatOllama 模型，配置模型参数
    if llm_type not in Config.SUPPORT_LLM_TYPES:
        raise ValueError(f"llm_type must be one of {Config.SUPPORT_LLM_TYPES}")

    llm_config = config_client.get_llm_config()

    if llm_type == Config.SUPPORT_LLM_TYPE_OPENAI:
        return gen_openai_llm(**llm_config)

    if llm_type == Config.SUPPORT_LLM_TYPE_OLLAMA:
        return gen_ollama_llm(**llm_config)

    raise ValueError(f"llm_type must be one of {Config.SUPPORT_LLM_TYPES}")


def gen_openai_llm(model, max_tokens, temperature, api_key, base_url, **kwargs):
    return ChatOpenAI(
        model=model,  # 使用的模型名称
        max_tokens=max_tokens,  # 最大生成的token数
        temperature=temperature,  # 生成文本的随机性
        api_key=api_key,
        base_url=base_url
    )


def gen_ollama_llm(model, max_tokens, temperature, **kwargs):
    return ChatOllama(
        model=model,  # 使用的模型名称
        max_tokens=max_tokens,  # 最大生成的token数
        temperature=temperature,  # 生成文本的随机性
    )
