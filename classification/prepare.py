#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:04:28 2019

@author: snorks
"""

#import acquire
#from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import MinMaxScaler

#def prep_iris():
#    df = acquire.get_iris_data()

#    df = df.drop("species_id",axis = 1)
#    df = df.drop("measurement_id", axis=1)
#    df = df.rename(columns={'species_name':'species'})

#    df.info()

#    iris_enc = LabelEncoder()
#    iris_enc.fit(df.species)
#    df.species = iris_enc.transform(list(df.species))
#   return df

# df = acquire.get_titanic_data()
# df = df.assign(
#        embark_town=df.embark_town.fillna('Other'),
#        embarked=df.embarked.fillna('O')
#    )

#df = df.drop(columns='deck')

#encoder=LabelEncoder()
#encoder.fit(df.embarked)
#df = df.assign(embarked=encoder.transform(df.embarked))



###################

import pandas as pd
import acquire

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def drop_i_columns(df):
    '''drops iris columns'''
    return df.drop(columns=(['measurement_id', 'species_id']))

def rename_species(df):
    '''renames species_name to species'''
    return df.rename(index=str, columns={'species_name': 'species'})

def encode_species(df):
    '''encodes species'''
    encoder = LabelEncoder()
    encoder.fit(df.species)
    return df.assign(species=encoder.transform(df.species))


def handle_missing_values(df):
    '''sets missing values in embarked and embark_town'''
    return df.assign(
        embark_town=df.embark_town.fillna('Other'),
        embarked=df.embarked.fillna('O')
    )

def drop_t_columns(df):
    '''drop deck'''
    return df.drop(columns='deck')

def encode_embarked(df):
    '''encodes embarked'''
    encoder=LabelEncoder()
    encoder.fit(df.embarked)
    return df.assign(embarked=encoder.transform(df.embarked))

def prep_titanic(df):
    '''preps all of titanic'''
    return df.pipe(handle_missing_values)\
        .pipe(drop_t_columns)\
        .pipe(encode_embarked)

def prep_iris(df):
    '''preps all of iris data'''
    return df.pipe(drop_i_columns)\
        .pipe(rename_species)\
        .pipe(encode_species)
