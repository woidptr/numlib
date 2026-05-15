from typing import Callable


def simpsons_rule(
    func: Callable[[float], float],
    a: float,
    b: float,
    n: int,
) -> float:
    """
    Approximates the definite integral of f(x) from a to b using Simpson's 1/3 rule.
    Returns the enstimated area as a float.
    """

    if n <= 0:
        raise ValueError("Number of panels (n) must be a positive integer.")
    if n % 2 != 0:
        raise ValueError("Number of panels (n) must be an even number for Simpson's Rule.")
    
    h: float = (b - a) / n

    area: float = func(a) + func(b)

    for i in range(1, n):
        x_i: float = a + i * h

        if i % 2 == 0:
            area += 2.0 * func(x_i)
        else:
            area += 4.0 * func(x_i)
    
    return area * (h / 3.0)
