import numpy as np


class Perceptron:
    def __init__(self, input_size, lr=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.lr = lr
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = np.insert(x, 0, 1)  # add bias input
        summation = np.dot(self.weights, x)
        return self.activation(summation)

    def fit(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = np.insert(xi, 0, 1)  # add bias input
                output = self.activation(np.dot(self.weights, xi))
                self.weights += self.lr * (target - output) * xi


if __name__ == "__main__":
    # Logic gates data
    gates = {
        "AND": {
            "X": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
            "y": np.array([0, 0, 0, 1]),
        },
        "OR": {
            "X": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
            "y": np.array([0, 1, 1, 1]),
        },
        "NAND": {
            "X": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
            "y": np.array([1, 1, 1, 0]),
        },
        "NOR": {
            "X": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
            "y": np.array([1, 0, 0, 0]),
        },
        # XOR is not linearly separable, perceptron can't learn it
        "XOR": {
            "X": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
            "y": np.array([0, 1, 1, 0]),
        },
        "XNOR": {
            "X": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
            "y": np.array([1, 0, 0, 1]),
        },
    }

    for gate, data in gates.items():
        print(f"\nTesting {gate} gate:")
        p = Perceptron(input_size=2, lr=0.1, epochs=10)
        p.fit(data["X"], data["y"])
        for xi, target in zip(data["X"], data["y"]):
            pred = p.predict(xi)
            print(f"Input: {xi}, Predicted: {pred}, Target: {target}")
