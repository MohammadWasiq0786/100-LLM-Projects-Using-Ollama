"""
Project 92. Chain-of-Thought Reasoning Demo

Description:
This demo shows how large language models can solve complex problems more accurately when encouraged to "think step by step." 
You’ll input a question and see how the model reasons before answering.
"""

import os
import ollama
import gradio as gr
 
# Function to generate chain-of-thought response
def chain_of_thought_reasoning(question):
    try:
        # Chain-of-thought style prompt
        prompt = (
            "You are a helpful reasoning assistant. For each question, explain your thinking step by step before giving the final answer.\n\n"
            f"Question: {question}\n"
            "Let's think step by step:"
        )
 
        # Request from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=[{"role": "user", "content": prompt}]
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio UI
iface = gr.Interface(
    fn=chain_of_thought_reasoning,
    inputs=gr.Textbox(label="Enter a Complex Question (e.g., math, logic, decision-making)"),
    outputs="text",
    title="🧠 Chain-of-Thought Reasoning Demo",
    description="Ask a challenging question and the model will 'think step by step' to arrive at a clear answer."
)
 
# Launch the demo
iface.launch()