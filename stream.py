import os
from flask import Flask, send_from_directory, abort

# Flask app initialization
app = Flask(__name__)

# Define folder name
FOLDER_NAME = "stationlist"

# Ensure the folder exists
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

@app.route('/<path:filename>')
def serve_file(filename):
    """
    Serve files from the 'stationlist' folder.
    Returns 404 if the file does not exist.
    """
    file_path = os.path.join(FOLDER_NAME, filename)

    if not os.path.exists(file_path):
        return abort(404, description=f"File '{filename}' not found in '{FOLDER_NAME}'")

    return send_from_directory(FOLDER_NAME, filename)

if __name__ == "__main__":
    available_files = os.listdir(FOLDER_NAME)
    print(f"📂 Available files in '{FOLDER_NAME}': {available_files if available_files else 'No files found'}")
    print("🚀 Flask server starting at http://0.0.0.0:8000/")
    
    app.run(host="0.0.0.0", port=8000, debug=True)