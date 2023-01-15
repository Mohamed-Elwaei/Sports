import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
from Helper_Functions import *
class MMA:
    def Division_Rankings():
            url='https://www.espn.com/mma/story/_/id/21807736/mma-divisional-rankings-ufc-bellator-pfl-rankings-weight-class'
            result=requests.get(url)
            soup=BeautifulSoup(result.text,'html.parser')

            Weight_classes=soup.find_all('h2')
            Weight_classes=[Class.text for Class in Weight_classes]

            Fighter_Names=soup.find_all('h3')
            Fighter_Names=[Class.text for Class in Fighter_Names]

            for name in Fighter_Names:
                name=name.encode('ascii','ignore')
                name=name.decode()
            
            Classes_To_Names={}

            j=0
            for i in range(0,len(Weight_classes)):
                Classes_To_Names[Weight_classes[i]]=Fighter_Names[j:j+10]
                j+=10

            soup=str(soup).split('<h2>')
            soup=soup[1:]
            soup=['<h2>'+tag for tag in soup]
            Stats_soup=[BeautifulSoup(tag, 'html.parser').find_all('p') for tag in soup]
            stats=[]
            for i in Stats_soup:
                tmp=[]
                for j in i:
                    tmp.append(j.text)
                tmp.pop()    
                stats.append(tmp)

            Statistics={}
            Cols=stats[0][0].split('\n')
            Cols=[col.split(':')[0] for col in Cols]

            Final_Statistics={}
            for i in range(len(stats)):
                W_Class=[]
                for j in range(len(stats[i])):
                 try:
                    tmp_dict=dict()
                    stats[i][j]=stats[i][j].split('\n')
                    stats[i][j]=[s.split(':')[1].lstrip() for s in stats[i][j]]
                    if len(stats[i][j])<4:
                        stats[i][j].append(stats[i][j+1][0])
                        del stats[i][j+1]
                    tmp_dict[Fighter_Names[(i*10)+j]]=stats[i][j]
                    W_Class.append(tmp_dict)
                 except: i 
                    
                Final_Statistics[Weight_classes[i]]=W_Class
                


            dbs=[]
            for i in range(len(Weight_classes)):
                NAMES=[]
                PROMOTION=[]
                RECORD=[]
                LAST=[]
                NEXT=[]
                for j in range(len(Final_Statistics[Weight_classes[i]])):
                    name=list(Final_Statistics[Weight_classes[i]][j].keys())[0]
                    prom=Final_Statistics[Weight_classes[i]][j][Fighter_Names[(i*10)+j]][0]
                    rec=Final_Statistics[Weight_classes[i]][j][Fighter_Names[(i*10)+j]][1]
                    lst=Final_Statistics[Weight_classes[i]][j][Fighter_Names[(i*10)+j]][2]
                    nxt=Final_Statistics[Weight_classes[i]][j][Fighter_Names[(i*10)+j]][3]
                    NAMES.append(name)
                    PROMOTION.append(prom)
                    RECORD.append(rec) 
                    LAST.append(lst)
                    NEXT.append(nxt)
                d={'NAME':NAMES,'PROMOTION':PROMOTION,'RECORD':RECORD,'LAST':LAST,'NEXT':NEXT} 
                db=pd.DataFrame(data=d)
                db.index+=1
                dbs.append(db)
            Male_Weight_classes=dbs[:8]
            Female_Weight_classes=dbs[8:]
            MMA_choice=st.sidebar.selectbox('',['Male Weight classes','Female Weight classes'],key='MMA_choice')
            if MMA_choice=='Male Weight classes':
                for i in range(len(Male_Weight_classes)):
                    st.header(Weight_classes[i])
                    st.dataframe(Male_Weight_classes[i])
            elif MMA_choice=='Female Weight classes':  
                for i in range(len(Female_Weight_classes)):
                    st.header(Weight_classes[i+len(Male_Weight_classes)])
                    st.dataframe(Female_Weight_classes[i])
                    
MMA.Division_Rankings()                    