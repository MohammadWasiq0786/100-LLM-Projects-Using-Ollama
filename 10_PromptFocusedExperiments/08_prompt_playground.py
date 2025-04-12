"""
Project 98. Prompt Playground (tweak and compare)

Description:
This tool is an open sandbox for testing and comparing multiple prompt variations side by side. 
It’s ideal for understanding how small tweaks in wording, tone, or structure affect model outputs—perfect for refining prompts iteratively.
"""

import os
import ollama
import gradio as gr
 

# Function to compare two prompt versions
def compare_prompts(prompt1, prompt2):
    try:
        # Get response for prompt 1
        response1 = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=[{"role": "user", "content": prompt1}]
        )
 
        # Get response for prompt 2
        response2 = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=[{"role": "user", "content": prompt2}]
        )
 
        output1 = response1["message"]["content"].strip()
        output2 = response2["message"]["content"].strip()
 
        return output1, output2
 
    except Exception as e:
        return f"Error: {str(e)}", ""
 
# Gradio Interface
iface = gr.Interface(
    fn=compare_prompts,
    inputs=[
        gr.Textbox(label="Prompt 1", lines=4, placeholder="Enter your first version of the prompt"),
        gr.Textbox(label="Prompt 2", lines=4, placeholder="Enter your second version")
    ],
    outputs=[
        gr.Textbox(label="Response to Prompt 1", lines=6),
        gr.Textbox(label="Response to Prompt 2", lines=6)
    ],
    title="🎮 Prompt Playground – Tweak & Compare",
    description="Enter two variations of a prompt and see how the model responds to each. Great for fine-tuning your prompt design."
)
 
# Launch the playground
iface.launch()