"""
Project 87. One-Page Handbook Q&A

Description:
This app allows users to upload a short one-page handbook (in .txt, .md, or .pdf format) and ask questions about it. 
Whether it’s a cheat sheet, internal guide, or FAQ, the assistant reads and responds based on the content.
"""

import os
import ollama
import gradio as gr
import PyPDF2
 
# Extract text from file (.txt, .md, .pdf supported)
def extract_text(file):
    filename = file.name
    if filename.endswith(".txt") or filename.endswith(".md"):
        return file.read().decode("utf-8")
    elif filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() for page in pdf_reader.pages)
    else:
        return "Unsupported file type."
 
# Generate answer using handbook content
def chat_with_handbook(file, question):
    try:
        handbook_text = extract_text(file)
 
        prompt = (
            f"You are an expert assistant who answers questions based only on the following handbook content.\n\n"
            f"Handbook:\n{handbook_text[:4000]}\n\n"  # limit input size
            f"Question: {question}\nAnswer:"
        )
 
        # Generate response
        response = ollama.chat(
            model="llama3.2:latest",  # You can change the "model_name" if needed
            messages=[{"role": "user", "content": prompt}]
        )
 
        return response["message"]["content"].strip()
 
    except Exception as e:
        return f"Error: {str(e)}"
 
# Gradio interface
iface = gr.Interface(
    fn=chat_with_handbook,
    inputs=[
        gr.File(label="Upload Handbook (.txt, .md, or .pdf)", file_types=[".txt", ".md", ".pdf"]),
        gr.Textbox(label="Ask a Question")
    ],
    outputs="text",
    title="📘 One-Page Handbook Q&A",
    description="Upload a short guide or handbook and chat with it. Great for cheat sheets, internal SOPs, or how-to docs."
)
 
# Launch app
iface.launch()