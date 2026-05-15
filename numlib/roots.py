from typing import Callable
from dataclasses import dataclass


@dataclass
class RootResult:
    root: float
    iterations: int


def bisection(
    func: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-1,
    max_iter: int = 1000,
) -> RootResult:
    """
    Finds the root of a function using the Bisection method.

    Parameters
    ----------
    func : Callable[[float], float]
        The mathematical function to evaluate.
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    tol : float, optional
        The tolerance for the stopping criterion. The algorithm converges when 
        the interval width or the absolute function value is less than this. 
        Default is 1e-1.
    max_iter : int, optional
        The maximum number of iterations allowed before raising an error. 
        Default is 1000.
    
    Returns
    -------
    BisectionResult
        An object containing the estimated root and iteration count.
    
    Raises
    ------
    ValueError
        If the root is not bracketed (func(a) and func(b) do not have opposite signs)
    """

    if func(a) * func(b) >= 0:
        raise ValueError("Root is not bracketed: f(a) and f(b) must have opposite signs.")
    
    for i in range(max_iter):
        midpoint: float = (a + b) / 2.0

        if abs(func(midpoint)) < tol or (b - a) / 2.0 < tol:
            return RootResult(root=midpoint, interations=i)
        
        if func(midpoint) * func(a) < 0.0:
            b = midpoint
        else:
            a = midpoint
    
    raise TimeoutError("Exceeded maximum interations without converging.")


def halley(
    func: Callable[[float], float],
    dfunc: Callable[[float], float],
    d2func: Callable[[float], float],
    x0: float,
    tol: float = 1e-8,
    max_iter: int = 1000,
) -> RootResult:
    """
    Finds the root of a function using Halley's method (cubic convergence).

    Parameters
    ----------
    func : Callable[[float], float]
        The mathematical function f(x).
    dfunc : Callable[[float], float]
        The first derivative f'(x).
    d2func : Callable[[float], float]
        The second derivative f''(x).
    x0 : float
        The initial guess for the root.
    tol : float, optional
        Tolerance for the step size and function evaluation. Default is 1e-8.
    max_iter : int, optional
        Maximum allowed iterations. Default is 1000.
        
    Returns
    -------
    RootResult
        An object containing the estimated root, iteration count, and convergence status.
        
    Raises
    ------
    ZeroDivisionError
        If the denominator in Halley's formula evaluates to exactly zero.
    """

    x: float = x0

    for i in range(max_iter):
        fx: float = func(x)

        if abs(fx) < tol:
            return RootResult(root=x, iterations=i)
        
        dfx: float = dfunc(x)
        d2fx: float = d2func(x)

        denominator: float = (dfx ** 2) - 0.5 * fx * d2fx
        if denominator == 0.0:
            raise ZeroDivisionError(f"Denominator became zero at x={x}. Cannot continue.")
        
        step: float = (fx * dfx) / denominator
        x_new: float = x - step

        if abs(x_new - x) < tol:
            return RootResult(root=x_new, iterations=i+1)
        
        x = x_new
    
    raise TimeoutError("Exceeded maximum interations without converging.")
