import numpy as np

# ----- Toy training data -----
text = "hellohello"
chars = sorted(list(set(text)))
vocab_size = len(chars)

char_to_idx = {ch: i for i, ch in enumerate(chars)}
idx_to_char = {i: ch for ch, i in char_to_idx.items()}


def one_hot(idx, size):
    v = np.zeros((size, 1))
    v[idx] = 1.0
    return v


# Convert text to indices
data = [char_to_idx[c] for c in text]

# ----- RNN hyperparameters -----
input_size = vocab_size  # one-hot size
hidden_size = 8  # small hidden layer
output_size = vocab_size
learning_rate = 0.1

# ----- Parameter initialization -----
np.random.seed(0)
W_xh = np.random.randn(hidden_size, input_size) * 0.1
W_hh = np.random.randn(hidden_size, hidden_size) * 0.1
b_h = np.zeros((hidden_size, 1))

W_hy = np.random.randn(output_size, hidden_size) * 0.1
b_y = np.zeros((output_size, 1))


def softmax(z):
    e = np.exp(z - np.max(z))
    return e / np.sum(e)


# ----- One training step over the whole sequence -----
def rnn_step_through_sequence(data, targets, h_prev):
    xs, hs, ys, ps = {}, {}, {}, {}
    hs[-1] = h_prev
    loss = 0.0

    # Forward pass
    for t in range(len(data)):
        xs[t] = one_hot(data[t], input_size)
        hs[t] = np.tanh(W_xh @ xs[t] + W_hh @ hs[t - 1] + b_h)
        ys[t] = W_hy @ hs[t] + b_y
        ps[t] = softmax(ys[t])
        loss -= np.log(ps[t][targets[t], 0] + 1e-12)

    # Backward pass (compute gradients)
    dW_xh = np.zeros_like(W_xh)
    dW_hh = np.zeros_like(W_hh)
    db_h = np.zeros_like(b_h)
    dW_hy = np.zeros_like(W_hy)
    db_y = np.zeros_like(b_y)
    dh_next = np.zeros_like(hs[0])

    for t in reversed(range(len(data))):
        dy = np.copy(ps[t])
        dy[targets[t]] -= 1.0  # derivative of cross-entropy loss
        dW_hy += dy @ hs[t].T
        db_y += dy

        dh = W_hy.T @ dy + dh_next  # backprop into h
        dh_raw = (1 - hs[t] * hs[t]) * dh  # tanh'
        db_h += dh_raw
        dW_xh += dh_raw @ xs[t].T
        dW_hh += dh_raw @ hs[t - 1].T
        dh_next = W_hh.T @ dh_raw

    # Clip gradients to avoid exploding gradients in this toy example
    for dparam in [dW_xh, dW_hh, db_h, dW_hy, db_y]:
        np.clip(dparam, -5, 5, out=dparam)

    return loss, dW_xh, dW_hh, db_h, dW_hy, db_y, hs[len(data) - 1]


# ----- Training loop -----
h_prev = np.zeros((hidden_size, 1))

for epoch in range(200):
    # For simplicity, target is "next character", with last predicting first
    inputs = data
    targets = data[1:] + [data[0]]

    loss, dW_xh, dW_hh, db_h, dW_hy, db_y, h_prev = rnn_step_through_sequence(
        inputs, targets, h_prev
    )

    # SGD parameter update
    W_xh -= learning_rate * dW_xh
    W_hh -= learning_rate * dW_hh
    b_h -= learning_rate * db_h
    W_hy -= learning_rate * dW_hy
    b_y -= learning_rate * db_y

    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch + 1}, loss = {loss:.3f}")


# ----- Sampling: generate characters -----
def sample(h, start_idx, length=10):
    idx = start_idx
    output = []
    for _ in range(length):
        x = one_hot(idx, input_size)
        h = np.tanh(W_xh @ x + W_hh @ h + b_h)
        y = W_hy @ h + b_y
        p = softmax(y)
        idx = np.random.choice(range(vocab_size), p=p.ravel())
        output.append(idx_to_char[idx])
    return "".join(output)


print("\nGenerated sequence:")
print(sample(np.zeros((hidden_size, 1)), char_to_idx["h"], length=20))
