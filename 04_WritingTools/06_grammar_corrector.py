"""
Project 36. Grammar Corrector

Description:
This tool takes any block of text and corrects spelling, grammar, and punctuation mistakes. 
It also improves clarity and flow—making your writing polished, professional, and easy to read. 
Perfect for emails, essays, or social posts.
"""

import ollama
import os
import gradio as gr

 
# Function to correct grammar
def correct_grammar(input_text):
    # System prompt makes the assistant act like a proofreader
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert grammar editor. Review the following text and correct any grammar, spelling, punctuation, or clarity issues. "
                "Keep the meaning and tone intact while making it polished and professional."
            )
        },
        {
            "role": "user",
            "content": input_text
        }
    ]
 
    try:
        # Call Ollama for grammar correction
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the corrected version
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=correct_grammar,                                   # Grammar correction function
    inputs=gr.Textbox(lines=6, label="Your Text"),        # User input
    outputs="text",                                       # Output the corrected version
    title="✍️ Grammar Corrector",
    description="Paste any paragraph or message to fix grammar, spelling, and punctuation. Your writing, polished!"
)
 
# Launch the tool
iface.launch()