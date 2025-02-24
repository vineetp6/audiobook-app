import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import fitz  # PyMuPDF for PDF text extraction
import pyttsx3

# Define output directory
OUTPUT_DIR = r"C:\Vinit\Devpost\audiobook-app\output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Global variable for extracted text
current_text = ""

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    global current_text
    current_text = ""
    
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            current_text += page.get_text("text") + "\n\n"
        
        text_display.delete("1.0", tk.END)  # Clear previous text
        text_display.insert(tk.END, current_text)  # Insert extracted text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text: {e}")

# Function to open a file dialog and select a PDF
def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        extract_text_from_pdf(file_path)

# Function to convert extracted text to an audio file
def convert_to_audio():
    if current_text.strip():
        audio_path = os.path.join(OUTPUT_DIR, "audiobook.mp3")
        engine = pyttsx3.init()

        # Adjust speech properties
        engine.setProperty("rate", 180)  # Increase speed for better fluency
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)  # Select female voice (change index if needed)

        # Process text into fluent speech
        sentences = current_text.replace("\n", " ").split(". ")  # Sentence-level splitting
        refined_text = ". ".join(sentences)  # Maintain structure

        engine.save_to_file(refined_text, audio_path)
        engine.runAndWait()

        messagebox.showinfo("Success", f"Audiobook saved at:\n{audio_path}")
    else:
        messagebox.showwarning("Warning", "No text to convert!")

# Create the main application window
app = tk.Tk()
app.title("Audiobook Generator")
app.geometry("600x500")
app.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(app, text="📖 PDF to Audiobook Converter 🎙️", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Button to Open PDF
open_pdf_button = tk.Button(app, text="📂 Open PDF", font=("Arial", 12), command=open_pdf, bg="#3498db", fg="white")
open_pdf_button.pack(pady=5)

# Scrollable Text Display
text_display = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=15, font=("Arial", 12))
text_display.pack(pady=10)

# Convert to Audio Button
convert_button = tk.Button(app, text="🎧 Convert to Audiobook", font=("Arial", 12), command=convert_to_audio, bg="#2ecc71", fg="white")
convert_button.pack(pady=5)

# Run the application
app.mainloop()
