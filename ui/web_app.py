import os
import sys

import gradio as gr

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.chat_engine import ChatEngine
from core.utils import format_conversation_history

# Initialize the ChatEngine with supported LLMs
chat_engine = ChatEngine(supported_llms=["openai_gpt3"])

# Register a user
user_id = "user"
chat_engine.register_user(user_id)

def chat(user_input, model):
    # Process the user input and get a response from the LLM
    response = chat_engine.process_input(user_id, user_input, model)
    
    # Get the conversation history
    conversation_history = chat_engine.get_conversation_history(user_id)
    formatted_history = format_conversation_history(conversation_history)
    formatted_history = formatted_history.replace("\n", "<br>")

    return response, formatted_history

# Create a Gradio interface
iface = gr.Interface(
    fn=chat,
    inputs=[
        gr.inputs.Textbox(label="User Input", lines=3, placeholder="Type your message here..."),
        gr.inputs.Dropdown(choices=["openai_gpt3"], label="Select Model")
    ],
    outputs=[
        gr.outputs.Textbox(label="Response"),
        gr.outputs.HTML(label="Chat Log")
    ],
    title="OmniChat",
    description="A web app to interact with Large Language Models through a single interface.",
    allow_flagging=False,
    theme="default",
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
