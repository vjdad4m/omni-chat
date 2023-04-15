from transformers import AutoTokenizer, AutoModel

class ChatGLM6BAdapter:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
        self.model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()

    def generate_response(self, prompt, context=[]):
        """
        Generates a response using OpenAI GPT 3.5.
        """

        # Default context
        if context == []:
            context = [{'role': 'system', 'content': 'You are a chatbot called OmniChat. You are talking to a human.'}]

        # Build history
        history = []
        for i in range(len(context) // 2):
            history.append((context[i * 2]['content'], context[i * 2 + 1]['content']))

        # Run inference
        for response, history in self.model.stream_chat(self.tokenizer, prompt, history=history):
            pass

        return response
