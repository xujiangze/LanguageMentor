import yaml


class Config(object):
    SUPPORT_LLM_TYPE_OLLAMA = "ollama"
    SUPPORT_LLM_TYPE_OPENAI = "openai"
    SUPPORT_LLM_TYPES = [SUPPORT_LLM_TYPE_OLLAMA, SUPPORT_LLM_TYPE_OPENAI]

    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)

    def load_config(self, file_path):
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            cfg = yaml.safe_load(file)
        return cfg

    def get_llm_config(self):
        llm_config = self.config['llm']
        llm_types = self.SUPPORT_LLM_TYPES
        llm_type = llm_config.get("llm_type", "ollama")
        if llm_type not in llm_types:
            raise ValueError(f"llm_type must be one of {llm_types}")
        return {
            "llm_type": llm_type,  # 支持配置参数, llm_type
            "model": llm_config.get("model", "llama3.1:8b-instruct-q8_0"),  # 支持配置参数, model
            "max_tokens": llm_config.get("max_tokens", 8192),  # 支持配置参数, max_tokens
            "temperature": llm_config.get("temperature", 0.8),  # 支持配置参数, temperature
            "api_key": llm_config.get("api_key", None),  # 支持配置参数, api_key
            "base_url": llm_config.get("base_url", None)  # 支持配置参数, base_url
        }


global_config = Config('src/config/config_test.yaml')


if __name__ == '__main__':
    cfg_client = Config('config.yaml')
    print(cfg_client.config)
