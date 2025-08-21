import numpy as np


class GradientDescent:
    def __init__(self, loss_function, tolerance=1e-6, max_iterations=1000):
        self.learning_rate = 1.0
        self.loss_function = loss_function
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def calculate_step_size(self, alpha=0.2, beta=0.9):
        """
        Updates the learning rate based on the backtracking algorithm

        Args:
            alpha (float): Parameter for backtracking line search. Range = (0, 0.5)
            beta (float): Parameter for backtracking line search. Range = (0, 1)

        Returns:
            float: The updated learning rate.
        """
        new_params = self.params - self.learning_rate * self.gradients
        while self.loss_function(new_params) > (
            self.loss_function(self.params)
            - alpha * self.learning_rate * np.dot(self.gradients, self.gradients)
        ):
            self.learning_rate *= beta
            new_params = self.params - self.learning_rate * self.gradients
        return self.learning_rate

    def optimize(self, gradient_function, initial_params, log_rate=100):
        self.params = np.array(initial_params, dtype=float)
        history = []
        for i in range(self.max_iterations):
            self.gradients = np.array(gradient_function(self.params), dtype=float)
            self.learning_rate = self.calculate_step_size()
            self.params = self.params - self.learning_rate * self.gradients

            if i % log_rate == 0:  # Print status every log_rate iterations
                loss = self.loss_function(self.params)
                print(f"Iteration {i}: Loss = {loss}, Params = {self.params}")
                history.append((i, loss))
                if loss < self.tolerance:
                    print(
                        f"Convergence reached --- Iteration {i}: {loss=} {self.params=}"
                    )
                    break
        return self.params, history


# Example of a multivariate loss function
def loss_function(x):
    return (x[0] - 1) ** 2 + (x[1] - 2) ** 2 + (x[0] - x[1]) ** 2


# Example of a multivariate gradient function (derivative of the loss function)
def gradient_function(x):
    return np.array(
        [2 * (x[0] - 1) + 2 * (x[0] - x[1]), 2 * (x[1] - 2) - 2 * (x[0] - x[1])]
    )


# Starting point for optimization
initial_params = [0, 0]

# Example usage of the GradientDescent class
gd = GradientDescent(loss_function, max_iterations=200)
final_params, history = gd.optimize(gradient_function, initial_params, log_rate=20)

print(f"Final parameters: {final_params}")
print(f"Final loss: {loss_function(final_params)}")

print("*" * 30)
print()


# Example loss function
def loss_function(x):
    return (x - 3) ** 2


# Example gradient function (derivative of the loss function)
def gradient_function(x):
    return 2 * (x - 3)


# Starting point for optimization
initial_params = 0

# Example usage of the GradientDescent class
gd = GradientDescent(loss_function, tolerance=1e-100, max_iterations=300)

# Any differentiable function and its gradient can be supplied
final_params, history = gd.optimize(gradient_function, initial_params, log_rate=20)

print(f"Final parameters: {final_params}")
print(f"Final loss: {loss_function(final_params)}")
