import os
import glob
import pandas as pd
import numpy as np

# read all *.csv in samle file once and merge into one csv 

def data_prepare():
    #files = !ls *.csv # IPython magic
    # using glob get all csv name in same route as list 
    files = glob.glob('./*.csv')
    df = pd.concat([pd.read_csv(f, index_col=0, header=None) for f in files], keys=files)
    df.columns = ['name','address','url','style','area']
    df_ = df.ix[1:].reset_index()
    df_ = df_[['name','address','url','style','area']]
    #df_.head()
    return df_

def data_clean(df):
    # modify ur city list here 
    area_ = ['萬華區']
    df = df[area_].reset_index()
    return df

# group by city name and rename columns 
df_ = data_prepare()
df_inter = df_.groupby(['area','style']).count().reset_index()[['area','style','name']]
df_inter.columns = [['area','style','count']]

# to pivot table 
df_pivot = pd.pivot_table(df_inter, values='count', index=['area'],columns=['style'], aggfunc=np.sum).fillna(0).T
df_pivot_ = data_clean(df_pivot)
df_pivot.to_csv('df_pivot_final.csv')






