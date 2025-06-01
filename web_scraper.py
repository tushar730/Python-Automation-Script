import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

def scrape_news(url="https://news.ycombinator.com", num_articles=10, output_dir="assets/sample_output"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate a dynamic output filename with timestamp
    output_filename = os.path.join(output_dir, f"news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

    try:
        # Set a User-Agent header to avoid being blocked by the site
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the response was unsuccessful
        
    except requests.RequestException as e:
        print(f"❌ Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.select('.titleline > a')
    if not articles:
        print("❌ No articles found on the page.")
        return

    # Prepare the data
    scraped_data = []
    for i, article in enumerate(articles[:num_articles]):
        title = article.text.strip()
        link = article['href']
        scraped_data.append((i+1, title, link))

    try:
        # Write data to CSV
        with open(output_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['#', 'Title', 'Link'])
            writer.writerows(scraped_data)
        print(f"✅ Scraped and saved top {num_articles} Hacker News headlines to {output_filename}")
    except Exception as e:
        print(f"❌ Error saving the CSV file: {e}")

if __name__ == "__main__":
    scrape_news(num_articles=10)  # Default is 10, but can be changed
