"""
Project 91. Few-Shot Prompt Example App

Description:
This tool shows how to guide LLMs by giving a few well-crafted examples. You define an input-output pattern, 
and then test it with a new input—watch how the model generalizes based on your few-shot examples.
"""

import os
import ollama
import gradio as gr

 
# Function to apply few-shot prompting
def few_shot_prompt(examples, new_input):
    try:
        # Prepare the few-shot prompt format
        prompt = "You are an intelligent assistant. Learn from these examples:\n\n"
        prompt += examples.strip() + "\n\n"
        prompt += f"Now respond to the new input:\nInput: {new_input}\nOutput:"
 
        # Send to Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=[{"role": "user", "content": prompt}]
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio Interface
iface = gr.Interface(
    fn=few_shot_prompt,
    inputs=[
        gr.Textbox(lines=10, label="Few-Shot Examples (e.g. Input: X\nOutput: Y)"),
        gr.Textbox(label="New Input")
    ],
    outputs="text",
    title="🎯 Few-Shot Prompting Demo",
    description="Give 2–3 examples of input-output pairs, then add a new input to see how the LLM generalizes."
)
 
# Launch the app
iface.launch()