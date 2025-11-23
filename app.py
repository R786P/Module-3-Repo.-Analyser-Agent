from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from agents import run_analysis
import os

app = Flask(__name__, static_folder=".")

CORS(app)

@app.route('/')
def home():
    # Serve the frontend - index.html
    return send_from_directory('.', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        repo_url = data.get('repoUrl')
        mode = data.get('mode')

        if not repo_url or not mode:
            return jsonify({"error": "Both repoUrl and mode are required"}), 400

        result = run_analysis(repo_url, mode)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
