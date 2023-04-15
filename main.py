from core.chat_engine import ChatEngine
from core.utils import format_conversation_history

def main():
    # Initialize the ChatEngine with supported LLMs
    chat_engine = ChatEngine(supported_llms=['openai_gpt3'])

    # Register a new user
    user_id = 'user'
    chat_engine.register_user(user_id)

    print("Welcome to OmniChat! You can start chatting with me now or type 'exit' to quit the application.\n")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit application if user types 'exit'
        if user_input.lower() == 'exit':
            break

        # Process the user input and get the LLM-generated response
        response = chat_engine.process_input(
            user_id=user_id,
            user_input=user_input,
            llm_name='openai_gpt3',
        )

        # Print LLM-generated response
        print(f"OmniChat: {response}")
    
    # Retrieve and display the conversation history
    conversation_history = chat_engine.get_conversation_history(user_id)
    print("\nConversation History:")
    print(format_conversation_history(conversation_history))

if __name__ == '__main__':
    main()
