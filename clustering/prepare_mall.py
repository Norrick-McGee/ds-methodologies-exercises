from env import user,password,host
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def encode_gender(df):
    encoder = LabelEncoder()
    encoder.fit(df.gender)
    return df.assign(gender = encoder.transform(df.gender))

def detect_outliers(df, col='annual_income'):
    q3 = df[col].quantile(q=.75)
    q1 = df[col].quantile(q=.25)
    iqr = q3 - q1
    iqr_scaled = iqr*1.5
    outlier_floor = iqr_scaled - q1
    outlier_ciel = iqr_scaled + q3
    outlier_df = pd.concat([df[df[col] > outlier_ciel],df[df[col] < outlier_floor]])
    return outlier_df

def drop_outliers(df):
    outliers = detect_outliers(df)
    dfc = df.copy()
    for i in outliers.index:
        dfc.drop(i,inplace=True)
    return dfc

def prep_mall(df):
    return df.pipe(encode_gender).pipe(drop_outliers)
