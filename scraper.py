import requests
from bs4 import BeautifulSoup
for a in range(1,2):

    url='https://www.goldenpages.ie/q/business/advanced/what/credit%20union/'
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    container = soup.find_all('div', class_='listing_container')
    phone = soup.find_all('a', class_='link_listing_number')

    for i in container:
	    title = i.find('a', class_='listing_title_link')
	    print (title.text)
	    phone = i.find('a', class_='link_listing_number')
	    print ('Phone:', phone.text)
	    address = i.find('div', class_='listing_address')
	    print ('Address:', address.text)
	
