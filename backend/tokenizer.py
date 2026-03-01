from enum import Enum, auto

class TokenType(Enum):
    VAR = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    LPAR = auto()
    RPAR = auto()
    IMP = auto()
    DIMP = auto()

class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value is not None:
            return f"{self.type.name}({self.value})"
        return self.type.name

def tokenizer(prem_l: list, var_list: list):
    prems_tokens = []
    for prem in prem_l:
        tokens = []
        i: int = 0
        while i < len(prem):
            c: str = prem[i]

            if c.isspace():
                i += 1
                continue

            if c == '(':
                tokens.append(Token(TokenType.LPAR))
                i += 1
                continue

            if c == ')':
                tokens.append(Token(TokenType.RPAR))
                i += 1
                continue

            if c == '-':
                tokens.append(Token(TokenType.NOT))
                i += 1
                continue

            if c == '&':
                tokens.append(Token(TokenType.AND))
                i += 1
                continue

            if c == '|':
                tokens.append(Token(TokenType.OR))
                i += 1
                continue

            if c == '>':
                tokens.append(Token(TokenType.IMP))
                i += 1
                continue

            if c == '<':
                i += 1
                if i == len(prem) or prem[i] != '>':
                    return "sintaxis invalida: no se permite utilizar '<' sin ser cerrado por '>' inmediatamente despues"
                tokens.append(Token(TokenType.DIMP))
                i += 1
                continue

            if c.isalnum() or c == '_':
                start = i

                while i < len(prem) and (prem[i].isalnum() or prem[i] == '_'):
                    i += 1
                
                name = prem[start:i]

                if name not in var_list:
                    var_list.append(name)
                
                tokens.append(Token(TokenType.VAR, name))
                continue

            return f"sintaxis invalida: caracter invalido '{c}'"
        
        prems_tokens.append(tokens)
    
    return prems_tokens