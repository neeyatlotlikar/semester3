import numpy as np


def gradient(params):
    # Gradient: [df/dx, df/dy]
    x, y = params
    return np.array([2 * (x - 1), 2 * (y + 2)])


def bfgs_method(init_params, tol=1e-6, max_iter=100):
    params = np.array(init_params, dtype=float)
    n = len(params)
    B = np.eye(n)
    for _ in range(max_iter):
        grad = gradient(params)
        if np.linalg.norm(grad) < tol:
            break
        # Direction: p = -B^{-1} * gradient
        p = -np.linalg.solve(B, grad)
        params_new = params + p
        grad_new = gradient(params_new)
        s = params_new - params
        y = grad_new - grad
        ys = np.dot(y, s)
        # BFGS update
        if ys > 1e-10:  # safeguard against small denominators
            rho = 1.0 / ys
            I = np.eye(n)
            B = (I - rho * np.outer(s, y)) @ B @ (
                I - rho * np.outer(y, s)
            ) + rho * np.outer(s, s)
        else:
            # skip update or reset B to identity to maintain positive definiteness
            B = np.eye(n)
        params = params_new
    return params


# Usage
initial_params = [0.0, 0.0]
optimal_params_bfgs = bfgs_method(initial_params)
print("BFGS optimal parameters:", optimal_params_bfgs)
