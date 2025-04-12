"""
Project 5. Study Buddy Bot

Description:
This bot acts as a friendly study partner. It can quiz you on topics, explain concepts in simple terms, or 
help summarize your notes. It’s great for students who want a quick, interactive way to review material or 
learn new topics on the fly.
"""

import ollama
import gradio as gr
import os

# Function to handle conversation with the study buddy bot
def study_buddy(user_input):
    # Define how the bot should behave using the system prompt
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful and friendly study buddy. "
                "You help users understand difficult topics, quiz them with questions, "
                "or summarize content they provide. Always respond clearly and positively."
            )
        },
        {
            "role": "user",
            "content": user_input  # Input from the student
        }
    ]
    
    try:
        # Make a request to the OpenAI Chat API
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages       # Provide conversation context
        )
        
        # Return the assistant's reply
        return response["message"]["content"].strip()
    
    except Exception as e:
        # Handle any API or request errors
        return f"Error: {str(e)}"
 
# Gradio interface for the study buddy bot
iface = gr.Interface(
    fn=study_buddy,                    # Function to handle responses
    inputs="text",                     # Text input box
    outputs="text",                    # Text output box
    title="📚 Study Buddy Bot",        # App title
    description=(
        "Ask me to explain a topic, quiz you, or summarize something you're learning. "
        "Examples: 'Explain Newton's laws simply', 'Quiz me on world history', 'Summarize my notes on photosynthesis'."
    )
)
 
# Launch the Gradio app in the browser
iface.launch()