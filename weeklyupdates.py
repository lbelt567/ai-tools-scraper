import requests
import pandas as pd
import time
from datetime import datetime

# Load previous data
try:
    existing_df = pd.read_csv("all_ai_tools_detailed.csv")
    existing_slugs = set(existing_df["Slug"].dropna().astype(str))
except FileNotFoundError:
    existing_df = pd.DataFrame()
    existing_slugs = set()

# Init
new_tools = []
url = "https://www.aitoolhouse.com/api/tool/list?page=1"
headers = {"User-Agent": "Mozilla/5.0"}

while url:
    res = requests.get(url, headers=headers, timeout=10)
    data = res.json()

    for tool in data["results"]:
        slug = tool.get("slug", "")
        created = pd.to_datetime(tool.get("created_at", ""), errors='coerce')

        if slug not in existing_slugs:
            new_tools.append({
                "Name": tool.get("name", ""),
                "Slug": slug,
                "Homepage": tool.get("homepage_url", ""),
                "Short Description": tool.get("short_description", ""),
                "Price Text": tool.get("price_text", ""),
                "Pricing": ", ".join(tool.get("pricing", [])),
                "Features": ", ".join(tool.get("features", [])),
                "Categories": ", ".join(tool.get("subcategories", [])),
                "Verified": tool.get("verified", False),
                "Favorite Count": tool.get("favorite_count", 0),
                "Created At": created,
                "Updated At": pd.to_datetime(tool.get("updated_at", ""), errors='coerce'),
                "Rating": tool.get("average_rating", 0),
                "Reviews": tool.get("total_reviews", 0),
                "Image URL": tool.get("image_url", ""),
                "Optimized Image URL": tool.get("new_image_url", ""),
                "Social Links": ", ".join(tool.get("social_links", [])),
            })
        else:
            continue  # Already scraped, skip

    url = data.get("next")
    time.sleep(0.5)

# Combine and save
if new_tools:
    new_df = pd.DataFrame(new_tools)
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.to_csv("all_ai_tools_detailed.csv", index=False)
    print(f"✅ Added {len(new_df)} new tools.")
else:
    print("✅ No new tools found.")
