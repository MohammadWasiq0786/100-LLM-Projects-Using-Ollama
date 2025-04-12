"""
Project 41. AI Dungeon Master (Text Adventure Game)

Description:
This project turns the AI into a Dungeon Master for a fantasy-style text adventure game. You describe your actions, and 
the AI narrates the unfolding story. Great for roleplaying, storytelling, or just having fun with interactive fiction!
"""

import ollama
import os
import gradio as gr
 
# Initialize story context to remember the previous adventure log
conversation_history = [
    {
        "role": "system",
        "content": (
            "You are a creative and immersive Dungeon Master. Guide the player through a fantasy-style text adventure. "
            "Allow them to explore, battle, and make choices. Always respond in a storytelling tone. End each turn with a question like: "
            "'What would you like to do next?'"
        )
    }
]
 
# Function to interact with the AI Dungeon Master
def dungeon_master(player_action):
    # Add user input to the conversation history
    conversation_history.append({"role": "user", "content": player_action})
 
    try:
        # Call Ollama to generate the next part of the adventure
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=conversation_history
        )
 
        # Get assistant reply and store it
        reply = response["message"]["content"].strip()
        conversation_history.append({"role": "assistant", "content": reply})
 
        # Return the next piece of the story
        return reply
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for the AI Dungeon Master
iface = gr.Interface(
    fn=dungeon_master,
    inputs=gr.Textbox(lines=2, placeholder="e.g. I open the treasure chest cautiously..."),
    outputs="text",
    title="🎮 AI Dungeon Master",
    description="Start a fantasy text adventure! Type your actions and let the AI guide you through a magical world full of choices, danger, and loot."
)
 
# Launch the game
iface.launch()