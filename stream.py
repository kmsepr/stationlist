import subprocess
import time
from flask import Flask, Response, send_from_directory

app = Flask(__name__)

# 🎡 List of radio stations
RADIO_STATIONS = {
    "rurock": "https://stream02.pcradio.ru/Rock-hi",
    "rubat_ataq": "http://stream.zeno.fm/5tpfc8d7xqruv",
    "shahul_radio": "https://stream-150.zeno.fm/cynbm5ngx38uv?zs=Ktca5StNRWm-sdIR7GloVg",
    "eram_fm": "http://icecast2.edisimo.com:8000/eramfm.mp3",
    "abc_islam": "http://s10.voscast.com:9276/stream",
}

# 🔄 Streaming function with error handling
def generate_stream(url):
    process = None
    while True:
        if process:
            process.kill()  # Stop the old FFmpeg instance before restarting
        
        process = subprocess.Popen(
            [
                "ffmpeg", "-reconnect", "1", "-reconnect_streamed", "1", "-reconnect_delay_max", "10", "-i", url, "-vn", "-ac", "1", "-acodec", "libmp3lame", "-b:a", "40k", "-ar", "32000", "-buffer_size", "2048k", "-f", "mp3", "-"
            ],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=102400
        )

        print(f"🎵 Streaming from: {url} (Mono, 40kbps)")

        try:
            for chunk in iter(lambda: process.stdout.read(102400), b""):
                yield chunk
        except GeneratorExit:
            process.kill()
            break
        except Exception as e:
            print(f"⚠️ Stream error: {e}")

        print("🔄 FFmpeg stopped, restarting stream...")
        time.sleep(5)  # Wait before restarting

# 🌍 API to serve OPML file
@app.route('/podcasts.opml')
def serve_opml():
    return send_from_directory('stationlist', 'podcasts.opml', mimetype='text/xml')

# 🌍 API to stream selected station
@app.route("/<station_name>")
def stream(station_name):
    url = RADIO_STATIONS.get(station_name)
    if not url:
        return "⚠️ Station not found", 404
    
    return Response(generate_stream(url), mimetype="audio/mpeg")

# 🚀 Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
