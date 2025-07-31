rating_matrix = {
    "user1": {"item1": 5, "item2": 3, "item3": 4},
    "user2": {"item1": 3, "item2": 1, "item3": 2, "item4": 3},
    "user3": {"item1": 4, "item2": 3, "item3": 4, "item4": 4},
    "user4": {"item1": 2, "item2": 2, "item3": 1, "item4": 2},
}


def pearson_correlation(user_ratings, other_user_ratings):
    """
    Calculate the Pearson correlation coefficient between two users' ratings.

    :param user_ratings: Ratings of the first user.
    :param other_user_ratings: Ratings of the second user.
    :return: Pearson correlation coefficient (similarity score between -1 and 1).
    """
    common_items = set(user_ratings.keys()) & set(other_user_ratings.keys())
    if not common_items:
        print("No common items rated by both users, returning 0 for similarity.")
        return 0

    n = len(common_items)
    mean_x = sum(user_ratings[item] for item in common_items) / n
    mean_y = sum(other_user_ratings[item] for item in common_items) / n

    numerator = sum(
        [
            (user_ratings[item] - mean_x) * (other_user_ratings[item] - mean_y)
            for item in common_items
        ]
    )

    denominator = (
        sum((user_ratings[item] - mean_x) ** 2 for item in common_items) ** 0.5
        * sum((other_user_ratings[item] - mean_y) ** 2 for item in common_items) ** 0.5
    )

    if denominator == 0:
        print("Denominator is zero, returning 0 for similarity.")
        return 0

    return numerator / denominator


def predict_rating(
    user_ratings: dict[str, float], sorted_users: list[tuple[str, float]]
):
    """
    Predict the rating a user would give to an item based on their ratings and similar users.

    :param user_ratings: Ratings of the user.
    :param item: Item for which the rating is to be predicted.
    :return: Predicted rating for the item.
    """
    recommendations = {}

    # Unrated items
    all_items = set(
        item for item_ratings in rating_matrix.values() for item in item_ratings.keys()
    )
    print(f"All items: {all_items}")
    unrated_items = set(all_items) - set(user_ratings.keys())
    print(f"Unrated items for user: {unrated_items}")

    user_items = set(user_ratings.keys())

    n = len(user_items)
    mean_x = sum(user_ratings[item] for item in user_items) / n
    sim_sum = sum(abs(sim) for _, sim in sorted_users if sim > 0)

    for similar_user, sim in sorted_users:
        if similar_user not in rating_matrix:
            continue

        item_ratings = rating_matrix[similar_user]
        mean_y = (
            sum(item_ratings[item] for item in unrated_items if item in item_ratings)
            / n
        )

        for item, item_rating in item_ratings.items():
            if item not in user_ratings and item_rating > 0:
                if item not in recommendations:
                    recommendations[item] = mean_x

                recommendations[item] += sim * (item_rating - mean_y)

    # Normalize recommendations
    for item in recommendations:
        recommendations[item] /= sim_sum if sim_sum > 0 else 1

    return recommendations


def get_user_collaborative_filter(
    user_id: str, rating_matrix: dict[str, dict[str, int]]
) -> list[tuple[str, int]]:
    """
    Get recommendations for a user based on collaborative filtering.

    :param user_id: ID of the user for whom recommendations are to be generated.
    :param rating_matrix: Dictionary containing user ratings for items.
    :return: List of recommended items.
    """
    if user_id not in rating_matrix:
        return []

    user_ratings = rating_matrix[user_id]
    similar_users = {}

    # Calculate similarity with other users
    for other_user, ratings in rating_matrix.items():
        if other_user == user_id:
            continue
        similarity = pearson_correlation(user_ratings, ratings)
        similar_users[other_user] = similarity

    # Sort similar users by similarity score, select top 2
    sorted_users = sorted(similar_users.items(), key=lambda x: x[1], reverse=True)[:2]
    print(f"Similar users for {user_id}: {sorted_users}")

    # Aggregate recommendations from similar users
    recommendations = predict_rating(user_ratings, sorted_users)

    # Sort recommendations by aggregated score
    recommended_items = sorted(
        recommendations.items(), key=lambda x: x[1], reverse=True
    )

    return recommended_items


# Example usage
if __name__ == "__main__":
    user_id = "user1"
    recommendations = get_user_collaborative_filter(user_id, rating_matrix)
    print(f"Recommendations for {user_id}: {recommendations}")
    # Output: Recommendations for user1: [('item3', 7), ('item2', 6), ('item4', 5)]
