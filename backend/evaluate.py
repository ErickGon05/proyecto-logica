from AST import ASTNode
from tokenizer import Token, TokenType

def evaluate_ast(node: ASTNode, val_dict: dict):
    if node.token.type == TokenType.VAR:
        return val_dict[node.token.value]
    
    if node.token.type == TokenType.NOT:
        return not evaluate_ast(node.left, val_dict)
    
    left = evaluate_ast(node.left, val_dict)
    right = evaluate_ast(node.right, val_dict)

    if node.token.type == TokenType.AND:
        return left and right
    
    if node.token.type == TokenType.OR:
        return left or right
    
    if node.token.type == TokenType.IMP:
        return (not left) or right
    
    if node.token.type == TokenType.DIMP:
        return left == right

def evaluate(ast_list:list, comb_list: list, prem_list: list, conc):
    prem_ans_list = []
    for dictionary in comb_list:
        row = []
        for ast in ast_list:
            res = evaluate_ast(ast, dictionary)
            row.append(res)
        prem_ans_list.append(row)

    for i in range(len(comb_list)):
        print(f"premisas: {prem_list} conclusion: {conc}, {comb_list[i]}: {prem_ans_list[i]}")
    return prem_ans_list