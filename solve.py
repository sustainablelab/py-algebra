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

def hide_imaginary_if_eq_0(c : complex):
    """Return only the real part if imaginary part is 0.

    Example
    -------
    Set up a complex number:
    >>> z = 2 + cmath.sqrt(-2)
    >>> print(z)
    (2+1.4142135623730951j)

    It has a non-zero imaginary part, so this function just returns it as-is:
    >>> hide_imaginary_if_eq_0(z)
    (2+1.4142135623730951j)

    Set up a complex number with no imaginary part:
    >>> z = 2 + cmath.sqrt(2)
    >>> print(z)
    (3.414213562373095+0j)

    Imaginary part is zero this time, so this function just returns the real
    part:
    >>> hide_imaginary_if_eq_0(z)
    3.414213562373095
    """
    if c.imag == 0: return c.real
    else: return c

def poly_str(coeff: list) -> str:
    """Express polynomial as a human-readable string.

    Parameters
    ----------
    coeff : list
    
        List of polynomial coefficients starting with the
        coefficient of x^0 at index 0, then the coefficient
        of x^1 at index 1, etc.

    Example
    -------
    >>> poly_str([2,2,1])
    '1x^2 + 2x + 2'

    """
    assert len(coeff) > 0, "List of coefficients cannot be empty."
    # Return a string.
    _str = ""
    # Calculate polynomial order.
    order = len(coeff)
    # Put the highest-order coefficient first.
    flipped_coeff = coeff[::-1] # DO NOT USE coeff.reverse()
    # Build the polynomial string:
    o = order # order of "this" term
    for c in flipped_coeff:
        o -= 1 # decrement the order
        if o > 1:
            _str += f"{c}x^{o} + "
        elif o == 1:
            _str += f"{c}x + "
        else:
            _str += f"{c}"
    return _str

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

    print(f"Solve {poly_str(coeff)} = 0")
    ratio = Ratio(a, -1*b)
    return ratio

class Root():
    """A root of the quadratic: ax^2 + bx + c = 0

    Methods
    -------

    __repr__ :

        Perform purely symbolic manipulation to express the root as
        a string.

    calc :

        Calculate a numeric value.

    as_factor :

        Calculate a numeric value, but express as a
        1st-order polynomial (a string).

    Parameters
    ----------

    a, b, c : float

        The coefficients in the expression ax^2 + bx + c = 0

    sign : str

        Either '+' or '-'. There are two roots. Instantiate
        the root with sign='+' or with sign='-'.

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

    """
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

    def calc(self) -> complex:
        a = self.a
        b = self.b
        c = self.c
        sign = self.sign
        if   sign == '+': result = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
        elif sign == '-': result = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
        else: assert False, f"Programmer error: How did Root get sign='{sign}'?"
        result = hide_imaginary_if_eq_0(result)
        return result

    def as_factor(self) -> str:
        root = self.calc()
        return f"(x + {-1*root})"

def solve_second_order(coeff: list) -> tuple:
    """Repackage the polynomial as a list of roots.

    Return
    ------
    roots : tuple

        Polynomial is second order, so there are two roots.
        Each root is type ``Root``. Return a Python
        ``tuple`` of ``Root`` objects.

        The work to "solve for x" in "ax^2 + bx + c = 0"
        happens in the ``Root`` methods.


    Example
    -------
    >>> roots = solve_second_order([-35,2,1])
    Solve 1x^2 + 2x + -35 = 0

    The return value is a ``tuple`` of roots (an immutable list of roots):
    >>> type(roots)
    <class 'tuple'>

    Inspecting the root returns a string for human readability from the
    ``root.__repr__()``:
    >>> roots[0]
    (-2 + sqrt[2^2 - 4*1*-35])/(2*1)
    >>> roots[1]
    (-2 - sqrt[2^2 - 4*1*-35])/(2*1)

    To calculate the value of the root, call ``root.calc()``:
    >>> roots[0].calc()
    5.0
    >>> roots[1].calc()
    -7.0

    Note that real roots are returned as type ``float``.
    If the roots are complex, ``root.calc()`` returns type ``complex``:
    >>> roots = solve_second_order([2,2,1])
    Solve 1x^2 + 2x + 2 = 0
    >>> roots[0].calc()
    (-1+1j)
    >>> roots[1].calc()
    (-1-1j)

    """
    assert len(coeff) == 3, f"Must be THREE coefficients, your list has {len(coeff)} coefficients."

    c = coeff[0] # x^0
    b = coeff[1] # x^1
    a = coeff[2] # x^2
    
    # print(f"Solve {a}x^2 + {b}x + {c} = 0")
    print(f"Solve {poly_str(coeff)} = 0")
    return (Root(a,b,c,'+'), Root(a,b,c,'-'))

# =====[ HELPERS FOR REDUCING LOC IN main() ]=====

def print_a_bunch_of_stuff(coeff : list) -> None:

    # Find roots of quadratic
    roots = solve_second_order(coeff)

    # Show me the human readable roots and their calculated values.
    print("Roots:")
    for root in roots:
        print(root, " = ", root.calc())

    # Also show answer as a product of 1st-order factors.
    print("Print quadratic roots as 1st-order factors:")
    factors = [root.as_factor() for root in roots]
    print(poly_str(coeff), " = ", f"{factors[0]}{factors[1]}")

if __name__ == '__main__':
    print("\nSome examples calling `solve_ax_plus_b_eq_0()`:")

    print("\nEXAMPLE 1:\n")
    x = solve_ax_plus_b_eq_0([5,3])
    print(f"x = {x}")

    print("\nEXAMPLE 2:\n")
    x = solve_ax_plus_b_eq_0([0.3,1])
    print(f"x = {x}")

    print("\nSome examples calling `solve_second_order()`:")
    print("\nEXAMPLE 1: real roots calculate into type `float`\n")
    coeff = [2,3,1]
    print_a_bunch_of_stuff(coeff)

    print("\nEXAMPLE 2: complex roots calculate into type `complex`\n")
    coeff = [2,2,1]
    print_a_bunch_of_stuff(coeff)

