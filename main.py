import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    version = os.environ.get("APP_VERSION", "v1 - Buildpacks")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cloud Run Deployment Demo</title>
</head>
<body style="font-family:Arial,sans-serif;max-width:760px;margin:70px auto;line-height:1.7">
  <h1>Cloud Run Deployment Demo 🚀</h1>
  <h2>Application version: {version}</h2>
  <p>This Python Flask application is running on Google Cloud Run.</p>
  <p>Try the <a href="/info">/info</a> endpoint to see runtime details.</p>
</body>
</html>"""


@app.get("/info")
def info():
    return jsonify(
        version=os.environ.get("APP_VERSION", "v1 - Buildpacks"),
        hostname=socket.gethostname(),
        port=os.environ.get("PORT", "8080"),
        message="Hello from Cloud Run!",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
