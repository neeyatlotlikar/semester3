import pandas as pd


def pearson_correlation(user_ratings, other_user_ratings):
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


def predict_rating(user_ratings, sorted_users):
    recommendations = {}

    # Unrated items
    all_items = set(
        item.strip() for item_ratings in rating_matrix.values() for item in item_ratings.keys()
    )
    # print(f"All items: {all_items}")
    unrated_items = set(all_items)  # Calculate for all items
    # print(f"Unrated items for user: {unrated_items}")

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
            # if item not in user_ratings and item_rating > 0:
                if item not in recommendations:
                    recommendations[item] = mean_x

                recommendations[item] += sim * (item_rating - mean_y)

    # Normalize recommendations
    for item in recommendations:
        recommendations[item] /= sim_sum if sim_sum > 0 else 1

    # print(f"predict_rating {recommendations=}")
    return recommendations


def get_user_collaborative_filter(user_id, rating_matrix):
    if user_id not in rating_matrix:
        return []

    user_ratings = rating_matrix[user_id]
    similar_users = {}

    for other_user, ratings in rating_matrix.items():
        if other_user == user_id:
            continue
        similarity = pearson_correlation(user_ratings, ratings)
        similar_users[other_user] = similarity

    sorted_users = sorted(similar_users.items(), key=lambda x: x[1], reverse=True)[:3] # top 3
    print(f"Similar users for {user_id}: {sorted_users}\n")

    recommendations = predict_rating(user_ratings, sorted_users)

    recommended_items = sorted(
        recommendations.items(), key=lambda x: x[1], reverse=True
    )

    print("All Collaborative Filtering recommendations:")
    for item in recommended_items:
        print(item[0].strip(), item[1])
    print()

    return recommended_items


def modify_recomm_list(content_rec, recs):
    new_rec = content_rec
    if recs:
        # print("Final", recs)
        new_rec = [(item[0].strip(), item[1]) for item in recs if item[0].strip() in content_rec]
    return new_rec


if __name__ == "__main__":

    df = pd.read_csv("SEA/user_item_rank_matrix.csv", index_col=0)
    rating_matrix = df.transpose().to_dict()

    content_rec = "A C E H J".split()
    user_id = "John"

    cf_rec = get_user_collaborative_filter(user_id, rating_matrix)
    final_rec = modify_recomm_list(content_rec, cf_rec)

    # print(f"{cf_rec}=")
    print("Content Based Recommendation list:", content_rec, "\n")
    print(f"Recommendations for {user_id}: {final_rec}")

