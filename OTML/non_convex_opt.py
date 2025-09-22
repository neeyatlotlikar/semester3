import numpy as np


def simulated_annealing(fun, max_iter, x0, T_start, cooling_rate):
    x = x0
    T = T_start
    best_x = x0
    best_val = fun(x0)

    for _ in range(max_iter):
        # Small random step
        x_new = x + np.random.uniform(-1, 1)
        delta_f = fun(x_new) - fun(x)
        if delta_f < 0 or np.random.rand() < np.exp(-delta_f / T):
            x = x_new
            if fun(x) < best_val:
                best_val = fun(x)
                best_x = x
        T *= cooling_rate
    return best_x


if __name__ == "__main__":

    def fun(x):
        return x**4 - 3 * x**3 + 2

    minimum = simulated_annealing(
        fun, max_iter=10000, x0=0.0, T_start=1.0, cooling_rate=0.999
    )
    print(f"Simulated Annealing found minimum at x = {minimum:.4f}")
