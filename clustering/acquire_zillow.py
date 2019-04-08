from env import username,password,host
import pandas as pd

def generate_url(db = '/'):
    if db[0] is not '/':
        db = '/' + str(db)
    return f'mysql+pymysql://{username}:{password}@{host}{db}'

url = generate_url()
dburl = generate_url('zillow')

print(pd.read_sql('SHOW TABLES;', dburl))

def get_2016_properties(dburl):
    query = 'SELECT * FROM properties_2016'
    #query += ' JOIN '
    return pd.read_sql("SELECT * FROM properties_2016",dburl)

def get_2017_properties(dburl):
    return pd.read_sql("SELECT * FROM properties_2017",dburl)


df2016 = get_2016_properties(dburl)
print('done')
