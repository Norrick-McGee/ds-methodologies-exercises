from env import username, host, password
import pandas as pd

def generate_url(db = '/'):
    if db[0] is not '/':
        db = '/' + str(db)
    return f'mysql+pymysql://{username}:{password}@{host}{db}'

dburl = generate_url('mall_customers')

def get_customers():
    query = 'SELECT * FROM customers'

    return pd.read_sql(query,dburl)
