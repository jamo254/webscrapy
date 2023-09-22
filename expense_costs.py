import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://livingcost.org"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant data on the page using BeautifulSoup methods
    # Extract country data, table data, or other information as needed

    # Example: Extracting all country names
    country_names = []
    country_elements = soup.find_all("div", {"class": "country-row"})
    for country_element in country_elements:
        country_name = country_element.find(
            "div", {"class": "country-name"}).text.strip()
        country_names.append(country_name)

    # Now, you can process and store the data as needed (e.g., in a DataFrame or CSV)

    # Example: Print the extracted country names
    for country_name in country_names:
        print(country_name)

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
