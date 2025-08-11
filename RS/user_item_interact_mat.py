import pandas as pd
from collections import defaultdict, Counter

# Dataset (purchase logs)
purchase_history = [
    ("John", ["Milk", "Bread", "Napkin", "Butter", "Table salt"]),
    ("Mary", ["Lipstick", "Facewash", "Hair color", "Nail polish", "Bread"]),
    ("Ram", ["Rice", "Sugar", "Garam masala", "potato", "onion"]),
    ("Raj", ["Tea", "Milk", "wafers", "Chips", "nuts"]),
    ("Gita", ["Tomato", "Onion", "Cooking Oil", "Tur dal", "sugar"]),
    ("Raj", ["Bread", "Chips", "Sauce", "Pepsi", "Milk"]),
    ("Mary", ["Talcum Powder", "Fair & Lovely", "Nail cutter", "Ribbons", "Napkin"]),
    ("John", ["Onion", "Tea", "Milk", "Butter", "jam"]),
    ("Ram", ["Tur dal", "Tamarind", "Sugar", "pumpkin", "Milk"]),
    ("Raj", ["Noodles", "chips", "nuts", "wafers", "Tomato"]),
    ("Gita", ["Milk Powder", "Bread", "Napkin", "Butter", "Milk", "Table salt"]),
    ("Mary", ["Ribbon", "Body Wash", "Liquid Soap", "Nail polish", "Floor Cleaner"]),
    ("Ram", ["Cake", "Floor Cleaner", "Garam masala", "potato", "onion"]),
    ("Raj", ["Tea", "Milk", "wafers", "Chips", "nuts"]),
    ("John", ["Tomato", "Onion", "Floor Cleaner", "Tur dal", "sugar"]),
    ("Raj", ["Bread", "Chips", "Sauce", "Pepsi", "Milk"]),
    ("Gita", ["Talcum Powder", "Fair & Lovely", "grapes", "Apple", "Napkin"]),
    ("John", ["Onion", "Floor Cleaner", "Milk", "Butter", "jam"]),
    ("Mary", ["Tur dal", "Tamarind", "Sugar", "pumpkin", "Milk"]),
    ("Gita", ["Noodles", "chips", "nuts", "wafers", "Tomato"]),
    ("Raj", ["Apple", "Milk", "wafers", "Chips", "nuts"]),
    ("John", ["grapes", "Onion", "Cooking Oil", "Tur dal", "sugar"]),
    ("Gita", ["Apple", "Chips", "Sauce", "Pepsi", "Milk"]),
    ("Ram", ["Fair & Lovely", "Talcum Powder", "Nail cutter", "Ribbons", "Napkin"]),
    ("John", ["Onion", "Tea", "Milk", "Butter", "jam"]),
    ("Mary", ["Tur dal", "Floor Cleaner", "Sugar", "grapes", "Milk"]),
    ("Raj", ["Noodles", "chips", "nuts", "wafers", "Tomato"]),
    ("Raj", ["Tea", "Milk", "wafers", "Chips", "nuts"]),
    ("John", ["Tomato", "Floor Cleaner", "Cooking Oil", "Tur dal", "sugar"]),
    ("Mary", ["Tur dal", "Tamarind", "Sugar", "pumpkin", "Apple"]),
]

# Count item popularity
all_items = [item for _, items in purchase_history for item in items]
item_counts = Counter(all_items)
top_10_items = [item for item, _ in item_counts.most_common(10)]

#  Build user-item frequency table
user_item_freq = defaultdict(lambda: defaultdict(int))

for user, items in purchase_history:
    for item in items:
        if item in top_10_items:
            user_item_freq[user][item] += 1

# Convert frequency to ratings (cap at 5)
user_item_matrix = pd.DataFrame(
    index=tuple(set([u for u, _ in purchase_history])), columns=top_10_items
)

for user in user_item_matrix.index:
    for item in top_10_items:
        freq = user_item_freq[user][item]
        user_item_matrix.loc[user, item] = min(freq, 5) if freq > 0 else 0

user_item_matrix = user_item_matrix.fillna(0).astype(int)

print("Top 10 Items:", top_10_items)
print("\nUser-Item Interaction Matrix:")
print(user_item_matrix)
