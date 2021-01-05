import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

fileN = r"web-scraper\newsHeadlines.txt"
url = "https://www.indiatoday.in/top-stories"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
head = soup.find_all(class_ = "catagory-listing")
n = datetime.now()

if os.stat(fileN).st_size == 0:
    with open(fileN, 'w') as f:
        f.write("%s"%n)
        f.write("\n\n")
else:
    with open(fileN, 'a') as f:
        f.write("\n\n")
        f.write("%s"%n)
        f.write("\n\n")

for item in head:
    with open(fileN, 'a') as f:
        f.write(item.find("a").text)
        f.write("\n")
        f.write(item.find("p").text)
        f.write("\n\n")