import mysql.connector
import requests
from bs4 import BeautifulSoup
import time
from local_db import *

# connecting to database
db_connection = mysql.connector.connect(
    host="localhost",
    user=DB_USER,
    password=DB_PASSWORD
)

# make a cursor
cursor = db_connection.cursor(buffered=True)

# create database if not exists and use it (Enter DB)
cursor.execute("CREATE DATABASE IF NOT EXISTS MAKTABKHOONECRAWL")
cursor.execute("USE MAKTABKHOONECRAWL")

# create cars table if not exists
create_table_query = (
    "CREATE TABLE IF NOT EXISTS cars("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "stock TINYINT,"
    "year INT,"
    "brand VARCHAR(40),"
    "model VARCHAR(50),"    
    "mileage INT,"
    "pr_price INT,"
    "se_price INT)"
)
cursor.execute(create_table_query)


print("connected to database successfully!")


# If you want to receive the brand from the user:
# remove the commented part from the comment and comment the uncommented part as well.

# brand = input('Enter Brand (default=BMW): ')
# if brand == '':
#     brand = 'Porsche'
# print('brand = {brand}')
brand = 'Porsche'


# recieving number of pages for crawl
num_of_pages = int(input('Enter number of pages for crawl: '))

print("Please wait for data crawl...")
for i in range(1, num_of_pages + 1):
    url = f"https://www.cars.com/shopping/results/?list_price_max=&makes[]=porsche&maximum_distance=all&models[]=&page={i}&stock_type=all&zip="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", attrs={"class": "vehicle-details"})
    for card in cards:
        stock_temp = card.find('p', attrs={'class': 'stock-type'}).text
        if stock_temp == 'Used':
            stock = 1
        else:
            stock = 0
        title = card.find('h2', attrs={'class': 'title'}).text
        sentence = title.split()
        year = sentence[0]
        brand = sentence[1]
        model = ' '.join(sentence[2:])
        mileage = int(card.find('div', attrs={'class': 'mileage'}).text.split()[0].replace(',', ''))
        pr_price = int(card.find('span', attrs={'class': 'primary-price'}).text.split()[0].replace(',', '')[1:])
        se_price = card.find('span', attrs={'class': 'secondary-price price-drop'})
        if se_price:
            se_price_text = int(se_price.text.split()[0].replace(',', '')[1:])
        else:
            # if price drop not exist!
            se_price_text = pr_price
        # f.write(f'{"use" if stock else "not"} | {year} | {brand} | {model} | {mileage} | {pr_price} | {se_price_text}\n')
        data_to_insert = {
            "stock": stock,
            "year": year,
            "brand": brand,
            "model": model,
            "mileage": mileage,
            "pr_price": pr_price,
            "se_price": se_price_text
        }

        # inserting in table
        insert_query = (
            "INSERT INTO cars"
            "(stock, year, brand, model, mileage, pr_price, se_price) "
            "VALUES (%(stock)s, %(year)s, %(brand)s, %(model)s, %(mileage)s, %(pr_price)s, %(se_price)s)"
        )
        cursor.execute(insert_query, data_to_insert)
        db_connection.commit()
        print(f'page {i} -> commit successfully')


# closing database
cursor.close()
db_connection.close()
