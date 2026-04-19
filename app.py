import streamlit as st
import pandas as pd

from database.db import get_connection, init_db
from services.recommender import generate_recommendations
from services.feedback import get_clicked_titles, save_click, get_feedback_scores
from config import TOP_K

# Load data
data = pd.read_csv("data/data.csv")

# DB
conn = get_connection()
init_db(conn)
cursor = conn.cursor()

st.title("🧠 AI Self-Improvement Recommender")

query = st.text_input("Enter your goal")
user_level = st.selectbox("Level", ["beginner", "intermediate", "advanced"])

if st.button("Get Recommendations"):

    scores = generate_recommendations(data, query, user_level)

    clicked_titles = get_clicked_titles(cursor)
    feedback_scores = get_feedback_scores(data['title'], clicked_titles)

    data['final_score'] = scores + feedback_scores

    results = data.sort_values(by='final_score', ascending=False).head(TOP_K)

    for _, row in results.iterrows():
        st.write(f"### {row['title']}")
        st.write(f"Difficulty: {row['difficulty']}")

        if st.button(f"Like {row['title']}", key=row['title']):
            save_click(cursor, conn, row['title'])
            st.success("Saved!")