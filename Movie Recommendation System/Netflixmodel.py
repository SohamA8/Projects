# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:40:17 2024

@author: Admin
"""

import streamlit as st
import pickle
import pandas as pd


    
def recommend(show):
    show_index = movies[movies['title'] == show].index[0]
    distances = similarity[show_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies 
        
movies_list = pickle.load(open('netflix.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation Model :film_projector:')
select_movie_name = st.selectbox(
    'Type your favourite movie name',
    movies['title'].values)

if st.button('Recommend'):
   recommendations = recommend(select_movie_name)
   for i in recommendations:
       st.write(i)
      
   
       