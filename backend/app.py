from flask import Flask, request, jsonify
import tokenizer
import shunting_yard
import AST
import evaluate
import combination
import critic
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

    premisas = data.get("premisas")

    conclusion = data.get("conclusion")

    prem_list = premisas.split(", ")

    print(prem_list)

    print(conclusion)

    var_list = list()

    prem_tokens_list = tokenizer.tokenizer(prem_list, var_list)

    conc_tokens_list = tokenizer.tokenizer([conclusion], var_list)

    print(var_list)

    print(prem_tokens_list)

    if isinstance(prem_tokens_list, str):
        return prem_tokens_list
        #TODO formatear el output en un json para el front

    if isinstance(conc_tokens_list, str):
        return conc_tokens_list
        #TODO formatear el output en un json para el front

    prem_postfix_list = shunting_yard.shunting_yard(prem_tokens_list)

    conc_postfix_list = shunting_yard.shunting_yard(conc_tokens_list)

    print(prem_postfix_list)

    if isinstance(prem_postfix_list, str):
        return prem_postfix_list
        #TODO formatear el output en un json para el front

    if isinstance(conc_postfix_list, str):
        return conc_postfix_list
        #TODO formatear el output en un json para el front

    print(f"prem: {prem_postfix_list} conc: {conc_postfix_list}")

    print(prem_postfix_list + conc_postfix_list)

    ast_list = AST.ast_builder(prem_postfix_list + conc_postfix_list)

    print(ast_list)

    if isinstance(ast_list, str):
        return ast_list
        #TODO formatear el output en un json para el front

    comb_list = combination.comb_generator(var_list)

    ans_list = evaluate.evaluate(ast_list, comb_list, prem_list, conclusion)

    critic_index_list = critic.critic_ident(ans_list)

    print('renglones criticos: ',critic_index_list)

    invalid_index_list = critic.invalid_ident(critic_index_list, ans_list)

    invalid = len(invalid_index_list) != 0

    print('renglones invalidos: ',invalid_index_list)

    ans = {
        "error": False,
        "invalid": invalid,
        "premisas": prem_list,
        "conclusion": conclusion,
        "variables": var_list,
        "combination_list": comb_list,
        "ans_list": ans_list,
        "critic_index_list": critic_index_list,
        "invalid_index_list": invalid_index_list
    }

    return jsonify(ans), 200

if __name__ == "__main__":
    app.run(debug=True)