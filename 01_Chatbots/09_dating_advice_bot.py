"""
Project 9. Dating Advice Bot

Description:
This chatbot offers friendly, non-judgmental dating advice. It can help users craft messages, 
improve online dating profiles, give date ideas, or offer thoughtful responses in awkward situations. 
Think of it as your smooth-talking wingperson with empathy and charm.
"""

import ollama
import gradio as gr
import os

# Define the core function to generate advice
def dating_helper(user_input):
    # This sets the tone and knowledge of the assistant
    messages = [
        {
            "role": "system",
            "content": (
                "You are a charming and supportive dating advisor. "
                "You help people improve their dating profiles, come up with interesting date ideas, "
                "craft thoughtful or flirty messages, and offer guidance in a kind and uplifting tone. "
                "Avoid judgment, stay encouraging, and be both fun and respectful."
            )
        },
        {
            "role": "user",
            "content": user_input  # Whatever the user asks, from advice to message help
        }
    ]
 
    try:
        
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages        # Feed in the full conversation
        )
        
        # Return the assistant's thoughtful response
        return response['message']['content'].strip()
 
    except Exception as e:
        # If something goes wrong (e.g. missing key), show error
        return f"Error: {str(e)}"
 
# Set up Gradio interface for an interactive UI
iface = gr.Interface(
    fn=dating_helper,                         # Function to call on user message
    inputs="text",                            # User types here
    outputs="text",                           # AI's advice shows here
    title="💌 Dating Advice Bot",             # Title of the app
    description=(
        "Need help writing a message? Want first date ideas? Struggling to reply to a text? "
        "Ask for help with any dating scenario and get friendly, respectful advice. "
        "Examples: 'Help me respond to a message on Hinge', 'Ideas for a fun date in New York', or 'Rewrite my dating bio'."
    )
)
 
# Launch the Gradio app
iface.launch()
