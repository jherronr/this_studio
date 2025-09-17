import ollama
import gradio as gr

# --- Core Chat Logic ---
# This function will handle the conversation with the Ollama model.
# It takes the user's message and the chat history as input.
def chat_with_llama(message, history):
    """
    Handles the chat logic by sending the user message and history to the Ollama model.
    It streams the response back to the UI.
    """
    # Format the history for the Ollama client
    # The history object from Gradio needs to be converted to the format Ollama expects.
    messages = []
    for user_msg, assistant_msg in history:
        messages.append({'role': 'user', 'content': user_msg})
        messages.append({'role': 'assistant', 'content': assistant_msg})
    
    # Add the current user message
    messages.append({'role': 'user', 'content': message})

    # Use the ollama.chat function with streaming
    # 'stream=True' allows the model to return tokens as they are generated,
    # creating the "typing" effect seen in ChatGPT.
    stream = ollama.chat(
        model='llama3:8b', # The model we downloaded earlier
        messages=messages,
        stream=True
    )

    # Yield each part of the stream to update the UI incrementally
    partial_message = ""
    for chunk in stream:
        token = chunk['message']['content']
        partial_message += token
        yield partial_message

# --- Gradio User Interface ---
# This creates the web interface for our chat application.
# gr.ChatInterface is a high-level component that provides a full chat UI.
chat_interface = gr.ChatInterface(
    fn=chat_with_llama,  # The function to call when the user sends a message
    title="Llama 3 Chat (Hosted on Lightning.ai)",
    description="A simple chat interface for Llama 3 running with Ollama."
)

# --- Launch the Application ---
# The .launch() method starts the web server.
# Lightning.ai will automatically detect this and expose a public URL for you.
chat_interface.launch(share=True)