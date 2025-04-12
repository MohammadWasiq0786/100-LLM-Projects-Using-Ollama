"""
Project 7. Career Advisor Chatbot

Description:
This chatbot acts like a friendly career coach. 
It offers personalized guidance based on your interests, suggests career paths, reviews resumes, and 
even gives job-hunting tips.Great for students, professionals in transition, or anyone exploring new opportunities.
"""

import ollama
import gradio as gr
import os

# Function to simulate a conversation with a career advisor
def career_advisor(user_input):
    # Define system-level prompt to shape the assistant's personality and expertise
    messages = [
        {
            "role": "system",
            "content": (
                "You are a professional career advisor. Help users explore career options, improve their resumes, "
                "prepare for interviews, and set goals. Ask thoughtful follow-up questions when needed. "
                "Offer practical and motivational advice tailored to their background."
            )
        },
        {
            "role": "user",
            "content": user_input  # The user’s career-related question or concern
        }
    ]
 
    try:
        # Send the message to OpenAI's chat model
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
        
        # Extract and return the reply
        return response['message']['content'].strip()
 
    except Exception as e:
        # Display error message if something goes wrong
        return f"Error: {str(e)}"
 
# Gradio UI setup
iface = gr.Interface(
    fn=career_advisor,                       # Function that generates the assistant response
    inputs="text",                           # Text input field for user
    outputs="text",                          # Text output area for chatbot reply
    title="🎯 Career Advisor Chatbot",       # App title
    description=(
        "Ask for help with your career direction, resume tips, or interview advice. "
        "Examples: 'What jobs can I explore with a psychology degree?', 'Review my resume summary', "
        "or 'How do I prepare for a product manager interview?'"
    )
)
 
# Launch the Gradio web app
iface.launch()