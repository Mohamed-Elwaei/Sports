from ast import FunctionType
import pandas as pd
import streamlit as st
from io import StringIO
from bs4 import BeautifulSoup
import requests
from Helper_Functions import *

class NHL():
    def League():
        url ='https://www.espn.com/nhl/standings/_/group/league'
        db=pd.read_html(url)
        filler_row=pd.DataFrame({list(db[0].columns)[0]:list(db[0].columns)[0]},index=[0])
        db[0]=pd.concat([filler_row,db[0]]).reset_index(drop=True)
        nhl=pd.concat([db[0],db[1]], axis=1)
        db[0].columns=['TEAM']
        nhl=pd.concat([db[0],db[1]],axis=1)
        nhl.index+=1


        for i,row in nhl.iterrows():
            nhl.loc[i,['TEAM']] = Seperate_Symbol_from_Name(row['TEAM'])[1]
            nhl.loc[i,['SYMBOL']] = Seperate_Symbol_from_Name(row['TEAM'])[0]

        cols=list(nhl.columns)      
        nhl=nhl[[cols[-1]]+cols[0:-1]]
        st.dataframe(nhl)
    def Confernce():        
        url ='https://www.espn.com/nhl/standings/_/group/conference'
        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        tables=soup.findAll('table')
        dbs=pd.read_html(url)

        choice= st.sidebar.selectbox('', options=['EASTERN CONFERENCE','WESTERN CONFERENCE'])
        if choice=='EASTERN CONFERENCE': 
            EASTERN_CONFERENCE_list=dbs[0:2]
            filler_row=pd.DataFrame({list(EASTERN_CONFERENCE_list[0].columns)[0]:list(EASTERN_CONFERENCE_list[0].columns)[0]},index=[0])
            EASTERN_CONFERENCE_list[0]=pd.concat([filler_row,EASTERN_CONFERENCE_list[0]]).reset_index(drop=True)
            EASTERN_CONFERENCE=pd.concat([EASTERN_CONFERENCE_list[0],EASTERN_CONFERENCE_list[1]], axis=1)
            EASTERN_CONFERENCE_list[0].columns=['TEAM']
            EASTERN_CONFERENCE=pd.concat([EASTERN_CONFERENCE_list[0],EASTERN_CONFERENCE_list[1]],axis=1)
            EASTERN_CONFERENCE.index+=1
            for i,row in EASTERN_CONFERENCE.iterrows():
                EASTERN_CONFERENCE.loc[i,['TEAM']] = Seperate_Symbol_from_Name(row['TEAM'])[1]
                EASTERN_CONFERENCE.loc[i,['SYMBOL']] = Seperate_Symbol_from_Name(row['TEAM'])[0]

            cols=list(EASTERN_CONFERENCE.columns)      
            EASTERN_CONFERENCE=EASTERN_CONFERENCE[[cols[-1]]+cols[0:-1]]
            st.dataframe(EASTERN_CONFERENCE)
            
        if choice=='WESTERN CONFERENCE':    
            WESTERN_CONFERENCE_list=dbs[0:2]
            filler_row=pd.DataFrame({list(WESTERN_CONFERENCE_list[0].columns)[0]:list(WESTERN_CONFERENCE_list[0].columns)[0]},index=[0])
            WESTERN_CONFERENCE_list[0]=pd.concat([filler_row,WESTERN_CONFERENCE_list[0]]).reset_index(drop=True)
            WESTERN_CONFERENCE=pd.concat([WESTERN_CONFERENCE_list[0],WESTERN_CONFERENCE_list[1]], axis=1)
            WESTERN_CONFERENCE_list[0].columns=['TEAM']
            WESTERN_CONFERENCE=pd.concat([WESTERN_CONFERENCE_list[0],WESTERN_CONFERENCE_list[1]],axis=1)
            WESTERN_CONFERENCE.index+=1
            for i,row in WESTERN_CONFERENCE.iterrows():
                WESTERN_CONFERENCE.loc[i,['TEAM']] = Seperate_Symbol_from_Name(row['TEAM'])[1]
                WESTERN_CONFERENCE.loc[i,['SYMBOL']] = Seperate_Symbol_from_Name(row['TEAM'])[0]

            cols=list(WESTERN_CONFERENCE.columns)      
            WESTERN_CONFERENCE=WESTERN_CONFERENCE[[cols[-1]]+cols[0:-1]]
            st.dataframe(WESTERN_CONFERENCE)     
    def Division():
        East_Or_West=st.sidebar.selectbox('', ['EASTERN', 'WESTERN'])

        url='https://www.espn.com/nhl/standings'

        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        names_table=soup.find_all('table')

        dbs=[pd.read_html(str(i))[0] for i in names_table]

        if East_Or_West=='EASTERN':
            Atlantic_or_Metroplitan=st.sidebar.selectbox('ATLANTIC OR METROPOLITAN', ['ATLANTIC', 'METROPOLITAN'])
            EASTERN_CONFERENCE=pd.concat([dbs[0],dbs[1]],axis=1)
            if Atlantic_or_Metroplitan=='ATLANTIC':
                Atlantic=EASTERN_CONFERENCE.iloc[0:9]
                Atlantic.columns=[col for col in Atlantic.iloc[0]]
                Atlantic=Atlantic[1:]
                Atlantic=Atlantic.reset_index(drop=True)
                Atlantic.index+=1
                for i,row in Atlantic.iterrows():
                    Atlantic.loc[i,['Atlantic']] = Seperate_Symbol_from_Name(row['Atlantic'])[1]
                st.dataframe(Atlantic)
            elif Atlantic_or_Metroplitan=='METROPOLITAN':    
                Metropolitan=EASTERN_CONFERENCE.iloc[9:]
                Metropolitan.columns=[col for col in Metropolitan.iloc[0]]
                Metropolitan=Metropolitan[1:]
                Metropolitan=Metropolitan.reset_index(drop=True)
                Metropolitan.index+=1
                for i,row in Metropolitan.iterrows():
                    Metropolitan.loc[i,['Metropolitan']] = Seperate_Symbol_from_Name(row['Metropolitan'])[1]
                st.dataframe(Metropolitan)

        if East_Or_West=='WESTERN':   
            WESTERN_CONFERENCE=pd.concat([dbs[2],dbs[3]],axis=1)
            Central_or_Pacific=st.sidebar.selectbox("CENTRAL OR PACIFIC",['CENTRAL',"PACIFIC"])        
            if Central_or_Pacific=='CENTRAL': 
                Central=WESTERN_CONFERENCE.iloc[0:9]
                Central.columns=[col for col in Central.iloc[0]]
                Central=Central[1:]
                Central=Central.reset_index(drop=True)
                Central.index+=1
                for i,row in Central.iterrows():
                    Central.loc[i,['Central']] = Seperate_Symbol_from_Name(row['Central'])[1]
                st.dataframe(Central)
            elif Central_or_Pacific=='PACIFIC':    
                Pacific=WESTERN_CONFERENCE.iloc[9:]
                Pacific.columns=[col for col in Pacific.iloc[0]]
                Pacific=Pacific[1:]
                Pacific=Pacific.reset_index(drop=True)
                Pacific.index+=1
                for i,row in Pacific.iterrows():
                    Pacific.loc[i,['Pacific']] = Seperate_Symbol_from_Name(row['Pacific'])[1]
                st.dataframe(Pacific)    
