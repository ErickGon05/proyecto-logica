from flask import Flask, request, jsonify, send_from_directory
import tokenizer
import shunting_yard
import AST
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

    print(prem_list)

    var_list = list()

    prem_tokens_list = tokenizer.tokenizer(prem_list, var_list)

    print(var_list)

    print(prem_tokens_list)

    if isinstance(prem_tokens_list, str):
        return prem_tokens_list
        #TODO formatear el output en un json para el front

    post_fix_list = shunting_yard.shunting_yard(prem_tokens_list)

    print(post_fix_list)

    if isinstance(post_fix_list, str):
        return post_fix_list
        #TODO formatear el output en un json para el front

    ast_list = AST.ast_builder(post_fix_list)

    print(ast_list)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)