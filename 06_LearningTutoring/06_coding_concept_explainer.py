"""
Project 56. Coding Concept Explainer

Description:
This tool explains programming concepts in plain, beginner-friendly language. Whether you want to understand recursion, APIs, 
variables, or OOP—it provides examples, analogies, and even simple code snippets to help you truly get it.
"""

import ollama
import os
import gradio as gr
 
 
# Function to explain coding concepts
def explain_concept(concept, level):
    # Prompt the assistant to act like a coding mentor
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a friendly coding teacher. Explain the concept '{concept}' in a {level} way. "
                "Include a definition, a simple analogy, a code example (in Python), and a summary."
            )
        },
        {
            "role": "user",
            "content": concept
        }
    ]
 
    try:
        # Get concept explanation from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the explanation
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=explain_concept,
    inputs=[
        gr.Textbox(label="Enter a Coding Concept (e.g. recursion, list comprehension, class, API)"),
        gr.Radio(["beginner", "intermediate", "advanced"], label="Explanation Level")
    ],
    outputs="text",
    title="💡 Coding Concept Explainer",
    description="Type a coding term and choose your level. Get a clear explanation, analogy, and simple code snippet!"
)
 
# Launch the explainer
iface.launch()