import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_abstractive_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def abstractive_summarize(text):
    summarizer = load_abstractive_model()

    if len(text.split()) > 900:
        text = " ".join(text.split()[:900])

    result = summarizer(text, max_length=250, min_length=80, do_sample=False)
    return result[0]['summary_text']