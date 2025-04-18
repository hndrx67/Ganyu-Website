from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve static files
@app.route('/')
def home():
    return send_from_directory('templates', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if path.endswith('.html'):
        return send_from_directory('templates', path)
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)