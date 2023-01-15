from Helper_Functions import *
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests

class NFL:

    
    st.title(':football: NFL Standings 2022')
    def Division():
        choice=st.sidebar.selectbox('',['AFC','NFC'])
        url='https://www.espn.com/nfl/standings'
        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        names_table=soup.find_all('table',{'class':'Table Table--align-right Table--fixed Table--fixed-left'})
        afcs=pd.read_html(str(names_table[0]))[0]
        afcs.index+=1
        nfcs=pd.read_html(str(names_table[1]))[0]
        nfcs.index+=1


        dbs=soup.find_all('table')
        dfs=[]
        for db in dbs:
            dfs.append(pd.read_html(str(db))[0])

        afc=pd.concat([dfs[0],dfs[1]],axis=1)
        afcs_to_represent=[]
        for i in range(0,len(afc),5):
            tmp=afc.iloc[i:i+5]
            tmp.columns=[col for col in tmp.iloc[0]]
            tmp=tmp.iloc[1:]
            tmp=tmp.reset_index(drop=True)
            tmp.index+=1
            for i,row in tmp.iterrows():
                    tmp.loc[i,tmp.columns[0]] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row[tmp.columns[0]]))[1]
            afcs_to_represent.append(tmp)   
        nfcs_to_represent=[]
        nfc=pd.concat([dfs[2],dfs[3]],axis=1)
        for i in range(0,len(nfc),5):
            tmp=nfc.iloc[i:i+5]
            tmp.columns=[col for col in tmp.iloc[0]]
            tmp=tmp.iloc[1:]
            tmp=tmp.reset_index(drop=True)
            tmp.index+=1
            for i,row in tmp.iterrows():
                    tmp.loc[i,tmp.columns[0]] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row[tmp.columns[0]]))[1]
            nfcs_to_represent.append(tmp)
        if choice=='AFC':
            for a in afcs_to_represent:
                st.dataframe(a)    
        if choice=='NFC':
            for a in nfcs_to_represent:
                st.dataframe(a)    


    def conferences():        
        url ='https://www.espn.com/nfl/standings/_/group/conference'
        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        tables=soup.findAll('table')
        dbs=pd.read_html(url)

        choice= st.sidebar.selectbox('NFC or AFC: ', options=['AFC','NFC'])
        if choice=='AFC':
            afc_list=dbs[0:2]
            filler_row=pd.DataFrame({list(afc_list[0].columns)[0]:list(afc_list[0].columns)[0]},index=[0])
            afc_list[0]=pd.concat([filler_row,afc_list[0]]).reset_index(drop=True)
            afc=pd.concat([afc_list[0],afc_list[1]], axis=1)
            st.header('American Football Conference')
            afc_list[0].columns=['TEAM']
            afc=pd.concat([afc_list[0],afc_list[1]],axis=1)
            afc.index+=1
            for i,row in afc.iterrows():
                    afc.loc[i,afc.columns[0]] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row[afc.columns[0]]))[1]
            st.dataframe(afc)
        if choice=='NFC':    
            nfc_list=dbs[2:]
            filler_row=pd.DataFrame({list(nfc_list[0].columns)[0]:list(nfc_list[0].columns)[0]},index=[0])
            nfc_list[0]=pd.concat([filler_row,nfc_list[0]]).reset_index(drop=True)
            nfc=pd.concat([nfc_list[0],nfc_list[1]], axis=1)
            st.header('National Football Conference')
            nfc_list[0].columns=['TEAM']
            nfc=pd.concat([nfc_list[0],nfc_list[1]],axis=1)
            nfc.index+=1
            for i,row in nfc.iterrows():
                    nfc.loc[i,nfc.columns[0]] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row[nfc.columns[0]]))[1]
            st.dataframe(nfc)
    def League():      
        url ='https://www.espn.com/nfl/standings/_/group/league'
        db=pd.read_html(url)
        filler_row=pd.DataFrame({list(db[0].columns)[0]:list(db[0].columns)[0]},index=[0])
        db[0]=pd.concat([filler_row,db[0]]).reset_index(drop=True)
        nfl=pd.concat([db[0],db[1]], axis=1)
        db[0].columns=['TEAM']
        nfl=pd.concat([db[0],db[1]],axis=1)
        for i,row in nfl.iterrows():
            nfl.loc[i,nfl.columns[0]] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row[nfl.columns[0]]))[1]
        nfl.index+=1    
        st.dataframe(nfl)
        



########
# st.header('NFL Standings')
# url='https://www.espn.com/nfl/standings'
# result=requests.get(url)
# soup=BeautifulSoup(result.text,'html.parser')
# names_table=soup.find_all('table',{'class':'Table Table--align-right Table--fixed Table--fixed-left'})
# afcs=pd.read_html(str(names_table[0]))[0]
# afcs.index+=1
# nfcs=pd.read_html(str(names_table[1]))[0]
# nfcs.index+=1


# dbs=soup.find_all('table')
# # table_for_afcs=dbs[0]
# dfs=[]
# for db in dbs:
#     dfs.append(pd.read_html(str(db))[0])

# afc=pd.concat([dfs[0],dfs[1]],axis=1)
# afcs_to_represent=[]
# for i in range(0,len(afc),5):
#     tmp=afc.iloc[i:i+5]
#     tmp.columns=[col for col in tmp.iloc[0]]
#     tmp=tmp.iloc[1:]
#     tmp=tmp.reset_index(drop=True)
#     tmp.index+=1
#     for i,row in tmp.iterrows():
#             tmp.loc[i,tmp.columns[0]] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row[tmp.columns[0]]))[1]
#     afcs_to_represent.append(tmp)

# nfcs_to_represent=[]
# nfc=pd.concat([dfs[2],dfs[3]],axis=1)
# for i in range(0,len(nfc),5):
#     tmp=nfc.iloc[i:i+5]
#     tmp.columns=[col for col in tmp.iloc[0]]
#     tmp=tmp.iloc[1:]
#     tmp=tmp.reset_index(drop=True)
#     tmp.index+=1
#     for i,row in tmp.iterrows():
#             tmp.loc[i,tmp.columns[0]] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row[tmp.columns[0]]))[1]
#     nfcs_to_represent.append(tmp)
    

