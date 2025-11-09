import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


books_data = pickle.load(open("books_list1.pkl", 'rb'))


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books_data['processed_description'])


cosine_sim1 = cosine_similarity(tfidf_matrix, tfidf_matrix)


st.title("📚 Library Book Recommendation System")
st.write("Select a book from the list below to see similar recommendations.")


selectvalue = st.selectbox("Select a book:", books_data['title'])


def recommend_books(book_title):
    try:
        idx = books_data[books_data['title'] == book_title].index[0]
        if idx >= cosine_sim1.shape[0]:  # Check if index is valid
            st.error("The selected book's index is out of bounds for the similarity matrix.")
            return idx, []
    except IndexError:
        st.error("The selected book is not in the database.")
        return None, []

 
    sim_scores = list(enumerate(cosine_sim1[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Exclude the book itself

   
    book_indices = [i[0] for i in sim_scores]
    recommendations = [(books_data['title'].iloc[i], i) for i in book_indices]
    return idx, recommendations


if st.button("Show Recommendations"):
    selected_book_idx, recommended_books = recommend_books(selectvalue)    
    if recommended_books:
        st.subheader("Selected Book:")
        st.write(f"Book Number: {selected_book_idx}, Title: {selectvalue}")

        # Display the recommended books
        st.subheader("Recommended Books:")
        for book, idx in recommended_books:
            st.write(f"Book Number: {idx}, Title: {book}")
    else:
        st.write("No recommendations available.")
