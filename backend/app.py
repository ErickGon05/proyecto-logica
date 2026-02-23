from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__,
            static_folder="../frontend",
            static_url_path="")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/eval", methods=['POST'])
def recibe():
    data = request.get_json()

    message = data.get("message")

    print(message)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)