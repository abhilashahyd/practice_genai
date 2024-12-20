
import gradio as gr
import time

def generate_response(message, history):
    """
        Your code for generating a response
    """
    return response

demo = gr.ChatInterface(
    fn=generate_response, 
    examples=[{"text": "Hello", "files": []}], 
    title="Echo Bot", 
    multimodal=True)

demo.launch()