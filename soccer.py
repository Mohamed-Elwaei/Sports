import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests

def Soccer():
    url='https://www.espn.com/soccer/competitions'
    result=requests.get(url)
    soup=BeautifulSoup(result.text,'html.parser')
    competitions=soup.find_all('div', class_='pl3')
    Leagues=dict()

    for competition in competitions:
        team=competition.h2.get_text()
        link= competition.a['href']
        Leagues[team]=link

    list_of_leagues=sorted(list(Leagues.keys()))
    selected_league=st.sidebar.selectbox('League', list_of_leagues)
    st.title(selected_league)

    new_url=Leagues[selected_league]
    new_res=requests.get(new_url)
    new_soup=BeautifulSoup(new_res.text,'html.parser')
    table_heads=new_soup.find_all('thead')
    table_bodys=new_soup.find_all('tbody')
    tables=[]


    for i in range(len(table_heads)):
        tmp='<table>'+str(table_heads[i])+str(table_bodys[i])+'</table>'
        tables.append(tmp)


    tables=[pd.read_html(table)[0] for table in tables]

    for table in tables:
        table.index +=1
        st.dataframe(table)

