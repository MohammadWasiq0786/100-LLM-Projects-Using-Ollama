"""
Project 13. YouTube Transcript Summarizer

Description:
This tool summarizes transcripts from YouTube videos—great for turning long educational content, podcasts, or 
lectures into quick takeaways. Users can paste transcripts directly (from auto-generated captions or tools like 
YouTube Transcript) and get a concise summary.

YouTube Transcript: https://youtubetranscript.com/
"""

import ollama
import gradio as gr
import os



# Define function to summarize YouTube transcripts
def summarize_transcript(transcript_text):
    # Set up system prompt to guide the assistant
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert summarizer. Your task is to take long video transcripts (from YouTube lectures, interviews, or podcasts) "
                "and summarize them into key insights and bullet points. Be concise, clear, and educational."
            )
        },
        {
            "role": "user",
            "content": f"Please summarize this transcript:\n\n{transcript_text}"
        }
    ]
 
    try:
        
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=messages
        )
 
        # Return summarized content
        return response["message"]["content"].strip()
 
    except Exception as e:
        # Return any errors encountered
        return f"Error: {str(e)}"
 
# Create Gradio interface for transcript summarization
iface = gr.Interface(
    fn=summarize_transcript,                       # Function to summarize transcript
    inputs=gr.Textbox(lines=15, placeholder="Paste YouTube transcript here..."),
    outputs="text",                                # Display summarized output
    title="🎥 YouTube Transcript Summarizer",      # App title
    description=(
        "Paste the full transcript from a YouTube video to get a clean summary. "
        "Great for lectures, interviews, podcasts, or long videos. Example: use '...' from auto-captions or https://youtubetranscript.com/"
    )
)
 
# Launch the app
iface.launch()