from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "CI/CD Pipeline Demo - Deployed via GitHub Actions!",
        "version": os.getenv("APP_VERSION", "v1.0"),
        "deployed_by": "GitHub Actions → ECR → EKS"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
