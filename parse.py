Symbol = str              # A Scheme Symbol is implemented as a Python str
Number = (int, float)     # A Scheme Number is implemented as a Python int or float
Atom   = (Symbol, Number) # A Scheme Atom is a Symbol or Number
List   = list             # A Scheme List is implemented as a Python list
Exp    = (Atom, List)     # A Scheme expression is an Atom or List
Env    = dict             # A Scheme environment (defined below) 
                          # is a mapping of {variable: value}

def parse(program):
    return read_from_tokens(tokenize(program))

def tokenize(program):
    return program.replace('(', ' ( ').replace(')', ' ) ').split()
    return program



def read_from_tokens(tokens):

    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')

    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)


def atom(token):
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)


program = "(begin (define r 10) (* pi (* r r)))"
print(parse(program))