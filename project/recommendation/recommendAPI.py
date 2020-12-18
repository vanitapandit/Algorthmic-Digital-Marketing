import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import joblib

def recommend_item_item(ItemId):
    interactions = joblib.load('interactions')
    user_dict = joblib.load('user_dict')
    item_dict = joblib.load('item_dict')
    model = joblib.load('mf_model')
    
    def create_item_emdedding_distance_matrix(model,interactions):
        df_item_norm_sparse = sparse.csr_matrix(model.item_embeddings)
        similarities = cosine_similarity(df_item_norm_sparse)
        item_emdedding_distance_matrix = pd.DataFrame(similarities)
        item_emdedding_distance_matrix.columns = interactions.columns
        item_emdedding_distance_matrix.index = interactions.columns
        return item_emdedding_distance_matrix
    
    
    item_item_dist = create_item_emdedding_distance_matrix(model = model,
                                                       interactions = interactions)
    
    def item_item_recommendation(item_emdedding_distance_matrix, ItemId, 
                                 item_dict, n_items = 10, show = True):
        '''
        Function to create item-item recommendation
            - recommended_items = List of recommended items
        '''
        recommended_items = list(pd.Series(item_emdedding_distance_matrix.loc[ItemId,:]. \
                                      sort_values(ascending = False).head(n_items+1). \
                                      index[1:n_items+1]))
        if show == True:
            print("Item of interest :{0}".format(item_dict[ItemId]))
            print("Item similar to the above item:")
            counter = 1
            for i in recommended_items:
                print(str(counter) + '- ' +  item_dict[i])
                counter+=1
        return recommended_items
    
    rec_list_item = item_item_recommendation(item_emdedding_distance_matrix = item_item_dist,
                                    ItemId = ItemId,
                                    item_dict = item_dict,
                                    n_items = 5)
    
    return rec_list_item

def recommend_similar_user_item(ItemId):
    interactions = joblib.load('interactions')
    user_dict = joblib.load('user_dict')
    item_dict = joblib.load('item_dict')
    model = joblib.load('mf_model')
    
    def sample_recommendation_item(model,interactions,ItemId,user_dict,item_dict,number_of_user):
        '''
        Funnction to produce a list of top N interested users for a given item
            - user_list = List of recommended users 
        '''
        n_users, n_items = interactions.shape
        x = np.array(interactions.columns)
        scores = pd.Series(model.predict(np.arange(n_users), np.repeat(x.searchsorted(ItemId),n_users)))
        user_list = list(interactions.index[scores.sort_values(ascending=False).head(number_of_user).index])
        return user_list 
    
    rec_item_user = sample_recommendation_item(model = model,
                               interactions = interactions,
                               ItemId = ItemId,
                               user_dict = user_dict,
                               item_dict = item_dict,
                               number_of_user = 15)
    
    return rec_item_user
    
