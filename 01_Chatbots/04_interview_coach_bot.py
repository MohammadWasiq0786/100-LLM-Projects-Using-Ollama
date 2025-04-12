"""
Project 4. Interview Coach Chatbot

Description:
A chatbot that simulates an interview coach. 
It helps users practice answering behavioral and technical questions, gives feedback, and suggests improvements.
Ideal for job seekers looking to sharpen their answers in a conversational setting.
"""

import ollama
import gradio as gr
import os


# Function to interact with Ollama API
def interview_coach(user_input):
    # Define the system message that sets the tone and behavior of the AI
    messages = [
        {
            "role": "system",
            "content": (
                "You are an experienced interview coach helping candidates prepare for job interviews. "
                "Ask common interview questions (behavioral or technical), provide feedback on answers, "
                "suggest improvements, and encourage the user. Be supportive but honest."
            )
        },
        {
            "role": "user",
            "content": user_input  # This is the input from the user (job seeker)
        }
    ]
    
    try:
        # Generate the response from OpenAI's GPT model
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages       # Provide the conversation messages
        )
        
        # Extract and return the assistant's reply
        return response["message"]["content"].strip()
    
    except Exception as e:
        # Return error message in case of an issue
        return f"Error: {str(e)}"
 
# Create a Gradio UI interface
iface = gr.Interface(
    fn=interview_coach,              # Function to call on user input
    inputs="text",                   # User input: plain text
    outputs="text",                  # Bot response: plain text
    title="🎤 Interview Coach Bot",  # Title of the web app
    description=(
        "Practice job interviews with an AI coach. Type your answer to a sample question, "
        "or ask for interview tips or mock questions. For example: 'Ask me a behavioral question.'"
    )
)
 
# Launch the Gradio web app
iface.launch()