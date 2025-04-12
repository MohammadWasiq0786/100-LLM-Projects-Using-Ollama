"""
Project 6. Coding Assistant Chatbot

Description:
This chatbot helps users write, understand, and debug code in various programming languages. 
It can explain syntax, generate functions, suggest improvements, or help with errors. 
Ideal for students, beginners, or developers looking for a quick second opinion.
"""

import ollama
import gradio as gr
import os

# Function to interact with the LLM as a coding assistant
def code_helper(user_input):
    # Define assistant behavior using system role
    messages = [
        {
            "role": "system",
            "content": (
                "You are a skilled programming assistant. Help the user write, debug, or understand code. "
                "Explain your answers in clear, beginner-friendly language and include code examples where appropriate. "
                "Support Python, JavaScript, C++, HTML, and other popular languages."
            )
        },
        {
            "role": "user",
            "content": user_input  # User's programming-related question or request
        }
    ]
 
    try:
        # Query the OpenAI API with the conversation history
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the assistant's message content
        return response['choices'][0]['message']['content'].strip()
 
    except Exception as e:
        # If there's an error (e.g., no API key or network), show it to the user
        return f"Error: {str(e)}"
 
# Define a Gradio interface
iface = gr.Interface(
    fn=code_helper,                      # Function that handles the logic
    inputs="text",                       # Textbox for user queries
    outputs="text",                      # Display the assistant's code response
    title="💻 Coding Assistant Bot",     # App title
    description=(
        "Ask me to write, debug, or explain code. "
        "Try: 'Write a Python function to reverse a string', 'Explain async in JavaScript', or 'Why am I getting a TypeError?'"
    )
)
 
# Launch the chatbot app in your browser
iface.launch()
