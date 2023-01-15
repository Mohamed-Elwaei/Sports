
import streamlit as st
from PIL import Image
st.sidebar.image(logo)
from Helper_Functions import *
logo=Image.open(r'C:\Users\win\Documents\Data Science Projects\sports\Symbols\index.png')

sports_choice_list=['⚽SOCCER','🎾TENNIS','🏑NHL','🏈NFL','🏀NBA','🚗NASCAR','🥋MMA','⚾MLB','⛳GOLF','🏎️F1']

sports_choice=st.sidebar.selectbox('CHOOSE YOUR SPORT',sports_choice_list,key='sports_choice')

if sports_choice=='⚽SOCCER':
    import soccer
    soccer.Soccer()
    
    
if sports_choice=='🏑NHL':
    from NHL import NHL
    choice=st.sidebar.selectbox('',options=['LEAGUE','CONFERENCE','DIVISION'])
    if choice=='LEAGUE':
        NHL.League()
    elif choice=='CONFERENCE':
        NHL.Confernce()
    elif choice=='DIVISION':
        NHL.Division()
        
if sports_choice=='🏈NFL':
    from NFL import NFL
    choice=st.sidebar.selectbox('',options=['LEAGUE','CONFERENCE','DIVISION'])
    if choice=='LEAGUE':
        NFL.League()
    elif choice=='CONFERENCE':
        NFL.conferences()
    elif choice=='DIVISION':
        NFL.Division()
if sports_choice=='🏀NBA':
    from NBA import NBA
    choice=st.sidebar.selectbox('',options=['LEAGUE','CONFERENCE','DIVISION'])
    if choice=='LEAGUE':
        NBA.League()
    elif choice=='CONFERENCE':
        NBA.Conferences()
    elif choice=='DIVISION':
        NBA.Division()
        
if sports_choice=='🚗NASCAR':
    from NASCAR import NASCAR
    NASCAR.Standings()
   
        
if sports_choice=='🥋MMA':
    from MMA import MMA
    MMA.Division_Rankings()

if sports_choice=='⚾MLB':
    from MLB import MLB
    choice=st.sidebar.selectbox('',options=['LEAGUE','OVERALL','DIVISION'])
    if choice=='LEAGUE':
        MLB.League()
    elif choice=='OVERALL':
        MLB.overall()
    elif choice=='DIVISION':
        MLB.division()
if sports_choice=='⛳GOLF':
    from Golf import Golf
    choice=st.sidebar.selectbox('',options=['RYDER CUP','PRESIDENTIAL CUP'])
    if choice=='RYDER CUP':
        Golf.Ryder_Cup()
    elif choice=='PRESIDENTIAL CUP':
        Golf.Presidential_Cup()
if sports_choice=='🏎️F1':
    from F1 import F1
    choice=st.sidebar.selectbox('',options=['DRIVER STANDINGS','CONSTRUCTOR STANDINGS'])
    if choice=='DRIVER STANDINGS':
        F1.Driver_Standings()
    elif choice=='CONSTRUCTOR STANDINGS':
        F1.Constructor_Standings()