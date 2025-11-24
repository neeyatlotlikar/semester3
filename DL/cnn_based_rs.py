import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.metrics.pairwise import cosine_similarity

# Load MNIST dataset (using only images)
(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train[:1000]  # Small subset for speed
x_test = x_test[:10]  # Only a few queries for fast demo

# Normalize and add channel dimension
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

# Define a simple CNN model to extract features
cnn = models.Sequential(
    [
        layers.Conv2D(16, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D(),
        layers.Conv2D(32, (3, 3), activation="relu"),
        layers.Flatten(),
        layers.Dense(32, activation="relu"),  # 32-dim feature embedding
    ]
)

# Extract features
train_features = cnn.predict(x_train, verbose=0)
test_features = cnn.predict(x_test, verbose=0)


# Recommend similar items for each test image using cosine similarity in feature space
def recommend(query_feat, all_feats, top_k=3):
    sims = cosine_similarity([query_feat], all_feats)[0]
    # Get indices of top_k highest similarities
    top_indices = sims.argsort()[-top_k:][::-1]
    return top_indices, sims[top_indices]


for i, test_feat in enumerate(test_features):
    idxs, sims = recommend(test_feat, train_features)
    print(
        f"Test Item {i}: Recommended training images (indices): {idxs}, Similarities: {sims.round(4)}"
    )

print("Program executed successfully!")
