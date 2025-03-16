import os
from flask import Flask, send_from_directory

# Create the Flask app
app = Flask(__name__)

# Ensure "stationlist" folder exists
FOLDER_NAME = "stationlist"
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

@app.route('/<path:filename>')
def serve_file(filename):
    """Serve files from the 'stationlist' folder."""
    file_path = os.path.join(FOLDER_NAME, filename)

    # Check if the requested file exists
    if not os.path.exists(file_path):
        return f"File {filename} not found in {FOLDER_NAME}", 404

    return send_from_directory(FOLDER_NAME, filename)

if __name__ == "__main__":
    print(f"📂 Available files in '{FOLDER_NAME}':", os.listdir(FOLDER_NAME))
    print("🚀 Flask server starting...")
    app.run(host="0.0.0.0", port=8000, debug=True)
