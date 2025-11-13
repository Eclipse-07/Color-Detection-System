from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for, session, flash
import requests
import cv2
import pandas as pd
from googletrans import Translator
import os
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from PIL import Image
import webbrowser
from threading import Timer


app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
app.config['UPLOAD_FOLDER'] = 'uploads/'


client = MongoClient('mongodb://localhost:27017/')
db = client.Color_detect
users_collection = db.users


# Reading the CSV file with pandas and naming columns
index = ["color_id", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=0)  # Adjusted to skip the header row
translator = Translator()


def getColorName(R, G, B):
    minimum = 10000
    cname = "Unknown"
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    return redirect(url_for('login'))


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
       
        hashed_password = generate_password_hash(password)
       
        # Check if the user already exists
        if users_collection.find_one({'email': email}):
            flash('Email address already exists.', 'danger')
            return redirect(url_for('login'))


        users_collection.insert_one({'username': username, 'email': email, 'password': hashed_password})
        flash('Registration successful, please log in.', 'success')
        return redirect(url_for('login'))


   


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
       
        user = users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
   
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files.get('file')
    if file is None:
        return 'No file was sent', 400
   
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
   
    with Image.open(filepath) as img:
        img.thumbnail((800, 800))  # Resize to max 800x800
        img.save(filepath)


    return render_template('uploads.html', filename=file.filename)


def translate_text(text, target_language):
    url = "http://localhost:5000/translate"
    data = {
        "q": text,
        "source": "en",  # Assuming the source language is English
        "target": target_language
    }
    response = requests.post(url, data=data)
    translated_text = response.json().get('translatedText', 'Translation failed')
    return translated_text


@app.route('/get_color_at_pixel', methods=['POST'])
def get_color_at_pixel():
    filename = request.form['filename']
    x = int(request.form['x'])
    y = int(request.form['y'])
    language = request.form['language']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img = cv2.imread(filepath)
    if img is not None and 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
        b, g, r = img[y, x]  # OpenCV uses BGR format
        color_name = getColorName(r, g, b)
        translated_color_name = translator.translate(color_name, dest=language).text
        return jsonify({'color_name': color_name, 'translated_color_name': translated_color_name})
    else:
        return jsonify({'color_name': 'Unknown', 'translated_color_name': 'Unknown'})
@app.route('/uploads/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
def open_browser():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open_new('http://127.0.0.1:5000/')
if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)


