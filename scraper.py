import requests
from bs4 import BeautifulSoup
import csv
import time

# Website to scrape
url = "https://blog.python.org/"

# Send request to the website
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=10)

# Check if website opened successfully
if response.status_code == 200:
    print("Website opened successfully!")

    # Convert HTML into BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headlines
    headlines = soup.find_all("h2")

    # Save headlines to CSV
    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # CSV heading
        writer.writerow(["Headline"])

        # Write each headline
        for headline in headlines:
            text = headline.get_text(strip=True)

            if text:
                writer.writerow([text])

    print("Headlines saved successfully to headlines.csv")

else:
    print("Failed to open website.")
    print("Status code:", response.status_code)

# Small delay between requests
time.sleep(2)