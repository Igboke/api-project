from flask import Flask, jsonify
from datetime import datetime,timezone
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_info():
    current_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return jsonify({
        "email": "danieligboke669@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/Igboke/api-project"
    }),200

if __name__ == '__main__':
    app.run()