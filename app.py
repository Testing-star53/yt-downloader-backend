from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return "No URL", 400

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    file = [f for f in os.listdir() if f.startswith("video.")][0]
    return send_file(file, as_attachment=True)

app.run(host="0.0.0.0", port=10000)
