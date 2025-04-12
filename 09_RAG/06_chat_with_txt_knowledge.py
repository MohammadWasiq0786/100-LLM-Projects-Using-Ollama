"""
Project 86. Personal Knowledge Q&A (using a .txt file)

Description:
This assistant lets you upload a plain .txt file full of your notes, thoughts, or custom knowledge—and then ask 
natural language questions about it. It’s like chatting with your second brain.
"""

import os
import ollama
import gradio as gr
 
 
# Function to chat with .txt file
def chat_with_txt(file, question):
    try:
        # Read and decode the uploaded .txt file
        knowledge = file.read().decode("utf-8")
 
        # Construct prompt using the file content
        prompt = (
            f"You are a helpful assistant. Use the following personal notes to answer the user's question accurately and clearly.\n\n"
            f"Personal Knowledge:\n{knowledge[:4000]}\n\n"  # Truncate if needed
            f"Question: {question}\nAnswer:"
        )
 
        # Get answer from OpenAI
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=[{"role": "user", "content": prompt}]
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error reading file: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=chat_with_txt,
    inputs=[
        gr.File(label="Upload .txt Knowledge File", file_types=[".txt"]),
        gr.Textbox(label="Ask a Question About Your Notes")
    ],
    outputs="text",
    title="📚 Chat with Personal Knowledge (.txt)",
    description="Upload a text file of notes or info and ask questions—great for your custom knowledge base!"
)
 
# Launch the app
iface.launch()
