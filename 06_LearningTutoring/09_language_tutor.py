"""
Project 59. AI Language Tutor (e.g. Spanish)

Description:
This AI-powered tutor helps you learn any language by teaching vocabulary, grammar rules, and useful phrases. 
It can simulate conversations, translate your answers, and explain mistakes—all in a friendly, personalized way.
"""

import ollama
import os
import gradio as gr
 
 
# Function for language tutoring
def language_tutor(input_text, target_language, practice_type):
    # System prompt: make the AI act as a patient language teacher
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a helpful and friendly language tutor for {target_language}. Depending on the practice type, "
                f"you will either teach vocabulary, correct grammar, explain a sentence, or simulate a simple conversation "
                f"with the user. Use beginner-friendly language and always give explanations."
            )
        },
        {
            "role": "user",
            "content": f"Practice type: {practice_type}\nInput: {input_text}"
        }
    ]
 
    try:
        # Request from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for the language tutor
iface = gr.Interface(
    fn=language_tutor,
    inputs=[
        gr.Textbox(label="Write something to translate, learn, or ask about"),
        gr.Textbox(label="Target Language (e.g. Spanish, French, Japanese)"),
        gr.Radio(
            ["vocabulary help", "grammar correction", "sentence explanation", "conversation practice"],
            label="Practice Type"
        )
    ],
    outputs="text",
    title="🗣️ AI Language Tutor",
    description="Learn a new language with help from your AI tutor. Practice vocabulary, grammar, conversations, or ask anything!"
)
 
# Launch the tutor
iface.launch()