import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer  # Use Tfidf instead of CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Step 1: Setup - Install necessary libraries (if not installed)
# !pip install nltk pandas scikit-learn wordcloud streamlit

# Step 2: Data Preparation
nltk.download("movie_reviews")

# Load the dataset
documents = [
    (" ".join(nltk.corpus.movie_reviews.words(fileid)), category)
    for category in nltk.corpus.movie_reviews.categories()
    for fileid in nltk.corpus.movie_reviews.fileids(category)
]

# Convert to DataFrame
df = pd.DataFrame(documents, columns=["review", "sentiment"])

# Step 3: Model Training
vectorizer = TfidfVectorizer(max_features=2000)  # Use TfidfVectorizer instead of CountVectorizer
X = vectorizer.fit_transform(df["review"])
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)  # Increase max_iter for better convergence
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

# Streamlit User Interface Customization
st.title("My Custom Sentiment Analysis Tool")
st.header("Analyze the sentiment of any text, be it a movie review, product review, or tweet!")

st.markdown("""
    ## How it works
    1. Type a review or text in the input box above.
    2. Click 'Analyze Sentiment' to analyze the sentiment of the text.
    3. The sentiment will be displayed as either **Positive** or **Negative**.
""")

# User Input
user_input = st.text_area("Enter your review or text here:", placeholder="Type a product review or tweet here...")

# Analyze Button
if st.button("Analyze Sentiment"):
    if user_input:
        sentiment = model.predict(vectorizer.transform([user_input]))[0]
        sentiment_display = "Positive 😊" if sentiment == 'pos' else "Negative 😞"
        st.write(f"**Sentiment: {sentiment_display}**")
    else:
        st.write("Please enter some text to analyze.")

# Word Cloud Visualizations
st.markdown("### Word Cloud - Positive Reviews")
positive_reviews = ' '.join([word for word in nltk.corpus.movie_reviews.words(categories='pos')])
wordcloud = WordCloud(background_color='white', colormap='Blues', width=800, height=400).generate(positive_reviews)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

st.markdown("### Word Cloud - Negative Reviews")
negative_reviews = ' '.join([word for word in nltk.corpus.movie_reviews.words(categories='neg')])
wordcloud_neg = WordCloud(background_color='white', colormap='Reds', width=800, height=400).generate(negative_reviews)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_neg, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

# Footer with Contact Info
st.markdown("""
---
Developed by [Oday](mailto:oday198@icloud.com) | Contact: oday198@icloud.com
""", unsafe_allow_html=True)
