"""
Project 58. History Quiz Generator
Description:
This project creates engaging multiple-choice history quizzes on any era, civilization, war, or event. 
Great for students, teachers, trivia fans, or just brushing up on your knowledge of the past.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate history quiz questions
def generate_history_quiz(topic, difficulty):
    # Prompt to make a history teacher AI
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a history quiz creator. Generate 3 multiple-choice quiz questions on the topic: '{topic}' "
                f"at a {difficulty} level. Each question should have 4 options (A–D), and clearly indicate the correct answer "
                "with a brief explanation at the end."
            )
        },
        {
            "role": "user",
            "content": "Please generate the quiz."
        }
    ]
 
    try:
        # Call Ollama for quiz generation
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return quiz content
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for quiz generation
iface = gr.Interface(
    fn=generate_history_quiz,
    inputs=[
        gr.Textbox(label="Enter History Topic (e.g. World War II, Ancient Egypt, Civil Rights Movement)"),
        gr.Radio(["beginner", "intermediate", "advanced"], label="Select Difficulty Level")
    ],
    outputs="text",
    title="🏺 History Quiz Generator",
    description="Enter a history topic and get a multiple-choice quiz with answers and brief explanations. Perfect for fun learning and classroom practice!"
)
 
# Launch the quiz generator
iface.launch()