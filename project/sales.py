import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
import lightgbm as lgb
st.title('Prediction')
st.set_option('deprecation.showPyplotGlobalUse', False)


@st.cache
def load_data(nrows):
    sales = pd.read_csv('all_sales.csv', nrows=nrows)
    df= sales[['date','item_id','shop_id','item_name','sales']]
    df['date'] = pd.to_datetime(df['date'])
    #represent month in date field as its first day
    df['date'] = df['date'].dt.year.astype('str') + '-' + df['date'].dt.month.astype('str') + '-01'
       #groupby date and sum the sales
    df = df.groupby('date').sales.sum().reset_index()
    return df



weekly_data = load_data(500000)

plt.figure(figsize=(15,5))
plt.plot(weekly_data['date'],weekly_data['sales'])

plt.xticks(rotation=90)
plt.title('Monthly Sales')
plt.xlabel('Date')

plt.show()
st.pyplot()


#st.subheader('Price Distribution')
#st.write(weekly_data)
#Bar Chart
#st.bar_chart(weekly_data['item_price'])


