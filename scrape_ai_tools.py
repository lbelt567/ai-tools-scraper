import requests
import pandas as pd
import time

tools = []
url = "https://www.aitoolhouse.com/api/tool/list?page=1"
headers = {"User-Agent": "Mozilla/5.0"}

while url:
    print(f"Fetching: {url}")
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        data = res.json()

        for tool in data["results"]:
            tools.append({
                "Name": tool.get("name", ""),
                "Slug": tool.get("slug", ""),
                "Homepage": tool.get("homepage_url", ""),
                "Short Description": tool.get("short_description", ""),
                "Price Text": tool.get("price_text", ""),
                "Pricing": ", ".join(tool.get("pricing", [])),
                "Features": ", ".join(tool.get("features", [])),
                "Categories": ", ".join(tool.get("subcategories", [])),
                "Verified": tool.get("verified", False),
                "Favorite Count": tool.get("favorite_count", 0),
                "Created At": tool.get("created_at", ""),
                "Updated At": tool.get("updated_at", ""),
                "Rating": tool.get("average_rating", 0),
                "Reviews": tool.get("total_reviews", 0),
                "Image URL": tool.get("image_url", ""),
                "Optimized Image URL": tool.get("new_image_url", ""),
                "Social Links": ", ".join(tool.get("social_links", [])),
            })

        url = data.get("next")
        time.sleep(0.7)

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        break

df = pd.DataFrame(tools)
df.to_csv("all_ai_tools_detailed.csv", index=False)
print(f"\n✅ Done. {len(df)} tools saved to all_ai_tools_detailed.csv")
