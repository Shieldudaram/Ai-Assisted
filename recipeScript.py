import requests
from bs4 import BeautifulSoup

# Define the URL of the website to search
url = "https://www.google.com/search?q=sourdough+bread+recipe"

# Send the HTTP request and parse the HTML response
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the relevant links for the recipe
links = soup.find_all('a', href=True)

# Loop through each link and check if it's a recipe page
for link in links:
    if "sourdough bread" in link["href"]:
        # If it is, print out the URL of the recipe page
        print(link["href"])
