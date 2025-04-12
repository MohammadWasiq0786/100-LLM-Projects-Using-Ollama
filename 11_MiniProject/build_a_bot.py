"""
Project 101. Build-a-Bot: A fully customizable chatbot

Build-a-Bot: A fully customizable chatbot with name, style, tone, role, and memory toggle

Description:
This is your ultimate DIY chatbot tool. You can define the bot’s name, tone, style, role, and even toggle memory behavior. 
It’s perfect for creating anything from a friendly assistant to a strict coach or playful pirate.
"""

import os
import ollama
import gradio as gr
 

# Function to run the customizable chatbot
def build_a_bot(name, tone, role, message, memory_mode):
    try:
        # Define the persona and style for the system prompt
        system_prompt = (
            f"You are {name}, a chatbot with the personality of a {tone} {role}. "
            f"Respond with that voice and be consistent in tone and mannerisms."
        )
 
        messages = [{"role": "system", "content": system_prompt}]
 
        # If memory mode is "off", forget past messages
        if memory_mode == "Off":
            messages.append({"role": "user", "content": message})
        else:
            # Use memory mode to track conversation history across turns (for real-world use, this would persist)
            if 'chat_history' not in gr.get_state():
                gr.set_state({'chat_history': []})
            state = gr.get_state()
            state['chat_history'].append({"role": "user", "content": message})
            messages += state['chat_history']
 
        # Get AI response
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        reply = response["message"]["content"].strip()
 
        # Store assistant response in memory if memory is on
        if memory_mode == "On":
            state['chat_history'].append({"role": "assistant", "content": reply})
 
        return reply
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=build_a_bot,
    inputs=[
        gr.Textbox(label="Bot Name", placeholder="e.g., Luna, Captain Code, Mentor Max"),
        gr.Dropdown(["Friendly", "Funny", "Serious", "Strict", "Playful", "Sarcastic", "Motivational"], label="Tone"),
        gr.Textbox(label="Bot Role", placeholder="e.g., Life Coach, Writing Tutor, Space Captain"),
        gr.Textbox(label="Your Message", placeholder="Say something to your bot"),
        gr.Radio(["On", "Off"], label="Memory Mode")
    ],
    outputs="text",
    title="🤖 Build-a-Bot: Customizable Chat Agent",
    description="Craft your own AI bot by setting its name, tone, role, and memory behavior. It will respond in character!"
)
 
# Launch the ultimate chatbot builder
iface.launch()