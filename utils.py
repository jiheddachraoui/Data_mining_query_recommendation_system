import csv
import time
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def KNN(k,similarity,IDs):
    indexes=(np.argsort(np.array(similarity))[::-1][:k]).tolist()
    return (similarity[indexes],IDs[indexes])


def jaccard_similarity(a, b):
    a = set(a)
    b = set(b)
    j = float(len(a.intersection(b))) / len(a.union(b))
    return j

def standardize(row):
    new_row=(row-row.mean())/(row.max()-row.min())
    return new_row

def center(row):
    new_row=(row-row.mean())
    return new_row

def k_nearest_neighbor(arr,k):
    n,m=arr.shape
    #get the indexes of the (n-k) least similar items to set to 0 
    for i in range(n):
        arr[i][arr[i].argmax()]=0
        indexes=arr[i].argsort()[:m-k].tolist()
        arr[i][indexes]=0
    return(arr)


def user_similarity(dataframe,k,center_matrix=False,standardize_matrix=False):
    gh=dataframe.fillna(0)
    if standardize_matrix: gh=gh.apply(standardize)
    if center_matrix: gh=gh.apply(center)
    u_sim_matrix=cosine_similarity(gh)
    return np.round(k_nearest_neighbor(u_sim_matrix,k),4)

def query_similarity(dataframe,k,center_matrix=False,standardize_matrix=False):
    gh=dataframe.fillna(0)
    gh=dataframe.fillna(0)
    if standardize_matrix: gh=gh.apply(standardize)
    if center_matrix: gh=gh.apply(center)
    q_sim_matrix=np.array(gh.apply(center).corr(method='pearson'))
    return np.round(k_nearest_neighbor(q_sim_matrix,k),4)




#collaborative filtreing with query to query similarity 
def predict_queries(utility_matrix,q_sim_matrix):
    utility_matrix_copy=utility_matrix.fillna(0)
    output=utility_matrix_copy.copy()
    scores_to_predict = np.array(np.where(utility_matrix.fillna(0)== 0)).T  
    for i,j in scores_to_predict:
        weighted_score=np.dot(utility_matrix_copy.iloc[i],q_sim_matrix[j])
        weights_used=np.dot(q_sim_matrix[j],utility_matrix.iloc[i].notna())
        output.iloc[i,j]=round(weighted_score/weights_used,2)
    return output

#collaborative filtreing with user to user similarity 
def predict_users(utility_matrix,u_sim_matrix):
    utility_matrix_copy=utility_matrix.fillna(0)
    output=utility_matrix_copy.copy()
    columns=utility_matrix.axes[1]
    scores_to_predict = np.array(np.where(utility_matrix.fillna(0)== 0)).T
    for i,j in scores_to_predict:
        weighted_score=np.dot(utility_matrix_copy[columns[j]],u_sim_matrix[i])
        weights_used=np.dot(u_sim_matrix[i],utility_matrix[columns[j]].notna())
        output.iloc[i,j]=round(weighted_score/weights_used,2)
    return output
