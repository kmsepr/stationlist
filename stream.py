import os
from flask import Flask, jsonify, send_from_directory

# Create the Flask app
app = Flask(__name__)

# Define file paths
STATIONLIST_FILE = "stationlist.txt"
PODCASTS_FILE = "podcasts.opml"

def read_file(filepath):
    """Read a file and return its content as a list of lines."""
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.readlines()
    return []

@app.route('/stations')
def get_stations():
    """Return the contents of stationlist.txt as JSON."""
    stations = read_file(STATIONLIST_FILE)
    return jsonify({"stations": [line.strip() for line in stations if line.strip()]})

@app.route('/podcasts')
def get_podcasts():
    """Return the contents of podcasts.opml as JSON."""
    podcasts = read_file(PODCASTS_FILE)
    return jsonify({"podcasts": [line.strip() for line in podcasts if line.strip()]})

@app.route('/<path:filename>')
def serve_file(filename):
    """Serve static files from the repository directory."""
    if not os.path.exists(filename):
        return f"File {filename} not found", 404
    return send_from_directory(".", filename)

if __name__ == "__main__":
    print("📂 Available files:", os.listdir("."))
    print("🚀 Flask server starting on http://0.0.0.0:8000")
    app.run(host="0.0.0.0", port=8000, debug=True)