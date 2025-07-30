# ai-tools-scraper
# 🧠 AI Toolhouse Scraper

This Python script scrapes 3,800+ ai tools and saves the data into a structured CSV file.

It includes detailed information like name, pricing, features, social links, categories, and more — ideal for use in AI dashboards, recommender systems, or discovery tools.

---

## 📦 Output

- `all_ai_tools_detailed.csv`:  
  Contains a structured list of all AI tools with metadata including:
  - Tool name
  - Category
  - Pricing
  - Image URLs
  - Features
  - Social links
  - Creation & update timestamps

---

## 📝 Sample Fields

| Field               | Description                                  |
|--------------------|----------------------------------------------|
| `Name`             | Name of the AI tool                          |
| `Slug`             | URL-friendly identifier                      |
| `Homepage`         | Link to the tool’s main site                 |
| `Short Description`| Summary of the tool                          |
| `Pricing`          | Free / Freemium / Paid                       |
| `Features`         | List of available features                   |
| `Categories`       | Functional tags like "copywriting", etc.     |
| `Image URL`        | Tool image/logo                              |
| `Social Links`     | GitHub, Twitter, LinkedIn, etc.              |
| `Verified`         | Whether the tool is marked official          |
| `Created / Updated`| Timestamps from the API                      |

---

## 🚀 How to Run

Clone this repo and run the script:

```bash
git clone git@github.com:lbelt567/ai-tools-scraper.git
cd ai-tools-scraper

pip install requests pandas
python scrape_ai_tools.py
The script will paginate through the full API and export a CSV file.

📊 Example Use Cases
🧭 AI discovery dashboards

📈 Trend analysis across categories

🤖 Input for chatbots or recommender systems

💼 Market research & product discovery

⚠️ Disclaimer
This project is for educational and non-commercial use only.
All data is publicly available and collected respectfully in compliance with GitHub and aitoolhouse.com guidelines.
