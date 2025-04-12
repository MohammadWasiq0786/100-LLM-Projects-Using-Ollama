"""
Project 1: Basic Chatbot

Description:
A simple command-line or web-based chatbot, and returns a natural-sounding response. 
Perfect for beginners who want to see how an LLM works behind the scenes.
"""

import ollama
import gradio as gr
import os


def chat_with_gpt(prompt):
    response = ollama.chat(
        model="llama3.2:latest",  # You can change the "model_name" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response["message"]["content"]


print("Welcome to the GPT Chatbot! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    reply = chat_with_gpt(user_input)
    print("AI:", reply)
