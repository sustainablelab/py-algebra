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

# =====[ SYMBOLIC REPRESENTATION STUFF ]=====

class Ratio():
    """Symbolic representation of a list of two numbers as a ratio.

    Given two numbers: `a` and `b`, the ratio is `b/a`.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f"{self.b}/{self.a}"

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

    assert len(coeff) == 2, print(f"Must be two coefficients, your list has {len(coeff)} coefficients.")
    b = coeff[0] # x^0
    a = coeff[1] # x^1

    print(f"Solve {a}x + {b} = 0")
    ratio = Ratio(a, -1*b)
    return ratio

if __name__ == '__main__':
    print("\nSome examples calling `solve_ax_plus_b_eq_0()`:")

    print("\nEXAMPLE 1:\n")
    x = solve_ax_plus_b_eq_0([5,3])
    print(f"x = {x}")

    print("\nEXAMPLE 2:\n")
    x = solve_ax_plus_b_eq_0([0.3,1])
    print(f"x = {x}")
