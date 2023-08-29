import mysql.connector
from sklearn import tree
from local_db import *


# connecting to database
db_connection = mysql.connector.connect(
    host="localhost",
    user=DB_USER,
    password=DB_PASSWORD,
    database='maktabkhoonecrawl'
)

# get data from database
query = "SELECT stock, year, brand, model, mileage, pr_price FROM cars"
cursor = db_connection.cursor(dictionary=True)
cursor.execute(query)
results = cursor.fetchall()

# closing database
cursor.close()
db_connection.close()

data_list = []
for row in results:
    data_list.append(row)


x = []
y = []

# for labeling
brand_label = []
model_label = []

for data in data_list:
    temp = []
    temp.append(data['stock'])
    temp.append(data['year'])
    if data['brand'] not in brand_label:
        brand_label.append(data['brand'])
    temp.append(brand_label.index(data['brand']))
    if data['model'] not in model_label:
        model_label.append(data['model'])
    temp.append(model_label.index(data['model']))
    temp.append(data['mileage'])
    x.append(temp)
    y.append(data["pr_price"])


# create decision tree classifier and fit it
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

print('Default values: stock: No | year: 2020 | brand: Porsche | model: 911 Turbo | mileage: 500')
flag = input('Default or manual input? (\'d\' or \'m\'): ')

if flag.lower() == 'm':
    # reciving data from user
    stock_status_temp = input("Is it in stock? (\'y\' or \'n\'): ")
    stock_status = 1 if stock_status_temp.lower() == 'y' else 0
    year = int(input("Enter Year: "))
    brand = input('Enter Brand: ')
    model = input('Enter Model: ')
    mileage = int(input("Enter mileage: "))
else:
    stock_status = 0
    year = 2020
    brand = 'Porsche'
    model = '911 Turbo'
    mileage = 5000

# find a Predicted Price
user_input = [[0, 2020, brand_label.index('Porsche'), model_label.index('911 Turbo'), 5000]]
answer = clf.predict(user_input)[0]
print(f"Predicted Price: ${answer}")