from bs4 import BeautifulSoup
import requests
import csv

from typing import Optional, List, TextIO

# Fetch the HTML content from the website
source: str = requests.get('http://google.com').text

# Parse the HTML content using BeautifulSoup
soup: BeautifulSoup = BeautifulSoup(source, 'lxml')

# Open a CSV file for writing
csv_file: TextIO = open('cms_scrape.csv', 'w')

# Create a CSV writer object and write the header row
csv_writer: csv.writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

# Iterate through each article on the website
for article in soup.find_all('article'):
    # Extract the headline of the article
    headline: str = article.h2.a.text
    print(headline)

    # Extract the summary of the article
    summary_div: Optional[BeautifulSoup] = article.find('div', class_='entry-content')
    summary: str = summary_div.p.text if summary_div and summary_div.p else ""
    print(summary)

    # Extract the YouTube video link if available
    try:
        vid_src: str = article.find('iframe', class_='youtube-player')['src']
        vid_id: str = vid_src.split('/')[4].split('?')[0]
        yt_link: str = f'https://youtube.com/watch?v={vid_id}'
    except (KeyError, IndexError, TypeError):
        # Set yt_link to None if no video link is found
        yt_link: Optional[str] = None

    print(yt_link)
    print()

    # Write the extracted data to the CSV file
    csv_writer.writerow([headline, summary, yt_link])

# Close the CSV file
csv_file.close()

