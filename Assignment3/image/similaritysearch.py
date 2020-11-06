#IMPORT REQUIRED MODULES
import streamlit as st
import numpy as np
import pandas as pd

#LHS METHOD SELECTION CODE 
add_selectbox = st.sidebar.radio(
    "Select Method",
    ("Cosine Similarity", "FAISS", "InputTextCosine", "InputTextFaiss")
)

st.markdown('<style>body{background-color: #e1c9f8;}</style>',unsafe_allow_html=True)

#IF COSINE SIMILARITY METHOD IS SELECTED, RETURNS COSINE SIMILARITY SEARCH OUTPUT FILE FOR RENDERING
if add_selectbox == 'Cosine Similarity' :
 st.title("COSINE SIMILARITY ")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('Method1.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 st.subheader("Select an image from the dropdown menu :point_down:")
 pic = st.selectbox('Choices:', images)
 st.write("**You selected:**")
 st.image(pic,width=None)


 z = st.slider('How many images do you want to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Output:")
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1
#IF FAISS METHOD IS SELECTED, RETURNS FAISS SIMILARITY SEARCH OUTPUT FILE FOR RENDERING
elif add_selectbox == 'FAISS':
 st.title("FAISS ")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
     return pd.read_csv('FAISS.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 st.subheader("Select an image from the dropdown menu :point_down:")
 pic = st.selectbox('Choices:', images)
 st.write("**You selected:**")
 st.image(pic,width=None)

#DISPLAYING OUTPUT
 z = st.slider('How many images do you want to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Output:")
 st.write('**Images similar to the image selected by you:**')
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1


#INPUT FILE

elif add_selectbox == 'InputTextCosine' :
 user_input = st.text_input('Input URL here:') 


 if user_input :

    st.title("COSINE SIMILARITY ")
    st.write("-------------------------------------------------------------------------------------------------")
    def get_data():
        return pd.read_csv('Method1Git.csv')
    n=1
    df = get_data()
    images = df['0'].unique()
    #st.subheader("Select an image from the dropdown menu :point_down:")
    #pic = st.selectbox('Choices:', images)
    st.write("**You selected:**")
    st.image(user_input,width=None)


    z = st.slider('How many images do you want to see?', 1, 10, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    for index, row in df.iterrows():
        if row['0']==user_input:
            while n < z+1:
                
                st.image(row[n], use_column_width=None, caption=row[n])
                n+=1

 


#INPUT FILE

elif add_selectbox == 'InputTextFaiss' :
 user_input = st.text_input('Input URL here:') 


 if user_input :

    st.title("FAISS ")
    st.write("-------------------------------------------------------------------------------------------------")
    def get_data():
        return pd.read_csv('FAISS.csv')
    n=1
    df = get_data()
    images = df['0'].unique()
    #st.subheader("Select an image from the dropdown menu :point_down:")
    #pic = st.selectbox('Choices:', images)
    st.write("**You selected:**")
    st.image(user_input,width=None)


    z = st.slider('How many images do you want to see?', 1, 10, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    for index, row in df.iterrows():
        if row['0']==user_input:
            while n < z+1:
                
                st.image(row[n], use_column_width=None, caption=row[n])
                n+=1

 
