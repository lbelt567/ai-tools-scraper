import pandas as pd

# Load your data
df = pd.read_csv("all_ai_tools_detailed.csv")

# Convert date columns to datetime objects
df["Created At"] = pd.to_datetime(df["Created At"], errors='coerce')
df["Updated At"] = pd.to_datetime(df["Updated At"], errors='coerce')


sorted_df = df.sort_values(by="Updated At", ascending=False)
print(sorted_df[["Name","Updated At"]].head(20))

