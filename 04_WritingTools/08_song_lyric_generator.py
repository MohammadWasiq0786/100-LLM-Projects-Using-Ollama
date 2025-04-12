"""
Project 38. Song Lyric Generator

Description:
This AI lyricist writes original song lyrics based on your theme, genre, and emotion. Whether it’s pop, rap, country, or 
R&B—you'll get lyrics with flow, rhyme, and feeling. Perfect for musicians, content creators, or just for fun!
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate song lyrics
def generate_lyrics(theme, genre):
    # Prompt the assistant to become a creative lyricist
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a talented songwriter. Based on the user's theme and chosen music genre, write original song lyrics. "
                "Use rhyming patterns, repetition, and emotional tone that fits the genre. Include verses, a chorus, and optionally a bridge."
            )
        },
        {
            "role": "user",
            "content": f"Theme: {theme}\nGenre: {genre}"
        }
    ]
 
    try:
        # Ollama for lyric generation
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the song lyrics
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for creating song lyrics
iface = gr.Interface(
    fn=generate_lyrics,                              # Core lyric generator
    inputs=[
        gr.Textbox(label="Song Theme (e.g. heartbreak, summer love, chasing dreams)"),
        gr.Radio(["pop", "rap", "country", "rock", "r&b", "ballad"], label="Genre")
    ],
    outputs="text",
    title="🎤 Song Lyric Generator",
    description="Enter a theme and select a genre—I'll write original lyrics with structure and style. Great for inspiration, writing, or jamming!"
)
 
# Launch the lyric generator
iface.launch()