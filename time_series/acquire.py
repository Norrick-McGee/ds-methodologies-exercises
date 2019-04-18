import requests
import json
import pandas as pd
import os

def get_items():
    url='https://python.zach.lol'
    response = requests.get(url+'/api/v1/items')
    items = [pd.DataFrame(response.json()['payload']['items'])]
    response = requests.get(url+response.json()['payload']['next_page'])
    items.append(pd.DataFrame(response.json()['payload']['items']))
    response = requests.get(url+response.json()['payload']['next_page'])
    items.append(pd.DataFrame(response.json()['payload']['items']))
    #print(response.json()['payload']['next_page'])
    return pd.concat(items).reset_index().drop(columns="index")

def get_stores():
    url='https://python.zach.lol'
    response = requests.get(url+'/api/v1/stores').json()
    #print(f"max page: {response['payload']['max_page']}")
    #print(f"next page: {response['payload']['next_page']}")
    return pd.DataFrame(response['payload']['stores'])

def get_sales():
    url='https://python.zach.lol'
    counter = 0
    sales= []
    response = requests.get(url+'/api/v1/sales').json()
    print(f"total pages to download: {response['payload']['max_page']}")
    while True:
        sales.append(pd.DataFrame(response['payload']['sales']))
        counter += 1

        if counter%10==0:
            print(f"Pages {counter-9} - {counter} loaded successfully")
        if response['payload']['next_page'] == None:
            print('No next page, acquisition complete')
            print(f"{counter} pages loaded successfully")
            break
        response = requests.get(url+response['payload']['next_page']).json()
    print('merging pages into DataFrame')
    return pd.concat(sales).reset_index().drop(columns="index")

def merge_dfs(sales,items,stores):
    sales = sales.rename({'store':"store_id",'item':'item_id'},axis=1)
    merged = pd.merge(sales,items)
    merged = pd.merge(merged,stores)
    return merged

def generate_csvs():
    print('generating multiple large csvs, please be patient')
    print('Downloading list of items')
    items = get_items()
    print('Complete')
    print('Downloading sales, this may take some time')
    sales = get_sales()
    print('Complete')
    print('Downloading List of stores')
    stores = get_stores()
    print('Complete')

    if not os.path.exists('./csvs/'):
        os.makedirs('./csvs/')
    print('Converting to CSVs')
    sales.to_csv('./csvs/sales.csv',index=False)
    items.to_csv('./csvs/items.csv',index=False)
    stores.to_csv('./csvs/stores.csv',index=False)

    return [sales,items,stores]

def load_csvs():

    return([pd.read_csv('./csvs/sales.csv'), pd.read_csv('./csvs/items.csv'),pd.read_csv('./csvs/stores.csv')])


def acquire_sales(refresh_data = False):
    if not os.path.exists('./csvs/'):
        os.makedirs('./csvs/')

    if refresh_data or not (os.path.isfile('./csvs/sales.csv') and os.path.isfile('./csvs/items.csv') and os.path.isfile('./csvs/stores.csv')):
        return merge_dfs(*generate_csvs())
    else:
        return merge_dfs(*load_csvs())
