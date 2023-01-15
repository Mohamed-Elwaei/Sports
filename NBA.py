import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
from Helper_Functions import *

class NBA:
    def League():

        url='https://www.espn.com/nba/standings/_/group/league'
        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        tables=soup.find_all('table')
        dbs=[pd.read_html(str(table))[0] for table in tables]
        filler_row=pd.DataFrame({list(dbs[0].columns)[0]:list(dbs[0].columns)[0]},index=[0])
        dbs[0]=pd.concat([filler_row,dbs[0]]).reset_index(drop=True)
        standings=pd.concat([dbs[0],dbs[1]],axis=1)
        standings=standings.reset_index(drop=True)
        standings=standings.rename(columns={standings.columns[0]:'TEAM'})
        standings.index+=1
        for i, row in standings.iterrows():
            standings.loc[i,'TEAM']=Seperate_Symbol_from_Name(Remove_Non_Capitals((standings.loc[i,'TEAM'])))[1]
        st.dataframe(standings)
    def Conferences():    
        url ='https://www.espn.com/nba/standings/_/group/conference'
        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        tables=soup.findAll('table')
        dbs=pd.read_html(url)
        filler_row=pd.DataFrame({list(dbs[0].columns)[0]:list(dbs[0].columns)[0]},index=[0])

        st.header('Eastern Conference')
        dbs[0]=pd.concat([filler_row,dbs[0]]).reset_index(drop=True)
        E_conf=pd.concat([dbs[0],dbs[1]],axis=1)
        E_conf=E_conf.rename(columns={E_conf.columns[0]:'TEAM'})
        for i, row in E_conf.iterrows():
            E_conf.loc[i,'TEAM']=Seperate_Symbol_from_Name(Remove_Non_Capitals((E_conf.loc[i,'TEAM'])))[1]
        E_conf.index+=1
        st.dataframe(E_conf)

        st.header('Western Conference')
        dbs[2]=pd.concat([filler_row,dbs[0]]).reset_index(drop=True)
        W_conf=pd.concat([dbs[2],dbs[3]],axis=1)
        W_conf=W_conf.rename(columns={W_conf.columns[0]:'TEAM'})
        for i, row in W_conf.iterrows():
            W_conf.loc[i,'TEAM']=Seperate_Symbol_from_Name(Remove_Non_Capitals((W_conf.loc[i,'TEAM'])))[1]
        W_conf.index+=1
        st.dataframe(W_conf)
    def Division():    
        url='https://www.espn.com/nba/standings/_/group/division'
        dbs=pd.read_html(url)
        choice =st.sidebar.selectbox('Eastern or Western Conference',['Eastern', 'Western'])
        
        E_conf=pd.concat([dbs[0],dbs[1]],axis=1)
        ATL_CENT_SE=[]

        for i in range(0,len(E_conf),6):
            tmp=E_conf.iloc[i:i+6]
            tmp=tmp.reset_index(drop=True)
            tmp.columns=[i for i in tmp.loc[0]]
            tmp=tmp[1:]
            for i, row in tmp.iterrows():
                tmp.loc[i,tmp.columns[0]]=Seperate_Symbol_from_Name(Remove_Non_Capitals((tmp.loc[i,tmp.columns[0]])))[1]
            ATL_CENT_SE.append(tmp)

        E_conf=pd.concat([dbs[0],dbs[1]],axis=1)
        #Atlantic Central SouthEast; For loop splits them

        W_CONF=pd.concat([dbs[2],dbs[3]],axis=1)
        # Same Idea as above
        NW_PAC_SW=[]

        for i in range(0,len(W_CONF),6):
            tmp=W_CONF.iloc[i:i+6]
            tmp=tmp.reset_index(drop=True)
            tmp.columns=[i for i in tmp.loc[0]]
            tmp=tmp[1:]
            for i, row in tmp.iterrows():
                tmp.loc[i,tmp.columns[0]]=Seperate_Symbol_from_Name(Remove_Non_Capitals((tmp.loc[i,tmp.columns[0]])))[1]
            NW_PAC_SW.append(tmp)

        if choice=='Eastern':
            for i in range(len(ATL_CENT_SE)):
                st.header(ATL_CENT_SE[i].columns[0])
                st.dataframe(ATL_CENT_SE[i])  
        elif choice=='Western':
            for i in range(len(NW_PAC_SW)):
                st.header(NW_PAC_SW[i].columns[0])
                st.dataframe(NW_PAC_SW[i])          
