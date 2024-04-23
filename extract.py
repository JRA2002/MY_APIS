import requests
import csv

url = 'http://127.0.0.1:8000/api/'

params = {
    'name':'name',
    'price':'price',
    'description':'description'   
}

response = requests.get(url,params=params)

if response.status_code == 200:
    product_list = response.json()
    print(product_list)
    with open('products.csv','w',newline='') as csvfile:
        
        writer = csv.DictWriter(csvfile,fieldnames=['name','price','description'])
        
        writer.writeheader()
        
        for product in product_list:
            writer.writerow({
                'name':product['name'],
                'price':product['price'],
                'description':product['description']
            })
            
else:
    print(f'error to obtain product list: {response.status_code}')