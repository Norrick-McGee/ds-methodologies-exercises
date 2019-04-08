from env import user,password,host

def detect_outliers(df):
    ""

def encode_gender(df):
    encoder = LabelEncoder()
    encoder.fit(df.gender)
    return df.assign(gender = encoder.transform(df.gender))
