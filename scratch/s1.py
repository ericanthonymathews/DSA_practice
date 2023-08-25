def bisection_method(f, a, b, tol=1e-6):
    """Finds the zeros of a function using the bisection method.

    Args:
      f: The function to find the zeros of.
      a: The lower bound of the interval to search.
      b: The upper bound of the interval to search.
      tol: The tolerance for determining when a zero has been found.

    Returns:
      The zero of the function, or None if no zero was found.
    """

    while abs(b - a) > tol:
        # Find the midpoint of the interval.
        m = (a + b) / 2

        # If the function value at the midpoint is zero, then we have found a zero.
        if f(m) == 0:
            return m

        # Otherwise, if the function value at the midpoint is negative, then the zero
        # must be in the lower half of the interval.
        elif f(m) < 0:
            b = m

        # Otherwise, the zero must be in the upper half of the interval.
        else:
            a = m

    # If we reach this point, then the interval has been reduced to a single point,
    # which must be the zero.
    return a
