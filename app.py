import streamlit as st
import pickle


movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values

st.header("Movie Recomandation System")




select_value = st.selectbox("Select Movies From The Dropdown",movies_list)

def recommend(movie):
    index = movies[movies['title']== movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    rec = []
    for i in distance[1:6]:
        rec.append(movies.iloc[i[0]].title)
    return rec

if st.button("Recommend"):
    movie_rec = recommend(select_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_rec[0])

    with col2:
        st.text(movie_rec[1])

    with col3:
        st.text(movie_rec[2])

    with col4:
        st.text(movie_rec[3])

    with col5:
        st.text(movie_rec[4])



