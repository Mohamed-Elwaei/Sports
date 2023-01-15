import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
from Helper_Functions import *


class Golf:
    def Ryder_Cup():
        url='https://www.espn.com/golf/standings/_/tournament/pgaryderus'
        dbs=pd.read_html(url)[0]
        dbs=dbs.drop(columns=dbs.columns[0])
        dbs.index+=1
        st.dataframe(dbs)
    def Presidential_Cup():  
          
        url='https://www.espn.com/golf/standings/_/tournament/pgapresus'
        dbs=pd.read_html(url)
        
        TEAM_US=dbs[0]
        TEAM_US=TEAM_US.drop(columns=TEAM_US.columns[0])
        TEAM_US.index+=1

        INTL=dbs[1]
        INTL=INTL.drop(columns=INTL.columns[0])
        INTL.index+=1
        st.dataframe(INTL)