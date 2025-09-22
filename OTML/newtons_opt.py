import numpy as np


def f(params):
    # Example function: f(x, y) = (x-1)^2 + (y+2)^2
    x, y = params
    return (x - 1) ** 2 + (y + 2) ** 2


def gradient(params):
    # Gradient: [df/dx, df/dy]
    x, y = params
    return np.array([2 * (x - 1), 2 * (y + 2)])


def hessian(params):
    # Hessian matrix is constant for this quadratic function
    return np.array([[2, 0], [0, 2]])


def newton_method(init_params, tol=1e-6, max_iter=100):
    params = np.array(init_params, dtype=float)
    for i in range(max_iter):
        grad = gradient(params)
        hess = hessian(params)
        step = np.linalg.solve(hess, grad)
        params -= step
        if np.linalg.norm(grad) < tol:
            break
    return params


if __name__ == "__main__":
    initial_params = [0.0, 0.0]
    optimal_params = newton_method(initial_params)
    print("Newton's method optimal parameters:", optimal_params)
