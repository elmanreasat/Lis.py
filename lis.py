from evaluate import *

def repl(prompt='lis.py> '):
        while True:
            val = eval(parse(input(prompt)))
            if val is not None: 
                print(schemestr(val))

def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)

repl()