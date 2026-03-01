from flask import Flask, request, jsonify, send_from_directory
import tokenizer
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

    prem_list = message.split(", ")

    print(message)
    print(prem_list)

    for p in prem_list:
        print(p)

    var_list = list()

    prem_tokens_list = tokenizer.tokenizer(prem_list, var_list)

    if isinstance(prem_tokens_list, str):
        return prem_tokens_list
        #TODO formatear el output en un json para el front

    for p in prem_tokens_list:
        print(p)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)