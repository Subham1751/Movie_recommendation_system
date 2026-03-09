import streamlit as st
import pickle
import pandas as pd
import difflib

# Page configuration
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommendation System" )
st.write("Get movie recommendations based on your favorite movie")

# Load data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies['title'].values


# Recommendation function
def recommend(movie_name):

    list_of_all_movies = movies['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_movies)

    if not find_close_match:
        return []

    close_match = find_close_match[0]

    index_of_movie = movies[movies.title == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_movie]))

    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []

    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies[movies.index == index]['title'].values[0]

        if i < 11:
            recommended_movies.append(title_from_index)
            i += 1

    return recommended_movies


# UI
selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    if recommendations:
        st.subheader("Recommended Movies")

        for movie in recommendations:
            st.write(movie)
    else:
        st.warning("Movie not found in database")