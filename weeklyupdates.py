import requests
import pandas as pd
import time
from datetime import datetime

def scrape_new_tools():
    """Scrape new AI tools from aitoolhouse.com and add to existing dataset."""

    print(f"Starting bi-weekly scrape at {datetime.now().isoformat()}")

    # Load previous data
    try:
        existing_df = pd.read_csv("all_ai_tools_detailed.csv")
        existing_slugs = set(existing_df["Slug"].dropna().astype(str))
        print(f"Loaded {len(existing_df)} existing tools")
    except FileNotFoundError:
        existing_df = pd.DataFrame()
        existing_slugs = set()
        print("No existing data found, starting fresh")

    # Init
    new_tools = []
    url = "https://www.aitoolhouse.com/api/tool/list?page=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    page_count = 0

    while url:
        try:
            res = requests.get(url, headers=headers, timeout=15)
            res.raise_for_status()
            data = res.json()
            page_count += 1

            for tool in data["results"]:
                slug = tool.get("slug", "")

                if slug and slug not in existing_slugs:
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
                        "Created At": pd.to_datetime(tool.get("created_at", ""), errors='coerce'),
                        "Updated At": pd.to_datetime(tool.get("updated_at", ""), errors='coerce'),
                        "Rating": tool.get("average_rating", 0),
                        "Reviews": tool.get("total_reviews", 0),
                        "Image URL": tool.get("image_url", ""),
                        "Optimized Image URL": tool.get("new_image_url", ""),
                        "Social Links": ", ".join(tool.get("social_links", [])),
                    })

            url = data.get("next")
            if url:
                time.sleep(0.5)  # Rate limiting

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_count + 1}: {e}")
            # Retry once after a short delay
            time.sleep(2)
            try:
                res = requests.get(url, headers=headers, timeout=15)
                res.raise_for_status()
                data = res.json()
                url = data.get("next")
            except Exception:
                print("Retry failed, stopping scrape")
                break

    print(f"Scraped {page_count} pages")

    # Combine and save
    if new_tools:
        new_df = pd.DataFrame(new_tools)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_csv("all_ai_tools_detailed.csv", index=False)
        print(f"Added {len(new_df)} new tools. Total: {len(combined_df)} tools")
    else:
        print("No new tools found")

    print(f"Scrape completed at {datetime.now().isoformat()}")

if __name__ == "__main__":
    scrape_new_tools()
