from flask import Flask, request, jsonify
import tokenizer
import shunting_yard
import AST
import evaluate
import combination
import critic
import var_finder

app = Flask(__name__,static_folder="../frontend",static_url_path="")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/eval", methods=['POST'])
def recibe():
    data = request.get_json()

    premisas = data.get("premisas")

    conclusion = data.get("conclusion")

    prem_list = premisas.split(", ")

    var_list = list()

    tokens_list = tokenizer.tokenizer(prem_list + [conclusion], var_list)

    if isinstance(tokens_list, str):
        return jsonify({"error": True, "message": tokens_list})

    postfix_list = shunting_yard.shunting_yard(tokens_list)

    print(" ".join(map(str, postfix_list[0])))

    if isinstance(postfix_list, str):
        return jsonify({"error": True, "message": postfix_list})

    ast_list = AST.ast_builder(postfix_list)

    if isinstance(ast_list, str):
        return jsonify({"error": True, "message": ast_list})

    comb_list = combination.comb_generator(var_list)

    ans_list = evaluate.evaluate(ast_list, comb_list, prem_list, conclusion)

    critic_index_list = critic.critic_ident(ans_list)

    print('renglones criticos: ',critic_index_list)

    invalid_index_list = critic.invalid_ident(critic_index_list, ans_list)

    invalid = len(invalid_index_list) != 0 or len(critic_index_list) == 0

    atomic_index = []

    for i in range(len(prem_list)):
        if prem_list[i].strip() in var_list:
            atomic_index.append(i + len(var_list))

    ans = {
        "error": False,
        "invalid": invalid,
        "premisas": prem_list,
        "conclusion": conclusion,
        "variables": var_list,
        "combination_list": comb_list,
        "ans_list": ans_list,
        "critic_index_list": critic_index_list,
        "invalid_index_list": invalid_index_list,
        "atomic_index": atomic_index,
        "message": "ok"
    }

    return jsonify(ans), 200

if __name__ == "__main__":
    app.run(debug=True)