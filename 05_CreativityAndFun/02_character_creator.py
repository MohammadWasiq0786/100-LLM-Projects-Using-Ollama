"""
Project 42. Character Creator for Stories

Description:
This AI helps you generate rich, imaginative characters for your stories, games, or roleplay. Just describe the setting or role, and 
it outputs a name, backstory, personality traits, and appearance—great for writers and D&D fans alike.
"""

import ollama
import os
import gradio as gr

 
# Function to generate a character profile
def generate_character(role_or_setting):
    # Prompt AI to act like a creative character designer
    messages = [
        {
            "role": "system",
            "content": (
                "You are a character creation assistant for fantasy and sci-fi writers. "
                "Based on the user's input, generate a detailed character profile. Include: "
                "1. Name, 2. Age, 3. Species/Race, 4. Role/Class, 5. Backstory, 6. Personality, 7. Appearance, 8. Special Abilities (if any). "
                "Make it vivid and creative."
            )
        },
        {
            "role": "user",
            "content": f"Create a character based on: {role_or_setting}"
        }
    ]
 
    try:
        # Call Ollama to generate the character
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return character profile
        return response['message']['content'].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface to input role or world
iface = gr.Interface(
    fn=generate_character,
    inputs=gr.Textbox(label="Character Role or Setting (e.g. elf archer in a steampunk world)"),
    outputs="text",
    title="🧝 Character Creator for Stories",
    description="Describe a role, class, or setting—and I’ll create a vivid character with a full backstory, personality, and powers."
)
 
# Launch the character builder
iface.launch()