from env import username,password,host
import pandas as pd

def generate_url(db = '/'):
    if db[0] is not '/':
        db = '/' + str(db)
    return f'mysql+pymysql://{username}:{password}@{host}{db}'

#aurl = generate_url()
dburl = generate_url('zillow')

#print(pd.read_sql('SHOW TABLES;', dburl))

def get_2016_properties():
    dburl = generate_url('zillow')
    dfz = pd.read_sql('SELECT * FROM properties_2016 JOIN predictions_2016 USING (parcelid)',dburl)
    tables = pd.read_sql('SHOW TABLES',dburl)
    tables.drop(4,inplace=True)
    tables.drop(5,inplace=True)
    tables.drop(6,inplace=True)
    tables.drop(7,inplace=True)
    tables.drop(11,inplace=True)

    type_dfs = []
    for i in list(tables.Tables_in_zillow):
        type_dfs.append(pd.read_sql('SELECT * FROM '+i,dburl))

    dfz2 = dfz
    for i in type_dfs:
        dfz2 = pd.merge(dfz2,i,how="left")

    return dfz2

def get_2017_properties():
        dburl = generate_url('zillow')
        dfz = pd.read_sql('SELECT * FROM properties_2017 JOIN predictions_2017 USING (parcelid)',dburl)
        tables = pd.read_sql('SHOW TABLES',dburl)
        tables.drop(4,inplace=True)
        tables.drop(5,inplace=True)
        tables.drop(6,inplace=True)
        tables.drop(7,inplace=True)
        tables.drop(11,inplace=True)

        type_dfs = []
        for i in list(tables.Tables_in_zillow):
            type_dfs.append(pd.read_sql('SELECT * FROM '+i,dburl))

        dfz2 = dfz
        for i in type_dfs:
            dfz2 = pd.merge(dfz2,i,how="left")

        return dfz2

def join_1617():
    

#df2016 = get_2016_properties(dburl)
#print('done')
