from typing import Callable


def bisection(
    func: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-1,
    max_iter: int = 1000,
) -> tuple[float, int]:
    """
    Finds the root of a function using the Bisection method.
    Requires func(a) and func(b) to have opposite signs.
    """

    if func(a) * func(b) >= 0:
        raise ValueError("Root is not bracketed: f(a) and f(b) must have opposite signs.")
    
    for i in range(max_iter):
        midpoint: float = (a + b) / 2.0

        if abs(func(midpoint)) < tol or (b - a) / 2.0 < tol:
            return midpoint, i
        
        if func(midpoint) * func(a) < 0.0:
            b = midpoint
        else:
            a = midpoint
    
    raise TimeoutError("Exceeded maximum interations without converging.")
