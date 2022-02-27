"""Solve for x

Usage
-----
Run this script to see two examples:

$ python solve.py

Test
----
$ python -m doctest solve.py

(No output is good. It means all docstring tests pass).

"""

import cmath

# =====[ SYMBOLIC REPRESENTATION STUFF ]=====

class Ratio():
    """Symbolic representation of a list of two numbers as a ratio.

    Given two numbers: `a` and `b`, the ratio is `b/a`.
    """
    def __init__(self, a : float, b : float):
        self.a = a
        self.b = b
    def __repr__(self):
        return f"{self.b}/{self.a}"

class Root():
    def __init__(self, a : float, b : float, c : float, sign : str):
        self.a = a
        self.b = b
        self.c = c
        assert (sign == '+') or (sign == '-'), f"Invalid sign `{sign}`, must be str '+' or '-'"
        self.sign = sign
    def __repr__(self) -> tuple:
        a = self.a
        b = self.b
        c = self.c
        sign = self.sign
        # TODO: simplify the representation
        return f"({-b} {sign} sqrt[{b}^2 - 4*{a}*{c}])/(2*{a})"


# =====[ ACTUAL SOLVER STUFF IS HERE ]=====

def solve_ax_plus_b_eq_0(coeff: list) -> Ratio:
    """Solve for x: ax + b = 0

    Example
    -------
    Solve 3x + 5 = 0

    Call this function with coefficients [x^0, x^1]:
    >>> x = solve_ax_plus_b_eq_0([5,3])
    Solve 3x + 5 = 0

    >>> print(x)
    -5/3

    Throw an error if user does not call this with exactly 2
    coefficients:
    >>> x = solve_ax_plus_b_eq_0([5,3,2])
    Traceback (most recent call last):
        ...
    AssertionError: Must be TWO coefficients, your list has 3 coefficients.

    Explanation
    -----------
    Algebra to solve for x::

        3x + 5 = 0
        3x = -5
        x = -5/3

    The answer is the ratio of the coefficients multiplied
    by negative 1. Easy enough. But me, the user, wants to
    see the ratio of two numbers, not the decimal expansion
    of the division!

    Why? In this example, the ratio has a 3 in the denominator.
    I'm in base 10, so any denominator that is not a
    multiple of a factor of 10 is going to give an infinite
    decimal.

    I think that is ugly. In fact, even if the answer is a
    finite decimal, I don't want to do the work of
    realizing this decimal is the ratio of the two
    coefficients. Just give me the ratio!

    Return
    ------
    Why am I returning a "Ratio"?

    I don't simply want to print a ``str``. If that's all I
    wanted, I could do that and not return anything.

    So I want to return a value. But I don't want to return
    a ``float`` because that "hides" the answer I'm looking
    for.

    I want to return a ratio, but there is no ratio type!

    I also want to print my answer and get something like::

        x = -5/3

    As opposed to just getting a list of numbers::

        (5,3)

    So I made my own Ratio class. I almost never make my own
    classes in Python, but in this case it's exactly what I
    need. I don't want Python to calculate anything, I want
    it to do symbolic manipulation.

    """

    assert len(coeff) == 2, f"Must be TWO coefficients, your list has {len(coeff)} coefficients."
    b = coeff[0] # x^0
    a = coeff[1] # x^1

    print(f"Solve {a}x + {b} = 0")
    ratio = Ratio(a, -1*b)
    return ratio

def print_roots(roots : tuple) -> None:
    for _root in roots:
        if _root.imag == 0:
            print(f"(x + {-1*_root.real})")
        else:
            print(f"( x + {-1*_root} )")

