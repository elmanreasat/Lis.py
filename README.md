# Lis.py

Interpreter for Scheme (A dialect of LISP) in Python.
Contains two modules that cover tokenizing, parsing, loading environments and evaluating valid Scheme code input.

## Coverage
Lispy is currently a lightweight interpreter that can deal with primitive and other non-primitive essentials of Scheme.
These are but not confined to the following:

+ Mathematical operators (Infix)
+ Primitive data structures (Number (Integers) , Strings, lists)
+ String literals and comments ("", ;;)
+ Procedure calls/Functions using lambda calculus
+ Abstract list functions (map)
+ User defined data structures
+ Racket predicates (equal?)
+ Functional paradigm supported
+ Dynamic scoping and environment building
+ Supports algorithms designed with these restrictions
+ Command line utility so available to all users alike
+ Interactive interface with minimalistic error handling

## Setup
```sh
$ git clone https://github.com/elmanreasat/Lis.py
$ cd Lis.py
$ py lis.py
```
## Examples
```sh
lis.py> (* (+ 1 1) (/ (- 5 3) 2))
2.0

lis.py> (define lst (list 1 2 3))
lis.py> lst
(1 2 3)

lis.py> (define factorial (lambda (n) (if (<= n 1) 1 (* n (factorial (- n 1))))))
lis.py> (factorial 10)
3628800 
lis.py> (factorial 100)
9332621544394415268169923885626670049071596826438162146859296389521759999322991
5608941463976156518286253697920827223758251185210916864000000000000000000000000

lis.py> (define circle-area (lambda (r) (* pi (* r r))))
lis.py> (circle-area 3)
28.274333877

lis.py> (define first car)
lis.py> (define rest cdr)
lis.py> (define count (lambda (item L) (if L (+ (equal? item (first L)) (count item (rest L))) 0)))
lis.py> (count 0 (list 0 1 2 3 0 0)) 
3

lis.py> (count (quote the) (quote (the more the merrier the bigger the better)))
4
```

## Disclaimer

Project created for learning purposes not production use.

## Author

Elman Reasat: [E-mail](mailto:elmanreasat@hotmail.com), [@elmanreasat]
(https://www.github.com/elmanreasat)

## License 

The command line utility is available as open source under the terms of
the [MIT License](https://opensource.org/licenses/MIT)
