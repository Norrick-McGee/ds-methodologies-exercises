import pandas as pd
import numpy as np
from scipy.stats import iqr
from sklearn.preprocessing import MinMaxScaler

def unit_count_impute(df):
    df = df.copy()
    df.unitcnt = df.unitcnt.replace(np.nan,1)
    return df

def drop_no_bathbr(df):
    i = df[df['bedroomcnt' ]==0]
    j = i[i['bathroomcnt'] ==0]
    return df.drop(j.index)

def drop_dup_parcelid(df):
    return df.drop_duplicates(subset='parcelid')

def df_missing_values_in_cols(df):
    cols = list(df.columns)
    percent_missing = []
    for col in cols:
        percent_missing.append((sum(df[col].isnull())/df.shape[0])*100)
    tot_missing=[]
    for col in cols:
        tot_missing.append(sum(df[col].isnull()))

    return pd.DataFrame(list(zip(cols, percent_missing, tot_missing)), columns=['column','percent missing','total missing'])


def df_missing_cols_in_rows(df):
    df = df.copy()
    if 'missing' in list(df.columns):
        df.drop('missing',axis=1,inplace=True)
    missing_col_by_row = df.T.isnull().sum()
    total_cols = df.shape[1]
    missing_cols_percentage = missing_col_by_row/total_cols
    df['missing'] = missing_col_by_row
    df['missing_percentage'] = missing_cols_percentage
    return df

def missing_values(df,rows=False):
    if rows:
        return df_missing_cols_in_rows(df)
    else:
        return df_missing_values_in_cols(df)

def drop_cols_missing_percentage(df,percentage):
    columns_missing_more_than_50 = list(missing_values(df)[missing_values(df)['percent missing'] > percentage].column)
    return df.drop(columns_missing_more_than_50,axis=1)

def drop_multiunits(df):
    return df.drop(df[df.unitcnt>1].index)

def drop_missing_rows_by_column(df,col):
    return df[~df[col].isnull()]

def outliers(df,col,drop_top=False,drop_bot=False):
    q1 = df[col].quantile(.25)
    q3 = df[col].quantile(.75)
    iqrscaled = iqr(df[col])*1.5
    upper = df[df[col] > q3+ float(iqrscaled)]
    lower = df[df[col] < float(iqrscaled) - q1]

    if drop_top and drop_bot:
        df = df.copy()
        df.drop(upper.index,inplace = True)
        return df.drop(lower.index)
    elif drop_top:
        return df.drop(upper.index)
    elif drop_bot:
        return df.drop(lower.index)

    return pd.concat([upper[['parcelid',col]],lower[['parcelid',col]]])


def scale_df(df,cols = []):
    scaler = MinMaxScaler()
    df = df.copy()
    for col in cols:
        scaler.fit(df[[col]])
        df[col] = scaler.transform(df[[col]])
    return df

def only_singletons(df):
    return df.pipe(drop_multiunits)\
    .pipe(drop_no_bathbr)



def prep_zillow(df):
    return df.pipe(only_singletons)\
    .pipe(drop_dup_parcelid)
