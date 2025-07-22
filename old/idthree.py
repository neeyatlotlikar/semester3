import pandas as pd
import numpy as np


def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy_val = -np.sum(
        [
            (counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts))
            for i in range(len(elements))
        ]
    )
    return entropy_val


def info_gain(data, split_attribute_name, target_name="label"):
    total_entropy = entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)

    weighted_entropy = np.sum(
        [
            (counts[i] / np.sum(counts))
            * entropy(
                data.where(data[split_attribute_name] == vals[i]).dropna()[target_name]
            )
            for i in range(len(vals))
        ]
    )
    gain = total_entropy - weighted_entropy
    return gain


def id3(data, originaldata, features, target_attribute_name, parent_node_class=None):
    # if only one class remains, return it
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]

    # if no features remain, return the majority class
    elif len(features) == 0:
        return np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])
        ]

    # if data is empty, return majority class of original data
    elif len(data) == 0:
        return np.unique(originaldata[target_attribute_name])[
            np.argmax(
                np.unique(originaldata[target_attribute_name], return_counts=True)[1]
            )
        ]

    # majority class of current data
    else:
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])
        ]

    item_values = [
        info_gain(data, feature, target_attribute_name) for feature in features
    ]
    best_feature_index = np.argmax(item_values)
    best_feature = features[best_feature_index]

    tree = {best_feature: {}}

    features = [i for i in features if i != best_feature]

    for value in np.unique(data[best_feature]):
        sub_data = data.where(data[best_feature] == value).dropna()
        subtree = id3(
            sub_data, data, features, target_attribute_name, parent_node_class
        )
        tree[best_feature][value] = subtree

    return tree


def predict(instance, tree):
    if not isinstance(tree, dict):
        return tree  # leaf node

    root = next(iter(tree))  # Get the current feature to split on
    feature_value = instance.get(root)

    if feature_value in tree[root]:
        return predict(instance, tree[root][feature_value])
    else:
        return None


if __name__ == "__main__":
    df = pd.read_csv("customer_restaurant.csv")
    # print(df)
    # print(df.dtypes)

    features = list(df.columns)
    # print(features)
    target = "WAIT"
    features.remove(target)
    features.remove("Sample")

    col_mapping = dict()
    for col in df.columns:
        if df[col].dtype == "object":
            tmp = df[col].astype("category")
            col_mapping[col] = dict(enumerate(tmp.cat.categories))
            df[col] = df[col].astype("category").cat.codes

    tree = id3(df, df, features, target_attribute_name=target)
    print("Decision Tree:\n", tree)

    print(f"{col_mapping=}")

    # Test unseen data
    new_data = pd.read_csv("test_data.csv")

    predictions = predict(new_data, tree)
    print(f"{predictions=}")
