"""
Project 100. Multilingual Prompt Tester

Description:
This app lets you input a prompt and see how it performs across different languages. 
It’s great for testing multilingual model behavior, translation consistency, and global prompt effectiveness.
"""

import os
import ollama
import gradio as gr

 
# Supported languages
language_map = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh",
    "Arabic": "ar",
    "Japanese": "ja"
}
 
# Function to translate and respond
def multilingual_prompt(prompt, language):
    try:
        # Prompt the model to respond in the selected language
        messages = [
            {
                "role": "system",
                "content": f"You are a helpful assistant. Respond only in {language}."
            },
            {
                "role": "user",
                "content": prompt
            }
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
    fn=multilingual_prompt,
    inputs=[
        gr.Textbox(label="Enter Prompt in English"),
        gr.Dropdown(list(language_map.keys()), label="Choose Output Language")
    ],
    outputs="text",
    title="🌍 Multilingual Prompt Tester",
    description="Enter a prompt and see how GPT responds in different languages. Useful for translation and global UX testing."
)
 
# Launch the tester
iface.launch()