import requests
from bs4 import BeautifulSoup

url = "https://www.booking.com/hotel/pl/happy-tower.uk.html"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select('li.review_list_new_item_block')
print(len(reviews))