import os
import pandas as pd
from bs4 import BeautifulSoup
import requests

data = requests.get('https://livingcost.org/')
soup = BeautifulSoup(data.text, 'html.parser')

# Extracting all countries
country_names = []

# The country names are in a table with class "table" and th elements inside
for table in soup.find_all("table", {"class": "table"}):
    for th in table.find_all("th", {'class': "cost-country"}):
        country_name = th.text.strip()
        country_names.append(country_name)

# Now you can print or process the extracted country names
for country_name in country_names:
    print(country_name)

# If you want to save the data to a CSV file using Pandas, you can do it like this:
# df = pd.DataFrame({'Country': country_names})
# df.to_csv("country_names.csv", index=False)




# Extracting cost of living data for all countries
country_data = []

# The cost of living data is inside a table with class "table-cost-of-living"
for table in soup.find_all("table", {"class": "table"}):
    # Extract the header row for column names
    header_row = table.find("tr")
    column_names = [th.text.strip() for th in header_row.find_all("th")]

    # Extract data rows for each country
    for data_row in table.find_all("tr")[1:]:  # Skip the header row
        country_values = [td.text.strip() for td in data_row.find_all("td")]
        country_data.append(dict(zip(column_names, country_values)))

# Now you can print or process the extracted cost of living data
for country in country_data:
    print(country)
    
    

# Extract all cities
city_names_populations = []

for order_list in soup.find_all("ol", {"class": "row"}):
    for li in order_list.find_all("h3", {"class": "geo-head-text"}):
        # Get the first part (city name)
        city_name = li.text.strip().split('<small>')[0]
        city_names_populations.append(city_name)
for city in city_names_populations:
    print("Cities",city)
    
    
# Extract all cities and populations
city_names_populations = []

for order_list in soup.find_all("ol", {"class": "row"}):
    for li in order_list.find_all("li", {"class": "col-6"}):
        city_name = li.text.strip()
        city_names_populations.append(city_name)
        
   
test_df = pd.DataFrame({
     'City Data': city_names_populations
 })
 
print(test_df.head())


# Create Pandas DataFrames for each data type
country_df = pd.DataFrame({'Country': country_names})
country_data_df = pd.DataFrame(country_data)
city_population_df = pd.DataFrame({'City Data': city_names_populations})

# Combine all data into a single DataFrame
combined_data_df = pd.concat([country_df, country_data_df, city_population_df], axis=1)

# Save the combined data to a CSV file
combined_data_df.to_csv("combined_data.csv", index=False)

print("Data has been saved to combined_data.csv")


# Send an HTTP request to the specific URL
url = 'https://livingcost.org/cost/russia/saint-petersburg'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the cost of living data
    cost_of_living = []

    # The data is typically organized in a table with class "table-cost-of-living"
    table = soup.find("table", class_="table-cost-of-living")

    if table:
        rows = table.find_all("tr")

        for row in rows[1:]:  # Skip the header row
            columns = row.find_all("td")

            if len(columns) >= 2:
                item = columns[0].text.strip()
                cost = columns[1].text.strip()
                cost_of_living.append((item, cost))

        # Print or process the cost of living data
        for item, cost in cost_of_living:
            print(f"{item}: {cost}")
    else:
        print("No cost of living data found on the page.")
else:
    print(f"Failed to retrieve data from URL: {url}")





