"""
Project 54. Flashcard Generator

Description:
This smart assistant creates flashcards from topics you input—breaking down complex subjects into Q&A format. 
Ideal for spaced repetition, exam prep, or bite-sized learning across any subject: science, history, language, or coding.
"""

import ollama
import os
import gradio as gr
 
 
# Function to generate flashcards
def generate_flashcards(topic, number_of_cards):
    # Prompt AI to act like a flashcard creator
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a flashcard generator. Create {number_of_cards} flashcards (question-answer format) "
                f"on the topic: '{topic}'. Use simple and clear language. Each flashcard should have a short question and a concise answer. "
                "Return them as a numbered list."
            )
        },
        {
            "role": "user",
            "content": f"Topic: {topic}"
        }
    ]
 
    try:
        # Call Ollama to get flashcards
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the list of flashcards
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface for generating flashcards
iface = gr.Interface(
    fn=generate_flashcards,
    inputs=[
        gr.Textbox(label="Topic (e.g. Photosynthesis, Python Loops, World War II)"),
        gr.Slider(1, 10, step=1, label="Number of Flashcards")
    ],
    outputs="text",
    title="🗂️ Flashcard Generator",
    description="Enter a topic and number of cards, and I’ll generate study flashcards in Q&A format—great for revision or memorization."
)
 
# Launch the flashcard builder
iface.launch()