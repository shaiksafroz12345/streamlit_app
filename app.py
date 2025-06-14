# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mini Profile Builder", layout="centered")

st.title("💼 Mini Profile Builder")

# 1. Name input
name = st.text_input("What is your name?")

# 2. Age slider
age = st.slider("How old are you?", 10, 100, 25)

# 3. Dropdown for programming language
language = st.selectbox(
    "What is your favorite programming language?",
    ("Python", "JavaScript", "C++", "Java", "Go", "Rust")
)

# 4. Button to display result
if st.button("Generate My Profile"):
    if name:
        st.subheader("👤 Profile Summary")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Favorite Language:** {language}")

        # 5. Generate a mock skill chart
        st.subheader("📊 Skill Rating (Demo)")
        skills = ["Communication", "Problem Solving", "Teamwork", "Coding", "Debugging"]
        ratings = np.random.randint(50, 100, size=len(skills))

        df = pd.DataFrame({"Skill": skills, "Rating": ratings})

        fig, ax = plt.subplots()
        ax.bar(df["Skill"], df["Rating"], color="skyblue")
        ax.set_ylabel("Rating (%)")
        ax.set_ylim(0, 100)
        ax.set_title("Your Skill Chart (Randomized)")
        st.pyplot(fig)
    else:
        st.warning("Please enter your name to build your profile.")
