from bs4 import BeautifulSoup
import requests
import time

url = input("Paste newegg url to scrape here: ")

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

product = doc.find_all("h1")[0]
product_name = product.string
product_brand = product_name[0:40]

prices = doc.find_all(text="£")
parent = prices[0].parent
strong = parent.find("strong")
product_price = strong.string

print("Starting product scrape...")


with open("productPrices.txt", "a") as f:
    f.write("\n")
    f.write("\n")
    f.write(product_brand)
    f.write(f"\nThe price is #{product_price}")

time.sleep(2)

print("Product name and price written to txt file...")