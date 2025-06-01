# 🤖 Python Automation Script

A collection of Python scripts to automate common tasks like organizing files, sending emails, and scraping websites. Great for learning and real-world usage!

---

## 📦 Contents

| Script            | Description                              |
|-------------------|------------------------------------------|
| `file_organizer.py` | Organizes files in folders by file type |
| `email_sender.py`   | Sends automated emails via SMTP         |
| `web_scraper.py`    | Scrapes top headlines from Hacker News  |

---

## 🚀 How to Use

### 1. Create a virtual environment (optional but recommended)



Install dependencies
  pip install -r requirements.txt

🔧 Scripts Overview & Usage
📁 1. file_organizer.py
Purpose: Automatically organize files in a folder by file type (e.g., .pdf, .jpg, .txt).

✅ How to Use
  python file_organizer.py "path_to_folder"
  
This script will create subfolders like Images, Documents, Archives, and move the files accordingly.

📧 2. email_sender.py

Purpose: Send emails using Gmail SMTP with support for:

Plain text or HTML body

CC, BCC

File attachments

✅ How to Use
  python email_sender.py recipient@example.com "Subject" "Body text" [--html] [--cc email] [--bcc email] [--attachments file1 file2]

Gmail Configuration:

Enable 2-Step Verification for your Google account.

Go to Google App Passwords and generate one for "Mail".

Create a .env file in the project root:
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password

🌐 3. web_scraper.py

Purpose: Scrape the top 10 (or more) articles from Hacker News and save them to CSV.

✅ How to Use
  python web_scraper.py
  
Optional Parameters
You can customize the number of articles and output folder by modifying the default values in the script:
  scrape_news(num_articles=20, output_dir="assets/sample_output")
Output: CSV files are saved in the assets/sample_output/ folder with timestamps (e.g., news_20250601_214020.csv).

📋 Requirements

The required libraries are listed in requirements.txt:
  requests
  beautifulsoup4
  python-dotenv

Install all dependencies with:
  pip install -r requirements.txt
  
🧪 Test It All
Test each script individually or run them all to automate your local environment, communicate via email, and scrape news data in one workflow.
