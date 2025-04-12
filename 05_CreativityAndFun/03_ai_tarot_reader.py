"""
Project 43. AI Tarot Reader

Description:
This fun and whimsical AI simulates a tarot card reading. You can ask a question or just request a general reading, and 
it will draw 3 virtual cards—interpreting their meaning and offering insight with a touch of magic and mystery.
"""

import ollama
import os
import gradio as gr
 
 
# Function to perform an AI tarot reading
def tarot_reading(question_or_context):
    # Set the AI to act like a mystical tarot reader
    messages = [
        {
            "role": "system",
            "content": (
                "You are a wise and mystical tarot reader. Conduct a 3-card tarot reading for the user based on their question or intention. "
                "For each card, give the name, symbolism, and interpretation in the context of the user's life. End with a spiritual insight or guidance. "
                "Keep the tone magical, warm, and thoughtful."
            )
        },
        {
            "role": "user",
            "content": f"My tarot reading question: {question_or_context}"
        }
    ]
 
    try:
        # Request tarot reading from OpenAI
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return tarot reading result
        return response['message']['content'].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for tarot reading
iface = gr.Interface(
    fn=tarot_reading,
    inputs=gr.Textbox(lines=2, label="Your Question or Intention (e.g. What's next in my career?)"),
    outputs="text",
    title="🔮 AI Tarot Reader",
    description="Enter a question or topic on your mind, and I’ll draw three tarot cards and interpret them in a mystical, insightful way."
)
 
# Launch the virtual tarot reader
iface.launch()