"""
Project 50. Personality Quiz Generator

Description:
This fun and interactive tool creates personality quizzes based on a topic you choose—like “What kind of pizza are you?” or 
“What’s your creative superpower?” It generates questions, answers, and results that are engaging and share-worthy.
"""

import ollama
import os
import gradio as gr

 
# Function to create a personality quiz
def generate_quiz(topic):
    # Prompt the assistant to act as a quiz creator
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a creative quiz maker. Create a fun and engaging 4-question personality quiz on the topic: '{topic}'. "
                "Each question should have 3-4 answer choices. After the questions, include 3 possible personality result types with descriptions. "
                "Keep the tone fun, playful, and light-hearted."
            )
        },
        {
            "role": "user",
            "content": f"Create a personality quiz on: {topic}"
        }
    ]
 
    try:
        # Call Ollama to create the quiz
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the quiz content
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for the quiz generator
iface = gr.Interface(
    fn=generate_quiz,
    inputs=gr.Textbox(label="Enter a Quiz Topic (e.g. What kind of wizard are you?, Your startup founder style)"),
    outputs="text",
    title="🧬 Personality Quiz Generator",
    description="Type a quiz idea and get a full personality quiz with questions, answers, and results. Great for social content or party fun!"
)
 
# Launch the app
iface.launch()