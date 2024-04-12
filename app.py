import streamlit as st
import pickle
import pandas as pd


movies_list = pickle.load(open("model.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

def recommend(movie_name):
    movie_index = movies_list[movies_list['title']== movie_name].index[0]
    distance = similarity[movie_index]
    top_movies = sorted(list(enumerate(distance)), reverse= True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in top_movies:
        recommended_movies.append(movies_list.iloc[i[0]]['title'])
    return recommended_movies


st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select Movie From The Given List',
    movies_list)

# creating button
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)