Solve algebra:

```python
>>> import solve
>>> x = solve.solve_ax_plus_b_eq_0([5,3])
Solve 3x + 5 = 0
>>> print(x)
-5/3
```

# Files

- [use-solve.py](use-solve.py) example script that uses lib `solve.py`
- [solve.py](solve.py) the actual lib

# Usage

## Run the example script

```run-example-script
$ python use-solve.py
Solve 3x + 5 = 0
x=-5/3
```

## Run the lib tests with `doctest`

```run-lib-doctests
$ python -m doctest solve.py

```

*Expect no output.*

## Run the lib as a script

This prints a few examples. It also prints my thoughts on what
*not* to do, having taken my initial stab:

```run-solve-as-py-script
$ python solve.py 

Some examples calling `solve_ax_plus_b_eq_0()`:

EXAMPLE 1:

Solve 3x + 5 = 0
x = -5/3

EXAMPLE 2:

Solve 1x + 0.3 = 0
x = -0.3/1

And hiding the `1`:
Solve x + 0.3 = 0
x = -0.3

EXAMPLE 3:

Solve -1x + 0.3 = 0
x = -0.3/-1

```
