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

# =====[ HUMAN READABILITY STUFF ]=====

# CONVENTIONS: sometimes we don't write 1

def implied_one(a) -> str:
    """Return an empty string if a == 1, otherwise return str(a).

    Parameters
    ----------
    a :
        Must be type ``int`` or ``float``.
        Otherwise, throw an ``AssertionError``.

    Examples
    --------

    If a != 1, return str(a):
    >>> implied_one(2)
    '2'

    If ``a`` is 1, return an empty string.

    This works whether ``a`` is an ``int`` or a ``float``:

        a = 1   # int
        a = 1.0 # float

    `int a` returns an empty string:
    >>> implied_one(1)
    ''

    `float a` returns an empty string:
    >>> implied_one(1.0)
    ''

    And throw an ``AssertionError`` if ``a`` is not a
    ``float`` or an ``int``:
    >>> implied_one('1')
    Traceback (most recent call last):
    ...
    AssertionError: Expect int or float, but received <class 'str'>

    """
    assert ( (type(a) == float) or
             (type(a) == int)
           ), f"Expect int or float, but received {type(a)}"
    if a == 1:
        return ""
    else:
        return str(a)

# SYMBOLIC REPRESENTATION: print ratio, don't evaluate

class Ratio():
    """Symbolic representation of a list of two numbers as a ratio.

    Given two numbers: `a` and `b`, the ratio is `b/a`.
    """
    def __init__(self, a, b, TEMP_pretty : bool = True):
        self.a = a
        self.b = b
        self.TEMP_pretty = TEMP_pretty
    def __repr__(self):
        # Only print a ratio if denominator is not 1.
        if self.TEMP_pretty:
            if implied_one(self.a) == '':
                return f"{self.b}"
            else:
                return f"{self.b}/{self.a}"
        else:
            return f"{self.b}/{self.a}"

# =====[ ACTUAL SOLVER STUFF IS HERE ]=====

def solve_ax_plus_b_eq_0(coeff: list, TEMP_pretty : bool = True) -> Ratio:
    """Solve for x: ax + b = 0

    Example
    -------
    Solve 3x + 5 = 0

    Call this function with coefficients [x^0, x^1]:
    >>> x = solve_ax_plus_b_eq_0([5,3])
    Solve 3x + 5 = 0

    >>> print(x)
    -5/3

    If coefficient a is 1, the "Solve blah" print-out should
    not print it:
    >>> x = solve_ax_plus_b_eq_0([0.3,1])
    Solve x + 0.3 = 0

    This also means the denominator of ``Ratio`` is 1.
    Printing x should just show the numerator (don't print
    blah over 1):
    >>> print(x)
    -0.3

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

    if TEMP_pretty: _a = implied_one(a) # If coefficient `a` is 1, do not print it.
    else: _a = str(a)
    print(f"Solve {_a}x + {b} = 0")
    ratio = Ratio(a, -1*b, TEMP_pretty)
    return ratio

if __name__ == '__main__':
    print("\nSome examples calling `solve_ax_plus_b_eq_0()`:\n")
    print("EXAMPLE 1:\n")
    x = solve_ax_plus_b_eq_0([5,3])
    print(f"x = {x}")
    print("Nice, right?")
    print("""
There are many conventions to make the printed results
human-readable.

I think the important conventions are the ones that really
help the user to understand the result.

For example, I felt strongly about printing the result as a
ratio. The above -5/3 reads much nicer than -1.666666666667.
I say that was good.

But other conventions, like not printing `1` as a
coefficient of x or the denominator of a ratio, are a bad
idea to implement at this point in the project. If these are
important, leave them as a TODO and add them later.

The reason to put these off is they really don't add much
usefulness, but they add a lot of code, which will make it
much harder to build the project. This code is also
noise that hides the important stuff. So it'd be nicer to
keep a clean core of code that is the important stuff.

I only know this because I did it. I added code to "hide"
printing `1`. It is shocking how much code this adds.
""")

    print("EXAMPLE 2:\n")
    print("So in ax + b = 0, what if ``a==1``?\n")
    print("Here is what it looks like if I don't hide the `1`:")
    x = solve_ax_plus_b_eq_0([0.3,1], TEMP_pretty=False)
    print(f"x = {x}")
    print("\nAnd hiding the `1`:")
    x = solve_ax_plus_b_eq_0([0.3,1])
    print(f"x = {x}")
    print("""
So hiding the `1` is nice, but is it really that essential?

It opens a rabbit-hole of similar presentation work. If I
handle ``a==1``, the user rightly expects I'd handle the
case ``a==-1``, but I don't handle that case yet:
""")

    print("EXAMPLE 3:\n")
    x = solve_ax_plus_b_eq_0([0.3,-1])
    print(f"x = {x}")
