"""
Project 67. Meditation Script Generator

Description:
This serene tool creates guided meditation scripts based on your goal—like relaxation, focus, sleep, or self-love. 
Whether you want a short breathing session or a full 10-minute journey, the script helps calm the mind and center your thoughts.
"""

import ollama
import os
import gradio as gr

 
# Function to generate a meditation script
def generate_meditation_script(goal, duration):
    # Set the AI to act like a calming meditation guide
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a calming meditation teacher. Write a guided meditation script for {duration} minutes "
                f"focused on the goal: {goal}. The tone should be peaceful, slow-paced, and deeply relaxing. "
                "Use soft imagery, pauses, breathing cues, and mindfulness guidance."
            )
        },
        {
            "role": "user",
            "content": f"I want a meditation session for: {goal}"
        }
    ]
 
    try:
        # Request script from Ollama
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return meditation script
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_meditation_script,
    inputs=[
        gr.Radio(["Relaxation", "Focus", "Sleep", "Self-Love", "Anxiety Relief"], label="Meditation Goal"),
        gr.Radio(["5 minutes", "10 minutes", "15 minutes"], label="Duration")
    ],
    outputs="text",
    title="🧘‍♀️ Meditation Script Generator",
    description="Choose your intention and duration—I’ll write you a gentle, guided meditation script to help you breathe and be present."
)
 
# Launch the tool
iface.launch()