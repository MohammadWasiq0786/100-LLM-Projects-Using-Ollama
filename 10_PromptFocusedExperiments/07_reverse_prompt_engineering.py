"""
Project 97. Reverse Prompt Engineering (guess what prompt made this)

Description:
This tool takes a model-generated response and tries to guess what prompt could have produced it. 
It helps you understand how prompts guide output—perfect for learning prompt design through reverse engineering.
"""

import os
import ollama
import gradio as gr
 
# Function to guess the original prompt
def reverse_engineer_prompt(model_output):
    try:
        # Prompt the LLM to guess what led to the output
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a reverse prompt engineer. Given a piece of model-generated output, guess what kind of prompt might have created it. "
                    "Try to infer the user's intent and reconstruct a suitable original prompt."
                )
            },
            {
                "role": "user",
                "content": f"Here is the AI-generated output:\n\n{model_output}\n\nGuess the original prompt:"
            }
        ]
 
        # Call Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI
iface = gr.Interface(
    fn=reverse_engineer_prompt,
    inputs=gr.Textbox(label="Paste the AI-Generated Output"),
    outputs="text",
    title="🕵️‍♂️ Reverse Prompt Engineering",
    description="Paste an AI response, and this app will guess what kind of prompt could have generated it."
)
 
# Launch the reverse engineer
iface.launch()