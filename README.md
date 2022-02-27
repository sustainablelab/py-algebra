Solve algebra:

```python-repl
>>> import solve

>>> x = solve.solve_ax_plus_b_eq_0([5,3])
Solve 3x + 5 = 0
>>> print(x)
-5/3

>>> roots = solve.solve_second_order([2,2,1])
Solve 1x^2 + 2x + 2 = 0
>>> solve.print_roots(roots)
( x + (1-1j) )
( x + (1+1j) )
```

# Files

- [use-solve.py](use-solve.py) example script that uses lib `solve.py`
- [solve.py](solve.py) the actual lib

# Usage

## Run the example script

```run-example-script
$ python use-solve.py 
Solve 3x + 5 = 0
x = -5/3

Solve 1x^2 + 2x + 2 = 0
Roots:
( x + (1-1j) )
( x + (1+1j) )
```

## Run the lib tests with `doctest`

```run-lib-doctests
$ python -m doctest solve.py
```

*Expect no output. That means all tests pass.*

## Run the lib as a script

This prints a few examples.

```run-solve-as-py-script
$ python solve.py 

Some examples calling `solve_ax_plus_b_eq_0()`:

EXAMPLE 1:

Solve 3x + 5 = 0
x = -5/3

EXAMPLE 2:

Solve 1x + 0.3 = 0
x = -0.3/1

Some examples calling `solve_second_order()`:

EXAMPLE 1:

Solve 1x^2 + 3x + 2 = 0
Roots:
(x + 1.0)
(x + 2.0)

EXAMPLE 2:

Solve 1x^2 + 2x + 2 = 0
Roots:
( x + (1-1j) )
( x + (1+1j) )
```
