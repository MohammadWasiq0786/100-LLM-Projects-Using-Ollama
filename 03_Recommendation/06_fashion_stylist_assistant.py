"""
Project 26. Fashion Stylist Assistant

Description:
This AI stylist helps users pick outfits, coordinate colors, or dress for specific occasions. 
Whether you’re planning a first date look, need a business casual vibe, or want to elevate your streetwear, 
this fashion-savvy bot has your back (and your closet).
"""

import ollama
import os
import gradio as gr
 
 
# Function to offer styling suggestions
def style_advisor(user_input):
    # Set the assistant to behave like a fashion consultant
    messages = [
        {
            "role": "system",
            "content": (
                "You are a personal fashion stylist. Help users choose outfits based on the occasion, current trends, season, body type, "
                "color preferences, or existing wardrobe pieces. Be creative, encouraging, and style-forward. Offer 2-3 suggestions and include tips!"
            )
        },
        {
            "role": "user",
            "content": f"I need outfit help: {user_input}"
        }
    ]
 
    try:
        # Make the Ollama call
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return fashion advice
        return response['message']['content'].strip()
 
    except Exception as e:
        # Show error message if something goes wrong
        return f"Error: {str(e)}"
 
# Gradio interface for the fashion stylist bot
iface = gr.Interface(
    fn=style_advisor,                                # Function to generate outfit suggestions
    inputs=gr.Textbox(lines=2, placeholder="e.g. I have a black blazer and jeans. Going on a casual dinner date."),
    outputs="text",                                  # Output fashion tips
    title="👗 AI Fashion Stylist Assistant",          # App title
    description=(
        "Need outfit ideas or fashion tips? Tell me the occasion, season, or what’s in your closet and I’ll give you stylish suggestions. "
        "Try: 'What should I wear to a summer wedding?' or 'Style my white sneakers and leather jacket'."
    )
)
 
# Launch the stylist chatbot
iface.launch()