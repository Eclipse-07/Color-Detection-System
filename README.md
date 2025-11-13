# 🎨 HueVerse — Intelligent Color Exploration Platform

HueVerse is an innovative web application that redefines how we interact with colors by integrating **precise color detection**, **optical character recognition (OCR)**, and **multilingual text-to-speech (TTS)** features.  

Built for **artists, designers, educators, and visually impaired users**, HueVerse combines technology and accessibility to make color exploration more interactive, inclusive, and creative.

---

## 🌈 Key Features

### 🎯 Color Identification
- Upload images and detect colors with pixel-level precision.  
- Analyze hue, saturation, and brightness.  
- Select specific regions for focused analysis.

### 🧠 Text Extraction (OCR)
- Extract text from images using **Tesseract OCR**.  
- Convert extracted text into editable text or audible speech.

### 🗣️ Multilingual Text-to-Speech
- Hear color names and text spoken aloud via **Google Text-to-Speech (gTTS)**.  
- Supports multiple languages for cultural and linguistic exploration.

### ♿ Accessibility
- Designed for visually impaired users with detailed auditory color descriptions.  
- Promotes independence and inclusivity.

### 🖼️ Image Editing
- Crop, rotate, or adjust image brightness in real-time.  
- Preview and download edited images instantly.

---

## ⚙️ Technology Stack

| Category | Technology |
|-----------|-------------|
| **Frontend** | HTML, CSS, JavaScript, AJAX |
| **Backend** | Flask (Python) |
| **Database** | MongoDB |
| **Libraries & APIs** | OpenCV, gTTS, Pandas, argparse, translate |
| **IDE** | VSCode, Jupyter Notebook, Spyder |

---

## 💻 Installation & Setup

### 🔧 Prerequisites
- Python 3.8 or higher  
- MongoDB  
- pip (Python package manager)

### 🌀 Clone the Repository
```bash
git clone https://github.com/Eclipse-07/Color-Detection-System.git
cd Color-Detection-System
````

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the Application

```bash
python app.py
```

Then open your browser and go to:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🧩 Project Structure

```
Color-Detection-System/
│
├── app.py                # Main Flask application
├── colors.csv            # Color dataset
├── output.mp3            # Sample audio output (TTS)
├── output.txt            # OCR text output
├── requirements.txt      # Dependencies list
│
├── static/               # CSS, JS, and assets
├── templates/            # HTML templates
├── uploads/              # Uploaded images
└── .vscode/              # VSCode configuration
```

---

## 🎯 Objectives

* Deliver **unparalleled accuracy** in color detection.
* Enhance **accessibility** through speech output for visually impaired users.
* Promote **cultural and linguistic diversity** with multilingual support.
* Provide a **user-friendly interface** for all experience levels.
* Foster **innovation and creativity** across artistic and educational domains.

---

## 👩‍💻 Author

**Developed by:** [Eclipse-07](https://github.com/Eclipse-07)
**Project:** HueVerse — Color Detection System
**Year:** 2025

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---


Would you like me to add **badges** (Python version, Flask version, license, etc.) and a **project banner image** section at the top to make it look even more professional for GitHub?
```
