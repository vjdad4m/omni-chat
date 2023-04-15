from .llm_handler import LLMHandler
from .utils import sanitize_input

class ChatEngine:
    def __init__(self, supported_llms=None):
        self.llm_handler = LLMHandler(supported_llms=supported_llms)
        self.conversation_history = {}
        self.users = set()

    def register_user(self, user_id):
        """
        Registers a new user.

        :param user_id: The ID of the user to be registered.
        """
        if user_id not in self.users:
            self.users.add(user_id)
            self.conversation_history[user_id] = []
        else:
            raise ValueError(f"User {user_id} is already registered.")

    def process_input(self, user_id, user_input, llm_name, add_to_history=True):
        """
        Processes the user input and returns the LLM-generated response.

        :param user_id: The unique identifier for the user.
        :param user_input: The input text from the user.
        :param llm_name: The name of the LLM to be used for generating the response.
        :param add_to_history: Whether to add the user input and the generated response to the conversation history.
        :return: Generated text from the model.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        # Sanitize input
        user_input = sanitize_input(user_input)

        response = self.llm_handler.generate_response(
            user_input,
            self.conversation_history[user_id],
            llm_name,
        )

        if add_to_history:
            self.conversation_history[user_id].append({'role': 'user', 'content': user_input})
            self.conversation_history[user_id].append({'role': 'system', 'content': response})

        return response

    def get_conversation_history(self, user_id):
        """
        Returns the conversation history for the specified user.

        :param user_id: The unique identifier for the user.
        :return: The conversation history for the specified user.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        return self.conversation_history[user_id]

    def add_llm(self, llm_name):
        """
        Adds a new LLM to the handler.

        :param llm_name: The name of the LLM to be added.
        """
        self.llm_handler.add_llm(llm_name)
    