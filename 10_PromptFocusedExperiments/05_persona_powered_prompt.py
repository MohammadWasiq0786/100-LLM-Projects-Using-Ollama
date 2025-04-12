"""
Project 95. Persona-Powered Prompt App (e.g. “Wise Mentor”)

Description:
This app lets you assign your assistant a unique persona—like “wise mentor,” “sarcastic teenager,” or “strict professor.” 
It tailors the assistant’s tone, language, and attitude accordingly, making it great for role-based interactions or playful experiences.
"""

import os
import ollama
import gradio as gr
 
# Function to generate persona-based response
def persona_chat(persona, message):
    try:
        # System prompt to define persona
        system_prompt = f"You are an AI assistant with the persona of a {persona}. Respond accordingly."
 
        # Prepare messages for chat
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
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
    fn=persona_chat,
    inputs=[
        gr.Textbox(label="Persona (e.g. wise mentor, pirate captain, sarcastic teenager)"),
        gr.Textbox(label="Your Message")
    ],
    outputs="text",
    title="🎭 Persona-Powered Prompt App",
    description="Give your AI a character—talk to it like a pirate, teacher, therapist, or wizard!"
)
 
# Launch the persona bot
iface.launch()