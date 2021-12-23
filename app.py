import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Social media data analysis")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    st.write("")
    st.write("")
    # processing
    data_trending_employers = data[data['categoryType'] == "Top Trending Employers"]
    location = data_trending_employers["countryName"].to_numpy()[0]
    data_trending_jobs = data[data['categoryType'] == "Top Trending Jobs"]
    data_trending_skills = data[data['categoryType'] == "Top Trending Skills"]

    genre = st.radio(
        "Select the trending",
        ('Trending Employers', 'Trending Jobs', 'Trending Skills'))
    
    if genre == 'Trending Employers':
        st.write('# Trending Employers of {}'.format(location))
        fig = plt.figure(figsize=(10, 10))
        sns.barplot(y=data_trending_employers['categoryName'], x=data_trending_employers['categoryValue'],)
        st.pyplot(fig)
    
    if genre == 'Trending Jobs':
        st.write('# Trending Jobs of {}'.format(location))
        fig = plt.figure(figsize=(10, 10))
        sns.barplot(y=data_trending_jobs['categoryName'], x=data_trending_jobs['categoryValue'],)
        st.pyplot(fig)
    
    if genre == 'Trending Skills':
        fig = plt.figure(figsize=(10, 10))
        st.write('# Trending Skills of {}'.format(location))
        sns.barplot( y=data_trending_skills['categoryName'], x=data_trending_skills['rank'],)
        st.pyplot(fig)
