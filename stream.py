from flask import Flask, send_from_directory

app = Flask(__name__)

# 🌍 Serve OPML and other files from "stationlist" folder
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('stationlist', filename)

# 🚀 Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
