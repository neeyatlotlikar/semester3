import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

transactions = [
    ['Milk', 'Bread', 'Napkin', 'Butter', 'Table salt'],
    ['Lipstick', 'Facewash', 'Hair color', 'Nail polish', 'Bread'],
    ['Rice', 'Sugar', 'Garam masala', 'potato', 'onion'],
    ['Tea', 'Milk', 'wafers', 'Chips', 'nuts'],
    ['Tomato', 'Onion', 'Cooking Oil', 'Tur dal', 'sugar'],
    ['Bread', 'Chips', 'Sauce', 'Pepsi', 'Milk'],
    ['Talcum Powder', 'Fair Lovely', 'Nail cutter', 'Ribbons', 'Napkin'],
    ['Onion', 'Tea', 'Milk', 'Butter', 'jam'],
    ['Tur dal', 'Tamarind', 'Sugar', 'pumpkin', 'Milk'],
    ['Noodles', 'chips', 'nuts', 'wafers', 'Tomato'],
    ['Milk Powder', 'Bread', 'Napkin', 'Butter', 'Milk', 'Table salt'],
    ['Ribbon', 'Body Wash', 'Liquid Soap', 'Nail polish', 'Floor Cleaner'],
    ['Cake', 'Floor Cleaner', 'Garam masala', 'potato', 'onion'],
    ['Tea', 'Milk', 'wafers', 'Chips', 'nuts'],
    ['Tomato', 'Onion', 'Floor Cleaner', 'Tur dal', 'sugar'],
    ['Bread', 'Chips', 'Sauce', 'Pepsi', 'Milk'],
    ['Talcum Powder', 'Fair Lovely', 'grapes', 'Apple', 'Napkin'],
    ['Onion', 'Floor Cleaner', 'Milk', 'Butter', 'jam'],
    ['Tur dal', 'Tamarind', 'Sugar', 'pumpkin', 'Milk'],
    ['Noodles', 'chips', 'nuts', 'wafers', 'Tomato'],
    ['Apple', 'Milk', 'wafers', 'Chips', 'nuts'],
    ['grapes', 'Onion', 'Cooking Oil', 'Tur dal', 'sugar'],
    ['Apple', 'Chips', 'Sauce', 'Pepsi', 'Milk'],
    ['Fair Lovely', 'Talcum Powder', 'Nail cutter', 'Ribbons', 'Napkin'],
    ['Onion', 'Tea', 'Milk', 'Butter', 'jam'],
    ['Tur dal', 'Floor Cleaner', 'Sugar', 'grapes', 'Milk'],
    ['Noodles', 'chips', 'nuts', 'wafers', 'Tomato'],
    ['Tea', 'Milk', 'wafers', 'Chips', 'nuts'],
    ['Tomato', 'Floor Cleaner', 'Cooking Oil', 'Tur dal', 'sugar'],
    ['Tur dal', 'Tamarind', 'Sugar', 'pumpkin', 'Apple']
]

print(f"📦 Loaded {len(transactions)} transactions [file:1]")

# Step 1: One-hot encoding
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(f"🔢 One-hot shape: {df.shape}")

# Step 2: Apriori (min_support=0.2 per experiment)
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)
print(f"\n🛒 Frequent itemsets: {len(frequent_itemsets)}")
print(frequent_itemsets.head())

# Step 3: Association rules (lift >= 1.0 per experiment)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print(f"\n⚖️  Rules (lift≥1.0): {len(rules)}")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].round(3).head())

# Step 4: Recommendation engine (Bread example from PDF)
def recommend_items(item, rules_df, top_n=3):
    item_rules = rules_df[rules_df['antecedents'].apply(lambda x: item in x)]
    if item_rules.empty:
        return [f"No rules for '{item}'"]
    
    item_rules = item_rules.sort_values(['confidence', 'lift'], ascending=False)
    recs = []
    for idx, row in item_rules.head(top_n).iterrows():
        for consec in row['consequents']:
            if consec != item and consec not in recs:
                recs.append(consec)
    return recs[:top_n]

# 🎯 EXPERIMENT DELIVERABLE
bread_recs = recommend_items('Bread', rules)
print(f"\n🏆 Bread → {bread_recs} [file:1]")

