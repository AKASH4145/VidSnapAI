# VidsnapAI – AI Reel Generator 

##  Overview
VidsnapAI is a Python-based AI web application that generates reel-style audio content using
AI-powered voice synthesis from the ElevenLabs API. It allows users to upload media (text, images, or video-related inputs) and process them into generated outputs such as text-to-speech audio, processed media, or AI-assisted transformations using FFmpeg and Python automation.

The project focuses on real-world AI API integration, backend development, and automation
for content creation workflows.The project is designed with a clean Flask architecture and proper Git hygiene, making it scalable and production-ready.

---

---

##  Features
- AI voice generation using ElevenLabs (Text-to-Speech)
- Flask-based backend application
- Text-to-MP3 audio generation
- FFmpeg-based processing for reel creation
- User input handling and file storage
- Modular project structure

---

---

##  Tech Stack
- Python
- Flask
- ElevenLabs API
- FFmpeg
- HTML / CSS (templates & static files)

---

---

## Project Structure
```text
VidsnapAI/
├── main.py                 # Flask app entry point
├── config.py               # App configuration
├── generate_processes.py   # Media / FFmpeg processing
├── text_to_mp3.py          # Text-to-speech logic
├── test.py                 # Testing / experimentation
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   └── gallery.html
├── static/                 # Static assets
│   └── css/
│       ├── style.css
│       ├── create.css
│       └── gallery.css
├── user_uploads/           # Runtime user uploads (git-ignored)
│   └── .gitkeep
├── .gitignore
└── README.md
```
---

---

## Setup & Run

git clone https://github.com/AKASH4145/VidSnapAI.git >> 
cd VidSnapAI >> 
pip install -r requirements.txt >> 
python main.py


---

##  User Uploads Handling

-All user uploads are stored inside user_uploads/ 
-Actual uploaded files are not tracked by Git
-gitkeep is used to keep the folder in the repository

---

## Version Control

-The repository tracks only source code and required assets.  
-Generated files, caches, and user uploads are excluded using `.gitignore`.

---

## Future Improvements

-Authentication system
-Database integration
-Cloud storage for uploads
-AI-based video summarization

---

## Author

Akash GS |
Mechanical Engineering student exploring 
AI, computer vision, and applied Python development 
