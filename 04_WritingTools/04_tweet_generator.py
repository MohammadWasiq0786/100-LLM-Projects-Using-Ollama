"""
Project 34. Tweet Generator
Description:
This tool helps generate catchy, concise, and engaging tweets based on your topic, audience, and style. Whether you're aiming to be witty, 
insightful, or informative—it crafts content that fits the 280-character Twitter limit.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate a tweet
def generate_tweet(topic, tone):
    # System message sets assistant behavior
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a social media expert. Write a tweet on the topic provided in a {tone} tone. "
                "Make sure it is short, punchy, engaging, and within Twitter’s 280 character limit."
            )
        },
        {
            "role": "user",
            "content": f"Topic: {topic}"
        }
    ]
 
    try:
        # Ollama call
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return tweet suggestion
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=generate_tweet,                                    # Core tweet generation function
    inputs=[
        gr.Textbox(label="Tweet Topic (e.g. AI for Beginners)"),
        gr.Radio(["funny", "educational", "inspiring", "controversial"], label="Tone")
    ],
    outputs="text",                                       # Display tweet
    title="🐦 Tweet Generator",
    description="Enter a topic and tone, and I’ll create a scroll-stopping tweet under 280 characters. Great for building your Twitter presence!"
)
 
# Launch the Twitter content creator
iface.launch()