import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
from Helper_Functions import *
class MLB:
    def League():
        url ='https://www.espn.com/mlb/standings/_/group/league'
        dbs=pd.read_html(url)
        
        American_or_National=st.sidebar.selectbox('American or National',['American','National'])
        filler_row=pd.DataFrame({list(dbs[0].columns)[0]:list(dbs[0].columns)[0]},index=[0])
        dbs[0]=pd.concat([filler_row,dbs[0]]).reset_index(drop=True)
        
        if American_or_National=='American':
            American_League=pd.concat([dbs[0],dbs[1]],axis=1)
            American_League=American_League.rename(columns={American_League.columns[0]:'TEAM'})

            for i,row in American_League.iterrows():
                American_League.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            American_League.index+=1    
            st.dataframe(American_League)
            
        elif American_or_National=='National':    
            filler_row=pd.DataFrame({list(dbs[2].columns)[0]:list(dbs[2].columns)[0]},index=[0])
            dbs[2]=pd.concat([filler_row,dbs[2]]).reset_index(drop=True)
            National_League=pd.concat([dbs[2],dbs[3]],axis=1)
            National_League=National_League.rename(columns={National_League.columns[0]:'TEAM'})

            for i,row in National_League.iterrows():
                National_League.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
                
            National_League.index+=1   
            st.dataframe(National_League)
    def division():
        url='https://www.espn.com/mlb/standings'

        result=requests.get(url)
        soup=BeautifulSoup(result.text,'html.parser')
        names_table=soup.find_all('table')

        dbs=[pd.read_html(str(i))[0] for i in names_table]
        American=pd.concat([dbs[0],dbs[1]],axis=1)

        A_or_N=st.sidebar.selectbox('American or National', ['American', 'National'])

        if A_or_N=='American': 
            'EAST'
            E_American=American.iloc[0:6]
            E_American.columns=[col for col in E_American.iloc[0]]
            E_American=E_American[1:]
            E_American=E_American.rename(columns={E_American.columns[0]:'TEAM'})
            for i,row in E_American.iterrows():
                E_American.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            E_American=E_American.reset_index(drop=True)
            E_American.index+=1
            st.dataframe(E_American)    
            
            'CENTRAL'
            C_American=American.iloc[6:12]
            C_American.columns=[col for col in C_American.iloc[0]]
            C_American=C_American[1:]
            C_American=C_American.rename(columns={C_American.columns[0]:'TEAM'})
            for i,row in C_American.iterrows():
                C_American.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            C_American=C_American.reset_index(drop=True)
            C_American.index+=1
            st.dataframe(C_American)    
            'WEST'
            W_American=American.iloc[12:18]
            W_American.columns=[col for col in W_American.iloc[0]]
            W_American=W_American[1:]
            W_American=W_American.rename(columns={W_American.columns[0]:'TEAM'})
            for i,row in W_American.iterrows():
                W_American.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            W_American=W_American.reset_index(drop=True)
            W_American.index+=1
            st.dataframe(W_American)    
        elif A_or_N=='National':    
            National=pd.concat([dbs[2],dbs[3]],axis=1)
            'EAST'
            E_National=National.iloc[0:6]
            E_National.columns=[col for col in E_National.iloc[0]]
            E_National=E_National[1:]
            E_National=E_National.rename(columns={E_National.columns[0]:'TEAM'})
            for i,row in E_National.iterrows():
                E_National.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            E_National=E_National.reset_index(drop=True)
            E_National.index+=1
            st.dataframe(E_National)    


            'CENTRAL'
            C_National=National.iloc[6:12]
            C_National.columns=[col for col in C_National.iloc[0]]
            C_National=C_National[1:]
            C_National=C_National.rename(columns={C_National.columns[0]:'TEAM'})
            for i,row in C_National.iterrows():
                C_National.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            C_National=C_National.reset_index(drop=True)
            C_National.index+=1
            st.dataframe(C_National)    

            'WEST'
            W_National=National.iloc[12:18]
            W_National.columns=[col for col in W_National.iloc[0]]
            W_National=W_National[1:]
            W_National=W_National.rename(columns={W_National.columns[0]:'TEAM'})
            for i,row in W_National.iterrows():
                W_National.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            W_National=W_National.reset_index(drop=True)
            W_National.index+=1
            st.dataframe(W_National)    
    def overall():
            'Overall'
            url='https://www.espn.com/mlb/standings/_/group/overall'

            result=requests.get(url)
            soup=BeautifulSoup(result.text,'html.parser')
            names_table=soup.find_all('table')

            dbs=[pd.read_html(str(i))[0] for i in names_table]
            filler_row=pd.DataFrame({list(dbs[0].columns)[0]:list(dbs[0].columns)[0]},index=[0])
            dbs[0]=pd.concat([filler_row,dbs[0]]).reset_index(drop=True)

            dbs[0]=dbs[0].rename(columns={dbs[0].columns[0]:"TEAM"})
            overall=pd.concat([dbs[0],dbs[1]],axis=1)
            overall.index+=1
            for i,row in overall.iterrows():
                overall.loc[i,['TEAM']] = Seperate_Symbol_from_Name(Remove_Non_Capitals(row['TEAM']))[1]
            st.dataframe(overall)

          
                     
               