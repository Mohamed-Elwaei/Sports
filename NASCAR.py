import pandas as pd
import streamlit as st

from Helper_Functions import *

class NASCAR:
    def Standings():

        dbs=pd.read_html('https://www.espn.com/racing/standings')[0][1:]
        dbs=dbs.dropna(axis=1)
        cols_to_rename=dict()

        for i in range(len(dbs.columns)):
            cols_to_rename[dbs.columns[i]]=dbs.iloc[0][i]

        dbs=dbs.rename(columns=cols_to_rename)
        dbs=dbs.reset_index(drop=True)
        dbs=dbs.drop(columns=['RK'])
        dbs=dbs[1:]
        st.dataframe(dbs)