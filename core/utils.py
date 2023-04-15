import re

def sanitize_input(input_text):
    """
    Sanitizes the input text by removing any special characters.

    :param input_text: The input text.
    :return: The sanitized text.
    """
    input_text = re.sub(r'\s+', ' ', input_text).strip()
    return input_text

def shorten_response(response, max_length):
    """
    Shortens the response to the specified maximum length.

    :param response: The response to be shortened.
    :param max_length: The maximum length of the response.
    :return: The shortened response.
    """
    if len(response) > max_length:
        response = response[:max_length]
        response = response[:response.rfind(' ')] + '...'
    return response

def format_conversation_history(conversation_history):
    """
    Formats the conversation history for display.

    :param conversation_history: A list containing user input and LLM-generated responses.
    :return: A formatted string representing the conversation history.
    """
    formatted_history = ''
    for i, message in enumerate(conversation_history):
        formatted_history += f"{i:03d}. {message['role'].capitalize()}: {message['content']}\n"
    return formatted_history
