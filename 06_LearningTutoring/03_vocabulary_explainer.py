"""
Project 53. Vocabulary Explainer

Description:
This tool explains any word like a teacher—offering definition, pronunciation, part of speech, usage in a sentence, 
and even a visual metaphor when helpful. It’s perfect for students, writers, or non-native speakers building vocabulary.
"""

import ollama
import os
import gradio as gr
 
 
# Function to explain vocabulary words
def explain_word(word):
    # Prompt the assistant to act like a dictionary + friendly tutor
    messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly English tutor. For the word provided, return:\n"
                "1. Definition\n"
                "2. Part of speech\n"
                "3. Pronunciation (using phonetics)\n"
                "4. Example sentence\n"
                "5. A metaphor or image to remember it\n"
                "Be clear and concise."
            )
        },
        {
            "role": "user",
            "content": word
        }
    ]
 
    try:
        # Query Ollama to explain the word
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return detailed explanation
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for vocabulary explanation
iface = gr.Interface(
    fn=explain_word,
    inputs=gr.Textbox(label="Enter a Word (e.g. ephemeral, audacity, benevolent)"),
    outputs="text",
    title="📘 Vocabulary Explainer",
    description="Enter any word to get a clear definition, part of speech, pronunciation, an example sentence, and a fun memory aid."
)
 
# Launch the app
iface.launch()