def solve_second_order(coeff: list) -> tuple:
    """Solve for x: ax^2 + bx + c = 0

    Return
    ------
    roots : tuple

        Polynomial is second order, so there are two roots.
        Each root is type ``complex``. Return a Python
        ``tuple`` of ``complex`` objects.

    Examples
    --------

    Throw an error if user does not call this with exactly 3
    coefficients:
    >>> roots = solve_second_order([2, 3])
    Traceback (most recent call last):
        ...
    AssertionError: Must be THREE coefficients, your list has 2 coefficients.

    >>> roots = solve_second_order([2, 3, 1])
    Solve 1x^2 + 3x + 2 = 0

    >>> type(roots[0])
    <class 'complex'>

    >>> print(roots)
    ((-1+0j), (-2+0j))

    >>> print_roots(roots)
    (x + 1.0)
    (x + 2.0)

    Explanation
    -----------

    Algebra to solve for x::

        ax² + bx + c = 0
        ax² + bx = -c
        x² + (b/a)x = -(c/a)
        x² + (b/a)x + ___ = ___ + -(c/a)
          ┌────────────┴─────┘
          └ COMPLETE THE SQUARE:
            Square has sides of length (x + m)
            (x + m)(x + m) = x² + (2m)x + m²
                                  └┬─┘
                  ┌────────────────┘
                  └ 2m = b/a
                    m = b/(2a)
                    m² = b²/(2a)²
                    m² = b²/(4a²)
        x² + (b/a)x + b²/(4a²) = b²/(4a²) - c/a
        └─────┬──────────────┘
              └─ (x + b/(2a))² = b²/(4a²) - c/a
        x + b/(2a) = ± sqrt[b²/(4a²) - c/a]
        x = -b/(2a) ± sqrt[b²/(4a²) - c/a]

                      sqrt┌b² - 4ac┐
        x = -b/(2a) ±     │────────│
                          └   4a²  ┘

            -b   sqrt[b² - 4ac]
        x = ── ± ─────────────── 
            2a          2a

       ┌────────────────────────┐
       │    -b ± sqrt[b² - 4ac] │
       │x = ─────────────────── │
       │           2a           │
       └────────────────────────┘

    First make up a simple example::

               x + 1
             * x + 2
               ─────
              2x + 2
        x^2 +  x
        ────────────
        x^2 + 3x + 2

    Solve for x: x^2 + 3x + 2

    Expect roots ``x = -1`` and ``x = -2``.

    Input coefficients as a list::

        # 
        # c*x^0, b*x^1, a*x^2
        [ 2,     3,     1]

    Assert len(coeff) == 3.

    x1 = (-3 + cmath.sqrt(3**2 - 4*1*2))/(2*1)
    x2 = (-3 - cmath.sqrt(3**2 - 4*1*2))/(2*1)

    x1 = -1
    x2 = -2

    """

    assert len(coeff) == 3, f"Must be THREE coefficients, your list has {len(coeff)} coefficients."

    c = coeff[0] # x^0
    b = coeff[1] # x^1
    a = coeff[2] # x^2
    
    print(f"Solve {a}x^2 + {b}x + {c} = 0")

    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)

    return (x1, x2)


def better_solve_second_order(coeff: list) -> tuple:
    assert len(coeff) == 3, f"Must be THREE coefficients, your list has {len(coeff)} coefficients."

    c = coeff[0] # x^0
    b = coeff[1] # x^1
    a = coeff[2] # x^2
    
    print(f"Solve {a}x^2 + {b}x + {c} = 0")

    return (Root(a,b,c,'+'), Root(a,b,c,'-'))

if __name__ == '__main__':
    print("\nSome examples calling `solve_ax_plus_b_eq_0()`:")

    print("\nEXAMPLE 1:\n")
    x = solve_ax_plus_b_eq_0([5,3])
    print(f"x = {x}")

    print("\nEXAMPLE 2:\n")
    x = solve_ax_plus_b_eq_0([0.3,1])
    print(f"x = {x}")

    print("\nSome examples calling `solve_second_order()`:")

    print("\nEXAMPLE 1:\n")
    roots = solve_second_order([2, 3, 1])
    print("Roots:")
    print_roots(roots)

    print("\nEXAMPLE 2:\n")
    roots = solve_second_order([2, 2, 1])
    print("Roots:")
    print_roots(roots)

    print("\nTry writing a better version of `solve_second_order()`:")
    print("\nEXAMPLE 1:\n")
    roots = better_solve_second_order([2, 3, 1])
    print("Roots:")
    for root in roots:
        print(root)
