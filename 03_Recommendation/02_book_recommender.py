"""
Project 22. Book Recommender

Description:
This chatbot suggests books tailored to your interests, mood, or favorite authors. 
Whether you're craving thrillers, looking for feel-good reads, or exploring self-help, 
this AI-powered recommender curates a list just for you—with mini summaries to boot.
"""

import ollama
import os
import gradio as gr


# Function to provide personalized book suggestions
def recommend_books(user_input):
    # System prompt sets up the AI as a book-loving assistant
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful and passionate book recommender. Based on a user's interests, mood, or favorite genres/authors, "
                "suggest a few great books. For each book, give the title, author, and a short 1-2 sentence summary. "
                "Be warm and encouraging in your tone."
            )
        },
        {
            "role": "user",
            "content": f"I'm looking for: {user_input}"
        }
    ]
 
    try:
        # Send the request to Ollama's API
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the curated book list
        return response['message']['content'].strip()
 
    except Exception as e:
        # Display error if something goes wrong
        return f"Error: {str(e)}"
 
# Gradio interface for book suggestions
iface = gr.Interface(
    fn=recommend_books,                            # Core function
    inputs=gr.Textbox(lines=2, placeholder="e.g. I like mystery novels with plot twists or something like Harry Potter."),
    outputs="text",                                # Display output
    title="📚 Book Recommender Bot",               # App title
    description=(
        "Tell me what kind of books you're in the mood for and I'll recommend a few with short summaries. "
        "Try things like: 'Books like The Alchemist', 'Dark fantasy adventures', or 'Short motivational reads'."
    )
)
 
# Launch the web app
iface.launch()