#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:36:13 2019

@author: snorks
"""

import pandas as pd
import seaborn as sns
from env import user, password, host


url = f'mysql+pymysql://{user}:{password}@{host}'
#pd.read_sql('SHOW DATABASES;', url)

if __name__ == '__main__':

    ## Part 1 ##
    ## Basic info from sns iris dataset ##
    df = sns.load_dataset('iris')

    print('First 3 rows:')
    print(df.head(3))

    print("\nRows x Columns:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns)

    print("\nColumn info:")
    print(df.info())

    print("\nDataFrame statistics:")
    print(df.describe())

    ## /Part 1 ##

    ## Part 2 ## 
    ## Slurping data from Excell ##
    file_path = 'snorks_stats.xlsx'

    df = pd.read_excel(file_path, sheet_name='Data', header=0
                       )
    stats_df = df.head(100)

    print("Number of rows in new DF:")
    print(stats_df.shape[0])

    print("Number of rows in original DF:")
    print(df.shape[0])

    print("First 5 columns:")
    print((stats_df.columns)[:5])

    print("All columns with data type object:")
    dtype_df = stats_df.dtypes
    print(dtype_df[dtype_df == 'object'])



    print("unique values for gender")
    print(df['gender'].unique())

    ## / Part 2 ##

    ## Part 3 ##
    ## slurp from csv on web ##

    df_google = pd.read_csv("train.csv")

    print("print the first 3 rows")
    print(df_google.head(3))

    print("print the number of rows and columns")
    print(df_google.shape)

    print("print the column names")
    print(*df_google.columns, sep=" | ")

    print("print the data type of each column")
    print(df_google.dtypes)

    print("print the summary statistics for each of the numeric variables")
    print(df_google.describe())

    ## /Part 3 ##

    ## Part 4 ##
    ## Mysql workbench ##

    df_csv = pd.read_csv("titanic.csv")
    df_csv.head()

    print("print the column names")
    print(*df_csv.columns, sep=" | ")

    print("print the data type of each column")
    print(df_csv.dtypes)

    print("print the summary statistics for each numeric variable")
    print(df_csv[["age", "fare"]].describe())

    print("print the unique values for each categorical variables. If there are more than 5 distinct values, print the top 5 in terms of prevelence or frequency.")
    cols = ("survived", "pclass", "sex", "sibsp", "parch", "embarked", "class", "deck", "alone")
    for col in cols:
        print(f"{col:>10}: {', '.join(pd.Series(df_csv[col].value_counts().index.values).astype(str).unique()[:5])}")

    ## /Part 4 ##

## Data Slurp ##
def get_titanic_data():

    return pd.read_sql("SELECT * FROM passengers",url+"/titanic_db")

def get_iris_data():

    return pd.read_sql("SELECT * FROM measurements JOIN species USING(species_id);", url+'/iris_db')
