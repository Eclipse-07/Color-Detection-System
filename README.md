🎨 Color Detection and Translation Web App

A Flask-based web application that allows users to upload an image, detect colors by clicking on any pixel, and translate the detected color name into multiple languages. The app also includes user authentication (register/login) and automatic browser launch when started.

🚀 Features

🖼️ Upload an image and view it in the browser

🎯 Detect the exact color name at any clicked pixel

🌍 Translate color names into multiple languages using Google Translate

👤 Secure user authentication (register/login/logout) using MongoDB

💾 Automatic image resizing and optimized upload handling

🌐 Auto-launch in Chrome for convenience

🧠 How It Works

The user registers or logs in.

Upload an image through the web interface.

Click on any pixel in the uploaded image.

The system extracts the pixel’s RGB value using OpenCV.

The app compares the RGB value with a color dataset (colors.csv) to find the closest match.

The color name is translated into the selected language using Google Translate API.

Results are displayed instantly in the browser.

🧩 Tech Stack
Component	Technology
Backend	Flask (Python)
Database	MongoDB
Image Processing	OpenCV, Pillow
Translation	Googletrans
Frontend	HTML, Jinja2 templates
Authentication	Werkzeug (Password Hashing)
🗂️ Project Structure
├── app.py                # Main Flask application
├── colors.csv            # Dataset containing color names and RGB values
├── output.txt            # Sample output for color detection results
├── output.mp3            # Audio output (from gTTS)
├── requirements.txt      # Python dependencies
├── uploads/              # Folder where uploaded images are stored
└── templates/            # HTML templates (login, register, index, etc.)

⚙️ Installation
1. Clone the repository
git clone https://github.com/yourusername/color-detection-translation.git
cd color-detection-translation

2. Install dependencies
pip install -r requirements.txt

3. Set up MongoDB

Make sure MongoDB is running locally:

mongod


Or use your connection string in app.py:

client = MongoClient('your_connection_string')

4. Run the app
python app.py


The app will automatically open in your browser at:

http://127.0.0.1:5000/

