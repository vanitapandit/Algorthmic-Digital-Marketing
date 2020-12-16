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
    sales1 = pd.read_csv('all_sales.csv', nrows=nrows)
    sales=sales1.drop(['date'], axis=1)
    sales.fillna(0)
    return sales



weekly_data = load_data(500000)

weekly_data['item_price'].hist(bins=50,edgecolor='white',figsize=(12, 6),range=[0,250])
plt.show()
plt.xlabel('price', fontsize=12)
plt.title('Price Distribution', fontsize=12)
st.pyplot()


#st.subheader('Price Distribution')
#st.write(weekly_data)
#Bar Chart
#st.bar_chart(weekly_data['item_price'])


shipping_fee_by_buyer = weekly_data.loc[weekly_data['shipment'] == 0, 'item_price']
shipping_fee_by_seller = weekly_data.loc[weekly_data['shipment'] == 1, 'item_price']
fig, ax = plt.subplots(figsize=(18,8))
ax.hist(shipping_fee_by_seller, color='#8CB4E1', alpha=1.0, bins=50, range = [0, 100],
       label='Price when Seller pays Shipping')
ax.hist(shipping_fee_by_buyer, color='#007D00', alpha=0.7, bins=50, range = [0, 100],
       label='Price when Buyer pays Shipping')
plt.xlabel('price', fontsize=12)
plt.ylabel('frequency', fontsize=12)
plt.title('Price Distribution by Shipping Type', fontsize=15)
plt.tick_params(labelsize=12)
plt.legend()
plt.show()
st.pyplot()