# Optimization Techniques for Machine Learning Lab Experiments

1) Implement Gradient Descent (Date: 24/07/2025)

    On 31/07/2025, [Gradient Descent](https://medium.com/data-science/complete-step-by-step-gradient-descent-algorithm-from-scratch-acba013e8420)

2) Stochastic Gradient Descent (Date: 14/08/2025)

3) Minibatch (Date: 21/08/2025)

4) Non-convex optimization

5) Newton method and quasi-Newton optimization

6) Co-ordinate descent (Date: 27/10/25)

7) Lower bound for smooth and convex functions (Date: 03/11/25)

    For **L-smooth and convex functions**, the lower bound on the convergence rate of first-order optimization methods after $T$ iterations is on the order of $$\frac{1}{T^2}$$. Specifically, for any first-order method, there exists an $L$-smooth convex function such that the function value gap satisfies:

    $$
    f(x^{(T)}) - f(x^*) \geq \frac{3L \|x^{(0)} - x^*\|^2}{32(T+1)^2}
    $$

    This result shows that no first-order algorithm can converge faster than $$\mathcal{O}(1/T^2)$$ in the worst case for smooth convex optimization.

    In contrast, standard gradient descent (GD) achieves only a $$\mathcal{O}(1/T)$$ rate for smooth convex functions, meaning there is **room for improvement**. This gap is closed by accelerated methods such as **Nesterov’s acceleration**, which achieve the optimal $$\mathcal{O}(1/T^2)$$ convergence rate, matching the lower bound.

8) Lower bounds for non-smooth functions

9) Lower bounds and accelerated gradient descent
