from flask import Flask

app = Flask(__name__)

@app.route("/api/", methods=["GET"])
def api_root():
    with open("data.json", "r") as file:
        data = file.read()
    return data, 200, {"Content-Type": "application/json"}

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
