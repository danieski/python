from unittest import result
import requests
from bs4 import BeautifulSoup



url='https://www.goldenpages.ie/q/business/advanced/what/credit%20union/'

result = requests.get(url)
content = result.text

soup = BeautifulSoup(content, 'lxml')

for result in soup.find_all('a', class_="listing_title_link"):
	result.get_text()
	mediaurl = result.get('href')
	enteraurl = "https://www.goldenpages.ie" + mediaurl
    result = requests.get(enteraurl)


#box = soup.find_all('div', class_='listing_content')
#title = box('a', class_= "listing_title_link").get_text()
#phone = box('a', class_="link_listing_number").get_text()
#print(phone)
#print("Phone number:%s" %phone)
