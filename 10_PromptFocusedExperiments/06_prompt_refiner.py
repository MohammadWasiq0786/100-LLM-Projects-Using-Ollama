"""
Project 96. Prompt Refiner (AI improves your prompt)

Description:
This tool takes a rough or unclear prompt and rewrites it to be clearer, more specific, and optimized for better LLM responses. 
Ideal for users who want to upgrade their prompt engineering skills or fine-tune task clarity.
"""

import os
import ollama
import gradio as gr
 

# Function to refine the user's prompt
def refine_prompt(user_prompt):
    try:
        # Ask GPT to act as a prompt engineer
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert in prompt engineering. Take the user's vague or basic prompt and improve it. "
                    "Make it more specific, focused, and likely to produce a high-quality output from a language model. "
                    "Also keep it in the same tone unless requested otherwise."
                )
            },
            {
                "role": "user",
                "content": f"Here is the original prompt:\n{user_prompt}\n\nRefine this prompt."
            }
        ]
 
        # Get refined prompt
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        return response["message"]["content"].strip()
    
    except Exception as e:
        return f"Error refining prompt: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=refine_prompt,
    inputs=gr.Textbox(label="Enter Your Prompt (Rough, Vague, or Simple)"),
    outputs="text",
    title="✨ Prompt Refiner",
    description="Paste a simple or unclear prompt and get back an optimized version ready to use with any LLM."
)
 
# Launch the refiner
iface.launch()