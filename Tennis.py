import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
from Helper_Functions import *

class Tennis:
    def Male_Rankings():

        url='https://www.espn.com/tennis/rankings/_/season/2022'
        MALE_RK=pd.read_html(url)[0]
        MALE_RK=MALE_RK.drop(columns=[MALE_RK.columns[0],MALE_RK.columns[1]])
        MALE_RK.index+=1
        st.dataframe(MALE_RK)
    def Female_Rankings():     
        url='https://www.espn.com/tennis/rankings/_/type/wta/season/2022'
        FEMALE_RK=pd.read_html(url)[0]
        FEMALE_RK=FEMALE_RK.drop(columns=[FEMALE_RK.columns[0],FEMALE_RK.columns[1]])
        FEMALE_RK.index+=1        
        st.dataframe(FEMALE_RK)
        