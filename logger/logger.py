from flask import Flask, request

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log():
    data = request.form.get("log", "")
    print(f"LOG: {data}")
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
