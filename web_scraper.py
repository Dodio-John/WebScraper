from bs4 import BeautifulSoup
import requests

def scrape_toscrape():
    url = 'https://toscrape.com'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.contents, 'html.parser')

        books = soup.find_all('h3')
        prices = soup.find_all('p', class_='price_color')
        ratings = soup.find_all('p', class_='star-rating')

        for book, price, rating in zip(books, prices, ratings):
            title = book.a('title')
            price_value = price.text.strip()
            rating_value = rating['class'][1]

            print(f"title: {title} | Price:  {price_value} | Rating: {rating_value}")
        else:
            print(f"Failed to retreive webpage respones {response.status_code}")

    if __name__ == '__main__':
        scrape_toscrape()
