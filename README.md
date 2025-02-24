📖 Audiobook Generator

🎙️ Convert PDFs to Audiobooks with AI

This Windows application converts any PDF document into an audiobook using AI-based speech synthesis. It extracts text from the PDF and generates a fluent, human-like narration.

🛠️ Features

✅ Load Any PDF – Select a PDF file to extract text.✅ AI-Powered Narration – Converts text into a fluent audiobook.✅ Natural Speech Synthesis – Uses pyttsx3 for lifelike narration.✅ User-Friendly UI – Simple and visually appealing interface.✅ Save to MP3 – Audio is saved to the output folder.✅ Windows Compatible – Works seamlessly on Windows.

📂 Folder Structure

📁 audiobook-app
│── 📁 output               # Folder where generated audiobooks are saved
│── 📁 src                  # Application source code
│    ├── main.py            # Entry point of the application
│    ├── pdf_to_text.py     # Extracts text from PDF
│── 📁 ui                   # UI components
│    ├── app.py             # Main UI of the application
│── 📄 requirements.txt      # Required dependencies
│── 📄 README.md            # Documentation

🔧 Installation

1️⃣ Install Python (Windows)

Make sure you have Python 3.8+ installed. If not, download it here.

2️⃣ Clone or Download the Repository

cd C:\Vinit\Devpost
git clone https://github.com/your-repo/audiobook-app.git
cd audiobook-app

3️⃣ Create a Virtual Environment (Recommended)

python -m venv audiobook-app
cd audiobook-app
Scripts\activate  # For Windows

🔹 4. Setup Models : Since GitHub does not support files larger than 100MB, you need to manually download and place the model in the correct folder.
📂 Create a models folder: mkdir models
⬇️ Download Model from Qualcomm AI Hub : Download the Whisper Base English Model from the link below and place it inside the models folder:https://aihub.qualcomm.com/compute/models/whisper_base_en?domain=Audio

4️⃣ Install Dependencies

pip install -r requirements.txt

🚀 How to Run the Application

1️⃣ Open Terminal in the Project Folder

cd C:\Vinit\Devpost\audiobook-app

2️⃣ Run the Application

python src/main.py

📦 Required Packages

Install all dependencies using the requirements.txt, or manually install:

pip install pyttsx3 PyMuPDF tk

pyttsx3 → AI-powered speech synthesis (text-to-speech)

PyMuPDF (fitz) → Extracts text from PDFs

tkinter → Creates a user-friendly interface

🎯 How It Works

1️⃣ Select a PDF 📂 → Extracts text.2️⃣ Text Appears in the App 📖 → Readable & scrollable.3️⃣ Click "Convert to Audiobook" 🎧 → AI generates fluent narration.4️⃣ MP3 Saved in output/ Folder 🎵 → Enjoy your audiobook!

📌 Notes

The app is designed for Windows (Linux & Mac may need modifications).

If voice sounds robotic, adjust engine.setProperty("rate", 180) in app.py.

You can change the voice gender using engine.setProperty("voice", voices[1].id).

🛠️ Troubleshooting

❌ ModuleNotFoundError: No module named 'fitz'✅ Run: pip install PyMuPDF

❌ No text extracted from PDF✅ Ensure the PDF contains selectable text (not images).

❌ App not opening?✅ Try running with administrator privileges.
