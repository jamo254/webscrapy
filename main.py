import pandas as pd
from bs4 import BeautifulSoup
import requests

# Arrays for storing the data
quotes = []
authors = []
tags_list = []  # Create a list to store tags for each quote separately

# Loop through multiple pages (adjust the range as needed)
for page in range(1, 10):
    url = f'http://quotes.toscrape.com/page/{page}/'
    f = requests.get(url)
    soup = BeautifulSoup(f.text, 'html.parser')

    # Extracting all quotes
    for quote in soup.find_all("div", {"class": "quote"}):
        quotes.append(quote.find("span", {"class": "text"}).text)

    # Extract all the author names within this tag
    for author in soup.find_all("div", {"class": "quote"}):
        authors.append(author.find("small", {"class": "author"}).text)

    # Extract all the tags on the page
    for meta in soup.find_all("div", {"class": "tags"}):
        tags = [tag['content'] for tag in meta.find_all("meta")]
        tags_list.append(tags)

# Create a Pandas DataFrame
finaldf = pd.DataFrame({
    'Quotes': quotes,
    'Authors': authors,
    'Tags': tags_list  # Include the list of tags for each quote
})

# Convert the list of tags to a comma-separated string
finaldf['Tags'] = finaldf['Tags'].apply(', '.join)

# Save the data to a CSV file
finaldf.to_csv('quotes.csv', index=False)

print("Data has been saved to 'quotes.csv'.")
