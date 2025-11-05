from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    msg = os.getenv("APP_MESSAGE", "APP_MESSAGE not set")
    return f"<h1>{msg}</h1>"


@app.route('/health')
def health():
    healthStatus = os.getenv("APP_HEALTH", "APP_HEALTH not set")
    return healthStatus

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)