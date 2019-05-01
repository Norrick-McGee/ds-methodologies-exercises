import requests
import pandas as pd


def open_file():

    file = open("access.log","r").readlines()
    for index,string in enumerate(file):
        file[index]= string[:-1]
    return file

def file_to_dict():

    file = open_file()
    file_dic = {}
    for log in file:
        file_dic[((log.split())[3]+(log.split())[4])[1:-1]] = {'user_ip' : (log.split())[0],
                                                          'method' :  ((log.split())[5])[1:],
                                                          'request' : (log.split())[6],
                                                          'protocol':((log.split())[7])[:-1],
                                                          'http_status': (log.split())[8],
                                                          'size': (log.split())[9],
                                                          'unknown':(log.split())[10].replace('"',''),
                                                          'user_agent': str((log.split())[11:])[3:-3]}

    return file_dic



def get_dataframe(date_time_as_index=True):

    if date_time_as_index:
        return pd.DataFrame(file_to_dict()).T
    else:
        return (pd.DataFrame(file_to_dict()).T.reset_index()).rename(columns={'index':'date_time'})
