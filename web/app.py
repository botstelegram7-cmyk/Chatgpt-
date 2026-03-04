from flask import Flask
from threading import Thread
from config import PORT

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK",200

def start_web():
    def run():
        app.run(host="0.0.0.0", port=PORT)
    Thread(target=run).start()