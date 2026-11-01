from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from my DevSecOps pipeline!"


@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/about")
def about():
    return "This app is protected by a DevSecOps pipeline."
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)