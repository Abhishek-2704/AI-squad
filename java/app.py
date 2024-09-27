from flask import Flask, request, jsonify
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for cross-origin requests
CORS(app)

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/recognize', methods=['POST'])
def recognize_text():
    try:
        # Check if an image file is part of the request
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files['image']

        if file.filename == '':
            return jsonify({"error": "No image file selected"}), 400

        # Check if the file has an allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Load the saved image using OpenCV
            image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            
            if image is None:
                return jsonify({"error": "Invalid image file. Could not process the image."}), 400

            # Preprocess the image (resize, normalize, etc.)
            processed_image = cv2.resize(image, (128, 32))  # Resize for model input size
            processed_image = processed_image / 255.0  # Normalize
            
            # Replace with your actual handwritten text recognition model
            # For example:
            # recognized_text = your_model.predict(processed_image)
            
            # Mock result (replace with actual model prediction)
            recognized_text = "माझे नाव गिरीश आहे"  # Example recognized text in Marathi

            return jsonify({"recognizedText": recognized_text})

        else:
            return jsonify({"error": "Invalid file format. Please upload a PNG or JPEG image."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

