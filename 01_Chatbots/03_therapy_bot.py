"""
Project 3. Therapy Bot with Empathetic Tone

Description:
This project builds a supportive, non-judgmental chatbot designed to simulate a virtual therapy session. 
The bot listens, responds with empathy, and encourages self-reflection. 
It doesn’t provide clinical advice but acts as a kind listener using an empathetic prompt style. 
Perfect for practicing tone, prompt design, and emotional intelligence in LLMs.
"""

import ollama
import gradio as gr
import os

def therapy_response(user_input):
    messages = [
        {"role": "system", "content": 
         "You are a compassionate and empathetic virtual therapist. "
         "You listen carefully, validate the user's emotions, and offer gentle, supportive guidance. "
         "Do not diagnose or give medical advice. Use a calm, warm tone."},
        {"role": "user", "content": user_input}
    ]
    
    try:
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
 
iface = gr.Interface(
    fn=therapy_response,
    inputs="text",
    outputs="text",
    title="🧠 EmpathyBot – Virtual Therapy Chat",
    description="Talk about how you're feeling. This bot responds with warmth and kindness. (Not a substitute for real therapy.)"
)
 
iface.launch()