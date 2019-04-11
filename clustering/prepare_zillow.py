import pandas as pd

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

def df_missing_cols(df):
    cols = list(df.columns)
    percent_missing = []
    for col in cols:
        percent_missing.append((sum(df[col].isnull())/df.shape[0])*100)
    tot_missing=[]
    for col in cols:
        tot_missing.append(sum(df[col].isnull()))

    return pd.DataFrame(list(zip(cols, percent_missing, tot_missing)), columns=['column','percent missing','total missing'])

def df_missing_v_rows(df):
    ### Returns the isnull count for columns for each row as a Series (can be added to DF)
    return df.T.isnull().sum()

def drop_multiunits(df):
    return df.drop(df[df.unitcnt>1].index)

def only_singletons(df):
    return df.pipe(drop_multiunits)\
    .pipe(drop_no_bathbr)

def prep_zillow(df):
    return df.pipe(only_singletons)
