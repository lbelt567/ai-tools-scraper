import pandas as pd
import re

def clean_scraped_data(input_file="all_ai_tools_detailed.csv", output_file="all_ai_tools_cleaned.csv"):
    """
    Transform scraped AI tools data into the format expected by the chatbot backend.

    Removes unnecessary columns and simplifies date format.
    """
    print(f"Loading {input_file}...")
    df = pd.read_csv(input_file)
    print(f"Loaded {len(df)} tools")

    # Select only the columns needed for the backend
    columns_to_keep = [
        "Name",
        "Slug",
        "Homepage",
        "Short Description",
        "Price Text",
        "Pricing",
        "Categories",
        "Verified",
        "Favorite Count",
        "Updated At"
    ]

    df_cleaned = df[columns_to_keep].copy()

    # Simplify Updated At to just the date (YYYY-MM-DD)
    df_cleaned["Updated At"] = pd.to_datetime(df_cleaned["Updated At"], errors='coerce').dt.strftime('%Y-%m-%d')

    # Clean Homepage URLs - remove UTM parameters for cleaner display
    def clean_url(url):
        if pd.isna(url):
            return url
        # Remove UTM parameters
        return re.sub(r'\?utm_[^&]*(&utm_[^&]*)*', '', str(url))

    df_cleaned["Homepage"] = df_cleaned["Homepage"].apply(clean_url)

    # Save cleaned data
    df_cleaned.to_csv(output_file, index=False)
    print(f"Saved {len(df_cleaned)} tools to {output_file}")

    return df_cleaned

if __name__ == "__main__":
    clean_scraped_data()
