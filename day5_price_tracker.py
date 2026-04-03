import requests
from bs4 import BeautifulSoup
import time

def track_price(url, target_price):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }   

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')  

        # price_element = soup.find("p", class_="price_color")
        # if price_element:
        #     price_text = price_element.get_text().strip()
        #     print(f'Extracted price text: "{price_text}"')
        #     print('============================================')
        #     # price_str = price_text.removeprefix('£').replace(',', '')
        #     price_str = price_text[2:]
        #     print(f'Cleaned price string: "{price_str}"')
        #     price = float(price_str)
        #     print(f'Initial price: ${price}')     
        #     if price <= target_price:
        #         print(f'Price is already at or below target: ${price}! Time to buy!')
        #     else:
        #         print(f'Price is above target. Starting to track...')
        #     return
        
        price_elements = soup.find_all("p", class_="price_color")
        if price_elements:
            for price_element in price_elements:
                price_text = price_element.get_text().strip()
                print(f'Extracted price text: "{price_text}"')
                print('============================================')
                price_str = price_text[2:]
                print(f'Cleaned price string: "{price_str}"')
                price = float(price_str)
                print(f'Initial price: ${price}')     
                # if price <= target_price:
                #     print(f'Price is already at or below target: ${price}! Time to buy!')
                # else:
                #     print(f'Price is above target. Starting to track...')   


    except requests.exceptions.RequestException as e:
        print(f'Error fetching the page: {e}')
        return  
if __name__ == "__main__":
    # url = 'https://books.toscrape.com/'
    url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    target_price = 299.99
    track_price(url, target_price)


