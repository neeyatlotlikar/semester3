import pandas as pd
import numpy as np


def compute_cosine_similarity(matrix):
    """
    Compute cosine similarity between rows of a matrix.

    Args:
        matrix: pandas DataFrame or numpy array where rows are items and columns are users

    Returns:
        pandas DataFrame containing the cosine similarity matrix
    """
    # Convert to numpy array if input is DataFrame
    if isinstance(matrix, pd.DataFrame):
        matrix_values = matrix.values
        index = matrix.index
    else:
        matrix_values = matrix
        index = range(matrix_values.shape[0])

    # Initialize similarity matrix
    n_items = matrix_values.shape[0]
    similarity_matrix = np.zeros((n_items, n_items))

    # Compute cosine similarity
    for i in range(n_items):
        for j in range(n_items):
            vector_i = matrix_values[i]
            vector_j = matrix_values[j]
            dot_product = np.dot(vector_i, vector_j)
            magnitude_i = np.sqrt(np.sum(vector_i**2))
            magnitude_j = np.sqrt(np.sum(vector_j**2))
            if magnitude_i == 0 or magnitude_j == 0:
                similarity_matrix[i, j] = 0
            else:
                similarity_matrix[i, j] = dot_product / (magnitude_i * magnitude_j)

    # Create DataFrame with similarity scores
    return pd.DataFrame(similarity_matrix, index=index, columns=index)


def predict_rating(user_id, item_id, item_user_matrix, similarity_df):
    """
    Predict rating for a specific user and item using weighted average of similar items.

    Args:
        user_id: ID of the target user
        item_id: ID of the target item
        item_user_matrix: DataFrame with items as rows and users as columns
        similarity_df: DataFrame with item-item similarity scores

    Returns:
        float: Predicted rating or None if prediction not possible
    """
    if item_id not in item_user_matrix.index or user_id not in item_user_matrix.columns:
        return None

    # Get items rated by the user
    rated_items = item_user_matrix[item_user_matrix[user_id] > 0].index

    if len(rated_items) == 0:
        return None

    # Get similarities between target item and rated items
    similarities = similarity_df.loc[item_id, rated_items]

    # Get ratings for these items
    ratings = item_user_matrix.loc[rated_items, user_id]

    # Calculate weighted average
    weighted_sum = np.sum(similarities * ratings)
    similarity_sum = np.sum(np.abs(similarities))

    if similarity_sum == 0:
        return None

    return weighted_sum / similarity_sum


def predict_all_unseen_ratings(user_id, item_user_matrix, similarity_df):
    """
    Predict ratings for all items not rated by the user.

    Args:
        user_id: ID of the target user
        item_user_matrix: DataFrame with items as rows and users as columns
        similarity_df: DataFrame with item-item similarity scores

    Returns:
        dict: Dictionary of item IDs to predicted ratings
    """
    if user_id not in item_user_matrix.columns:
        return {}

    # Get unrated items
    unrated_items = item_user_matrix[item_user_matrix[user_id] == 0].index

    predictions = {}
    for item_id in unrated_items:
        predicted_rating = predict_rating(
            user_id, item_id, item_user_matrix, similarity_df
        )
        if predicted_rating is not None:
            predictions[item_id] = predicted_rating

    return predictions


def recommend_top_n(user_id, item_user_matrix, similarity_df, n=3):
    """
    Recommend top-N items for a user based on predicted ratings.

    Args:
        user_id: ID of the target user
        item_user_matrix: DataFrame with items as rows and users as columns
        similarity_df: DataFrame with item-item similarity scores
        n: Number of items to recommend

    Returns:
        list: List of tuples (item_id, predicted_rating) sorted by predicted rating
    """
    predictions = predict_all_unseen_ratings(user_id, item_user_matrix, similarity_df)

    # Sort predictions by rating in descending order
    sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)

    # Return top N recommendations
    return sorted_predictions[:n]


# Example usage
if __name__ == "__main__":
    # Create sample data
    data = {
        "userId": [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5],
        "itemId": [
            101,
            102,
            103,
            101,
            104,
            105,
            101,
            102,
            103,
            104,
            102,
            103,
            105,
            101,
            104,
            105,
        ],
        "rating": [5, 3, 4, 4, 2, 5, 2, 5, 3, 4, 4, 5, 3, 3, 4, 2],
    }
    df = pd.DataFrame(data)

    # Create item-user matrix
    item_user_matrix = df.pivot_table(
        index="itemId", columns="userId", values="rating"
    ).fillna(0)

    # Compute cosine similarity
    cosine_sim_df = compute_cosine_similarity(item_user_matrix)

    # Example predictions
    target_user = 1
    target_item = 104

    # Predict rating for specific user and item
    predicted_rating = predict_rating(
        target_user, target_item, item_user_matrix, cosine_sim_df
    )
    print(
        f"Predicted rating for user {target_user} and item {target_item}: {predicted_rating:.2f}"
    )

    # Predict ratings for all unseen items
    unseen_ratings = predict_all_unseen_ratings(
        target_user, item_user_matrix, cosine_sim_df
    )
    print(f"\nPredicted ratings for unseen items for user {target_user}:")
    for item_id, rating in unseen_ratings.items():
        print(f"Item {item_id}: {rating:.2f}")

    # Recommend top-3 items
    recommendations = recommend_top_n(target_user, item_user_matrix, cosine_sim_df, n=3)
    print(f"\nTop-3 recommended items for user {target_user}:")
    for item_id, rating in recommendations:
        print(f"Item {item_id}: {rating:.2f}")
