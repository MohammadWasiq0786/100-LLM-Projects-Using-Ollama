"""
Project 49. “Explain Like I’m 5” App

Description:
This tool explains complex topics in a way even a 5-year-old could understand. 
Whether it’s quantum physics, inflation, or blockchain—it breaks it down into simple, fun, and friendly language. 
Great for kids, beginners, or curious minds!
"""

import ollama
import os
import gradio as gr
 
 
# Function to simplify a complex topic
def explain_eli5(topic):
    # Prompt AI to act like a fun, patient teacher for a 5-year-old
    messages = [
        {
            "role": "system",
            "content": (
                "You are a kind and fun teacher explaining things to a 5-year-old. "
                "Break down complex topics into very simple explanations using everyday examples, analogies, and friendly tone."
            )
        },
        {
            "role": "user",
            "content": f"Explain: {topic}"
        }
    ]
 
    try:
        # Ask Ollama for a simplified explanation
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the ELI5 explanation
        return response['message']['content'].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for ELI5 explanations
iface = gr.Interface(
    fn=explain_eli5,
    inputs=gr.Textbox(label="Enter a Topic (e.g. black holes, AI, inflation)"),
    outputs="text",
    title="🧠 Explain Like I'm 5 (ELI5)",
    description="Type any complex topic and I’ll explain it in a way a 5-year-old can understand. Simple, fun, and crystal clear!"
)
 
# Launch the ELI5 explainer
iface.launch()