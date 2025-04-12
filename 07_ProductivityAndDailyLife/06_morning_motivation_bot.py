"""
Project 66. Morning Motivation Bot

Description:
This uplifting bot sends you a personalized motivational message to start your day strong. Whether you want inspiration, confidence, 
gratitude, or focus—it delivers affirmations, quotes, and reminders tailored to your mood or goal.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate motivational message
def get_motivation(theme, mood):
    # Prompt the AI to act like a morning coach
    messages = [
        {
            "role": "system",
            "content": (
                "You are a morning motivation assistant. Generate an inspiring message based on the user's chosen theme and mood. "
                "Include an uplifting quote, a short affirmation, and one practical tip for the day. Keep it short, powerful, and positive."
            )
        },
        {
            "role": "user",
            "content": f"Theme: {theme}, Mood: {mood}"
        }
    ]
 
    try:
        # Call Ollama to generate the message
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the motivational message
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for the motivation bot
iface = gr.Interface(
    fn=get_motivation,
    inputs=[
        gr.Radio(["Confidence", "Gratitude", "Focus", "Courage", "Productivity"], label="Select a Theme"),
        gr.Radio(["Tired", "Anxious", "Hopeful", "Excited", "Neutral"], label="Current Mood")
    ],
    outputs="text",
    title="🌞 Morning Motivation Bot",
    description="Start your day with the right mindset. Get an inspiring quote, affirmation, and one practical tip based on your mood."
)
 
# Launch the bot
iface.launch()