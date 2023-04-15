import openai
from config.credentials import OPENAI_API_KEY

class OpenAIGPT3Adapter:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
    
    def generate_response(self, prompt, context=[]):
        """
        Generates a response using OpenAI GPT 3.5.
        """

        # Default context
        if context == []:
            context = [{'role': 'system', 'content': 'You are a chatbot called OmniChat. You are talking to a human.'}]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                *context,
                {'role': 'user', 'content': prompt},
            ],
        )
        return response.choices[0].message.content
