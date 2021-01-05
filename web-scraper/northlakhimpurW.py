import requests
import re
from bs4 import BeautifulSoup

#url = "https://www.theweathernetwork.com/in/weather/assam/north-lakhimpur"
#url = "https://www.timeanddate.com/weather/india/north-lakhimpur/ext"
url = "https://www.skymetweather.com/forecast/weather/india/assam/lakhimpur/north%20lakhimpur"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
days = soup.find(class_="seveldayforecast")



print(days)