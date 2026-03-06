from tokenizer import TokenType, Token

class ASTNode:
    def __init__(self, token, left = None, right = None):
        self.token: Token = token
        self.left: Token = left
        self.right: Token = right
    def __repr__(self):
        if(self.left or self.right):
            return f"{self.token}(L:{self.left if self.left else 'none'} R:{self.right if self.right else 'none'})"
        else:
            return self.token.__repr__()

def ast_builder(post_tokens):
    stack_list = []

    for t_list in post_tokens:
        stack = []
        for token in t_list:
            token: Token

            if token.type == TokenType.VAR:
                stack.append(ASTNode(token))

            elif token.type == TokenType.NOT:
                if not stack:
                    return "falta un operador para NOT"
                
                child = stack.pop()

                stack.append(ASTNode(token, left=child))

            else:
                if len(stack) < 2:
                    return "faltan operandos"
                
                right = stack.pop()
                left = stack.pop()

                stack.append(ASTNode(token, left=left, right=right))
            
        if len(stack) != 1:
            return "expresion invalida"
        
        stack_list.append(stack[0])
    
    return stack_list



"""
def evaluate(node: ASTNode, val_dict: dict):
    if node.token.type == TokenType.VAR:
        return val_dict[node.token.value]
    
    if node.token.type == TokenType.NOT:
        return not evaluate(node.left, val_dict)
    
    left = evaluate(node.left, val_dict)
    right = evaluate(node.right, val_dict)

    if node.token.type == TokenType.AND:
        return left and right
    
    if node.token.type == TokenType.OR:
        return left or right
    
    if node.token.type == TokenType.IMP:
        return (not left) or right
    
    if node.token.type == TokenType.DIMP:
        return left == right
    
def ast(p_fix_list, var_list, val_dict = None):

    if val_dict is None:
        val_dict = {}

    if len(var_list) == 0:
        row = []
        for i in range(len(p_fix_list)):
            sintax_tree = ast_builder(p_fix_list[i])
            row.append(evaluate(sintax_tree, val_dict))

        return [row]
    
    current_value = var_list[0]
    rem_vars = var_list[1:]
    

    val_dict[current_value] = True
    ast(p_fix_list, rem_vars, val_dict.copy())

    val_dict[current_value] = False
    ast(p_fix_list, rem_vars, val_dict.copy())
    """