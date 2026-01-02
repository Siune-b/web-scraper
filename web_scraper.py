import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website to scrape
url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []

for item in soup.select(".product_pod"):
    name = item.h3.a['title']
    price = item.select_one(".price_color").text
    link = item.h3.a['href']
    products.append({"Name": name, "Price": price, "Link": link})

# Save to CSV
df = pd.DataFrame(products)
df.to_csv("output/products.csv", index=False)

print("Scraping done! Check output/products.csv")
