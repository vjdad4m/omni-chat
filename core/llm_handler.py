from llm_adapters import get_llm_adapter

class LLMHandler:
    def __init__(self, supported_llms=None):
        self.supported_llms = supported_llms or []
        self._llm_instances = {}

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
        
        adapter = self.get_llm_instance(llm_name)
        if adapter is not None:
            response = adapter.generate_response(prompt, context)
            return response
        else:
            print(f"Could not load adapter for LLM {llm_name}.")
            return None

    
    def add_llm(self, llm_name):
        """
        Adds a new LLM to the handler.

        :param llm_name: The name of the LLM to be added.
        """
        if llm_name in self.supported_llms:
            raise ValueError(f"LLM {llm_name} is already supported by this handler.")
        
        self.supported_llms.append(llm_name)
        
    def get_llm_instance(self, llm_name):
        if llm_name not in self.supported_llms:
            raise ValueError(f"LLM {llm_name} is not supported by this handler.")
        
        if llm_name not in self._llm_instances:
            llm_adapter = get_llm_adapter(llm_name)
            if llm_adapter is not None:
                self._llm_instances[llm_name] = llm_adapter
            else:
                return None

        return self._llm_instances[llm_name]
