"""
Project 12. News Article Summarizer

Description:
This tool takes full news articles and returns a clear, objective summary with the key points and facts. 
It’s designed to cut through the fluff and deliver the headline insights. Perfect for journalists, researchers, or 
anyone staying informed without reading full articles.
"""


import ollama
import gradio as gr
import os

# Function that takes a news article and returns a concise summary
def summarize_news(article_text):
    # Prompt the model to act as a professional news summarizer
    messages = [
        {
            "role": "system",
            "content": (
                "You are a news editor. Read full news articles and generate concise summaries highlighting the key facts, events, "
                "and outcomes. Keep it objective and professional, suitable for readers who want the important information only."
            )
        },
        {
            "role": "user",
            "content": f"Summarize the following news article:\n\n{article_text}"
        }
    ]
 
    try:
        
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return the generated summary
        return response['message']['content'].strip()
 
    except Exception as e:
        # Return error message if something goes wrong
        return f"Error: {str(e)}"
 
# Gradio app interface setup
iface = gr.Interface(
    fn=summarize_news,                        # Function to summarize news
    inputs=gr.Textbox(lines=15, placeholder="Paste a news article here..."),
    outputs="text",                           # Output summarized text
    title="📰 News Article Summarizer",       # App title
    description=(
        "Paste a full news article and get a summarized version with key facts. "
        "Ideal for quick understanding of current events without reading the full story."
    )
)
 
# Launch the app in browser
iface.launch()