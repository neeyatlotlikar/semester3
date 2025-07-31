import numpy as np
from itertools import repeat


# Easy-to-switch activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_deriv(x):
    s = sigmoid(x)
    return s * (1 - s)


def relu(x):
    return np.maximum(0, x)


def relu_deriv(x):
    return (x > 0).astype(float)


def tanh(x):
    return np.tanh(x)


def tanh_deriv(x):
    return 1 - np.tanh(x) ** 2


class ANN:
    def __init__(self, act="sigmoid"):
        acts = {
            "sigmoid": (sigmoid, sigmoid_deriv),
            "relu": (relu, relu_deriv),
            "tanh": (tanh, tanh_deriv),
        }
        self.activation, self.activation_deriv = acts[act]
        self.lr = 0.1
        # init random number generator
        rng = np.random.default_rng()
        # random weights init
        self.w1 = rng.standard_normal((2, 2)) * 0.1
        self.b1 = np.zeros((1, 2))
        self.w2 = rng.standard_normal((2, 1)) * 0.1
        self.b2 = np.zeros((1, 1))

    def forward(self, X):
        # input to hidden layer
        self.z1 = X @ self.w1 + self.b1
        # hidden layer activation (output)
        self.a1 = self.activation(self.z1)
        # hidden layer output to next layer
        self.z2 = self.a1 @ self.w2 + self.b2
        # output always sigmoid for binary
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, X, y):
        # Backpropagation
        output_error = y - self.a2
        output_delta = output_error * sigmoid_deriv(self.z2)  # gradient of output layer
        # Calculate hidden layer error
        hidden_error = output_delta @ self.w2.T
        hidden_delta = hidden_error * self.activation_deriv(
            self.z1
        )  # gradient of hidden layer

        # Update weights
        self.w2 += self.a1.T @ output_delta * self.lr
        self.b2 += np.sum(output_delta, axis=0, keepdims=True) * self.lr
        self.w1 += X.T @ hidden_delta * self.lr
        self.b1 += np.sum(hidden_delta, axis=0, keepdims=True) * self.lr

    def train(self, X, y, epochs=1000):
        for _ in repeat(None, epochs):
            self.forward(X)
            self.backward(X, y)

    def predict(self, X):
        return (self.forward(X) > 0.5).astype(int)


# XOR Dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

ann_sigmoid = ANN(act="sigmoid")
ann_sigmoid.train(X, Y)
ann_relu = ANN(act="relu")
ann_relu.train(X, Y)
ann_tanh = ANN(act="tanh")
ann_tanh.train(X, Y)

print("Sigmoid:", ann_sigmoid.predict(X).ravel())  # flattened output
print("ReLU:", ann_relu.predict(X).ravel())
print("Tanh:", ann_tanh.predict(X).ravel())
