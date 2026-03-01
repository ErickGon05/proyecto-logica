from tokenizer import TokenType, Token

PRECEDENCE = {
    TokenType.NOT: 5,
    TokenType.AND: 4,
    TokenType.OR: 3,
    TokenType.IMP: 2,
    TokenType.DIMP: 1
}

RIGHT_ASSO = (TokenType.NOT, TokenType.IMP)

def shunting_yard(token_lists):

    post_fix_list = []

    for token_list in token_lists:

        output = []
        op_stack = []

        for token in token_list:
            token: Token

            if token.type == TokenType.VAR:
                output.append(token)

            elif token.type in PRECEDENCE:
                while (
                    op_stack and op_stack[-1] in PRECEDENCE and 
                    (
                    PRECEDENCE[op_stack[-1].type] > PRECEDENCE[token.type] or 
                    (
                        PRECEDENCE[op_stack[-1].type] == PRECEDENCE[token.type] and token.type not in RIGHT_ASSO
                    )
                                                                    )): 
                        output.append(op_stack.pop())
                op_stack.append(token)
            
            elif token.type == TokenType.LPAR:
                 op_stack.append(token)
                
            elif token.type == TokenType.RPAR:
                while op_stack and op_stack[-1].type != TokenType.LPAR:
                    output.append(op_stack.pop())

                if not op_stack:
                    return "Error: parentesis desbalanceado"
                
                op_stack.pop()
        
        while op_stack:
            if op_stack[-1] in (TokenType.LPAR, TokenType.RPAR):
                return "Error: parentesis desbalanceado"
            output.append(op_stack.pop())
        
        post_fix_list.append(output)
    
    return post_fix_list