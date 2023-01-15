import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
from Helper_Functions import *


class F1:
    def Driver_Standings():
        url='https://www.espn.com/f1/standings'
        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        tables=soup.find_all('table')
        dbs=[pd.read_html(str(table))[0] for table in tables]
        standings=pd.concat([dbs[0],dbs[1]],axis=1)
        standings=standings.reset_index(drop=True)
        standings=standings.rename(columns={standings.columns[-1]:''})
        standings=standings.rename(columns={standings.columns[0]:'NAME'})

        for i,row in standings.iterrows():
            standings.loc[i,'ABRV'] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['NAME']))[0]
            standings.loc[i,['NAME']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['NAME']))[1]
        cols=list(standings.columns.values)
        standings=standings[[cols[-1]]+cols[:-1]]
        standings=standings.fillna('_')
        st.dataframe(standings)
    def Constructor_Standings():   
        url='https://www.espn.com/f1/standings/_/group/constructors'
        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        tables=soup.find_all('table')
        dbs=[pd.read_html(str(table))[0] for table in tables]
        standings=pd.concat([dbs[0],dbs[1]],axis=1)
        standings=standings.reset_index(drop=True)
        standings=standings.rename(columns={standings.columns[0]:'NAME'})
        standings=standings.rename(columns={standings.columns[-1]:''})

        for i,row in standings.iterrows():
            standings.loc[i,['NAME']] = split_string_by_two(Remove_Non_Capitals(row['NAME']))
        standings.index+=1    
        standings=standings.fillna('_')
        st.dataframe(standings)
