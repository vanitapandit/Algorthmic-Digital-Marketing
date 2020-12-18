import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import time
#from PIL import Image
import json
import requests



st.sidebar.markdown('Sales Prediction and LTV reports')

chosen = st.sidebar.radio(
        'Select the action',
        ("Sales Prediction and LTV", "Recommendation system"))



userName = pd.read_csv('all_sales.csv', encoding= 'unicode_escape')
userName = userName[['CustomerID','item_id','item_name']].drop_duplicates()

itemName = userName[['item_id','item_name']]
itemName = itemName.drop_duplicates()

if chosen == "Recommendation system":
            st.markdown('<style>body{background-color: #B8E2F2;}</style>',unsafe_allow_html=True)
            #st.sidebar.slider.markdown("<h1 style='text-align: left; color: Blue;'>'ABC',0,20,10</h1>", unsafe_allow_html=True)


            st.markdown('<style>body{background-color: #E9C9F8;}</style>',unsafe_allow_html=True)

            if chosen == 'Recommendation system':
                
                
                    st.title('Recommendation System - similarity based on ITEM ID')
                    #image = Image.open('reco.jpg')
                    #st.image(image, caption='',use_column_width=True)
                
                    
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
                        item.columns = ['item_id']
                        item['item_id'] = item['item_id'].astype(int)
                        join = pd.merge(left = item, right = itemName, left_on = 'item_id', right_on = 'item_id')
                        
                        
                        st.dataframe(join)
                        #st.markdown(data_list)
                        
                        
                    if st.button('Similar Item bought by other Users'):
                        payload = json.dumps({
                            "ItemId" : number
                            })
                        response = requests.get(f"http://127.0.0.1:8000/recommend_items_users?ItemId={number}")
                        data_list = response.json()
                        user = pd.DataFrame(data_list)
                        user.columns = ['CustomerID']
                        user['CustomerID'] = user['CustomerID'].astype(int)
                        join = pd.merge(left = user, right = userName, left_on = 'CustomerID', right_on = 'CustomerID')
                        #join.drop('occupation', axis = 1, inplace = True)
                        #join.columns = ['itemID', 'itemName', 'category']
                        
                        st.dataframe(join)

if chosen == 'Sales Prediction and LTV':
        components.iframe("https://app.powerbi.com/reportEmbed?reportId=35475db1-6020-463f-ad3c-a6ef01ac7c64&autoAuth=true&ctid=a8eec281-aaa3-4dae-ac9b-9a398b9215e7&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXVzLW5vcnRoLWNlbnRyYWwtZi1wcmltYXJ5LXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9&filterPaneEnabled=false", scrolling=False, height=550, width=850)

       

       

