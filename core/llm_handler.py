from llm_adapters import get_llm_adapter

class LLMHandler:
    def __init__(self, supported_llms=None):
        self.supported_llms = supported_llms or []
        self.llm_adapters = {llm: get_llm_adapter(llm) for llm in self.supported_llms}
    
    def generate_response(self, prompt, context, llm_name):
        """
        Generates a response using the specified LLM.

        :param prompt: The input text or prompt for the model.
        :param context: The input context / message history for the model.
        :param llm_name: The name of the LLM to use for generating the response.
        :return: Generated text from the model.
        """
        if llm_name not in self.supported_llms:
            raise ValueError(f"LLM {llm_name} is not supported by this handler.")
        
        adapter = self.llm_adapters[llm_name]
        response = adapter.generate_response(prompt, context)
        return response
    
    def add_llm(self, llm_name):
        """
        Adds a new LLM to the handler.

        :param llm_name: The name of the LLM to be added.
        """
        if llm_name in self.supported_llms:
            raise ValueError(f"LLM {llm_name} is already supported by this handler.")
        
        self.supported_llms.append(llm_name)
        self.llm_adapters[llm_name] = get_llm_adapter(llm_name)
