import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


# Simple Feedforward Neural Network (1 hidden layer)
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, lr=0.1):
        self.lr = lr
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_deriv(self, a):
        return a * (1 - a)

    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def forward(self, X):
        self.Z1 = X @ self.W1 + self.b1
        self.A1 = self.sigmoid(self.Z1)
        self.Z2 = self.A1 @ self.W2 + self.b2
        self.A2 = self.softmax(self.Z2)
        return self.A2

    def compute_loss(self, Y_hat, Y):
        m = Y.shape[0]
        return -np.sum(Y * np.log(Y_hat + 1e-8)) / m

    def backward(self, X, Y):
        m = X.shape[0]
        dZ2 = self.A2 - Y
        dW2 = self.A1.T @ dZ2 / m
        db2 = np.sum(dZ2, axis=0, keepdims=True) / m

        dA1 = dZ2 @ self.W2.T
        dZ1 = dA1 * self.sigmoid_deriv(self.A1)
        dW1 = X.T @ dZ1 / m
        db1 = np.sum(dZ1, axis=0, keepdims=True) / m

        # Update weights
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

    def fit(self, X, Y, epochs=1000, verbose=False):
        for i in range(epochs):
            Y_hat = self.forward(X)
            loss = self.compute_loss(Y_hat, Y)
            self.backward(X, Y)
            if verbose and i % 100 == 0:
                print(f"Epoch {i}, Loss: {loss:.4f}")

    def predict(self, X):
        Y_hat = self.forward(X)
        return np.argmax(Y_hat, axis=1)


if __name__ == "__main__":
    print("Dummy Example:")
    X_dummy = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y_dummy = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])  # XOR as 2-class one-hot

    nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=2, lr=0.5)
    nn.fit(X_dummy, Y_dummy, epochs=2000, verbose=False)
    preds = nn.predict(X_dummy)
    print("Predictions:", preds)
    print("True labels:", np.argmax(Y_dummy, axis=1))

    print("\nIris Dataset Example:")
    iris = load_iris()
    X = iris.data
    y = iris.target.reshape(-1, 1)
    enc = OneHotEncoder(sparse_output=False)
    Y = enc.fit_transform(y)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    nn_iris = NeuralNetwork(input_size=4, hidden_size=8, output_size=3, lr=0.1)
    nn_iris.fit(X_train, Y_train, epochs=2000, verbose=False)
    preds = nn_iris.predict(X_test)
    true = np.argmax(Y_test, axis=1)
    acc = np.mean(preds == true)
    print(f"Test accuracy on Iris: {acc:.2f}")
