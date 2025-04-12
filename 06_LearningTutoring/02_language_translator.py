"""
Project 52. Language Translator

Description:
This multilingual translator lets you convert any sentence into another language with clarity and cultural tone. 
Great for travelers, language learners, or global communication. It even adapts to formality and slang!
"""

import ollama
import os
import gradio as gr
 


# Function to translate text
def translate_text(text, target_language, style):
    # Prompt the assistant to act as a fluent translator
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a professional language translator. Translate the following sentence into {target_language} "
                f"in a {style} tone. Ensure it's grammatically accurate and natural for a native speaker."
            )
        },
        {
            "role": "user",
            "content": text
        }
    ]
 
    try:
        # Call Ollama to translate
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the translated text
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Text to Translate"),
        gr.Textbox(label="Target Language (e.g. French, Japanese, Spanish)"),
        gr.Radio(["formal", "casual", "slang", "professional"], label="Tone/Style")
    ],
    outputs="text",
    title="🌐 Language Translator",
    description="Type a sentence, choose the target language and tone, and I’ll give you a clear and accurate translation."
)
 
# Launch the app
iface.launch()