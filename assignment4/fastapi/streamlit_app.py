import streamlit as st
import numpy as np
import pandas as pd
import time
#from PIL import Image
import json
import requests

#st.sidebar.markdown('**_RECOMMENDATION SYSTEM :SNACKFAIR_**')
itemName = pd.read_csv('Itemcategory.csv' ,encoding= 'unicode_escape')
userName = pd.read_csv('final_snack_data.csv')

radio = "LightGBM Algorithm"
#st.markdown('<style>body{background-color: #B8E2F2;}</style>',unsafe_allow_html=True)
#st.sidebar.slider.markdown("<h1 style='text-align: left; color: Blue;'>'ABC',0,20,10</h1>", unsafe_allow_html=True)


st.markdown('<style>body{background-color: #E9C9F8;}</style>',unsafe_allow_html=True)

if radio == 'LightGBM Algorithm':
    
    genre = st.selectbox(
        "Choose the Recommendation Method:",
        ('No Selection', 'similarity based on ITEM ID'))
    
    if genre == 'No Selection':
        
        st.title('Recommendation System')
        #image = Image.open('reco.jpg')
        #st.image(image, caption='',use_column_width=True)
    
    
    
    
    elif genre == 'similarity based on ITEM ID':
        
        #st.title('Recommendation on the basis of Item ID')
        sentence = st.text_input('Enter the ITEM ID:',value='0')
        
        number = int(sentence)   
        
        if st.button('Similar Items based on Item ID'):
            payload = json.dumps({
                "ItemId" : number
                })
            response = requests.get(f"http://127.0.0.1:8000/recommend_items?ItemId={number}")
            data_list = response.json()
            data_list = response.json()
            item = pd.DataFrame(data_list)
            item.columns = ['ItemId']
            item['ItemId'] = item['ItemId'].astype(int)
            join = pd.merge(left = item, right = itemName, left_on = 'ItemId', right_on = 'ItemId')
            join.drop('Category', axis = 1, inplace = True)
            #join.columns = ['Item_id', 'itemName', 'category']
            
            st.dataframe(join)
            #st.markdown(data_list)
            
            
        if st.button('Similar Item bought by other Users'):
            payload = json.dumps({
                "ItemId" : number
                })
            response = requests.get(f"http://127.0.0.1:8000/recommend_items_users?ItemId={number}")
            data_list = response.json()
            user = pd.DataFrame(data_list)
            user.columns = ['userID']
            user['userID'] = user['userID'].astype(int)
            join = pd.merge(left = user, right = userName, left_on = 'userID', right_on = 'userID')
            #join.drop('occupation', axis = 1, inplace = True)
            #join.columns = ['itemID', 'itemName', 'category']
            
            st.dataframe(join)

