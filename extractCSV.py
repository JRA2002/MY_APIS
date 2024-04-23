import requests
import csv

url = 'http://127.0.0.1:8000/api/'

params = {
    'name':'name',
    'price':'price'
}

response = requests.get(url,params=params)

if response.status_code == 200:
    product_list = response.json()
    
    with open('products1.csv','w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=['name','price'])
        
        writer.writeheader()
        
        for product in product_list:
            writer.writerow({
                'name':product['name'],
                'price':product['price']
            })
            
else:
    print(f'error to obtain the product : {response.status_code}')