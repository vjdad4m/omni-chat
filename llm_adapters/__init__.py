from .openai_gpt3 import OpenAIGPT3Adapter
from .chatglm_6b import ChatGLM6BAdapter

# Add more LLM import as needed

# Registry of available LLM adapters
LLM_ADAPTERS = {
    'openai_gpt3': OpenAIGPT3Adapter,
    'chatglm_6b': ChatGLM6BAdapter,
    # Add more LLM adapters to the registry
}

def get_llm_adapter(adapter_name):
    """
    Returns an instance of the requested LLM adapter.

    :param adapter_name: The name of the adapter to be fetched.
    :return: An instance of the requested LLM adapter.
    """
    adapter_class = LLM_ADAPTERS.get(adapter_name)
    if adapter_class is None:
        raise ValueError(f"Unknown LLM adapter: {adapter_name}")

    try:
        return adapter_class()
    except:
        # TODO: Log the error
        return None
