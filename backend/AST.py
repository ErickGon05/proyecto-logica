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