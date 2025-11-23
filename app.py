from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- new line
from agents import run_analysis

app = Flask(__name__)
CORS(app)  # <-- new line - enables CORS for all routes

@app.route('/')
def home():
    return "GitHub AI Agent Backend is running!"

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
