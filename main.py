# main.py
import streamlit as st
from chatbot import get_response
from scrape import scrape
from preprocess import preprocess_text
import os
import openai

# Fetch the API key from environment secrets
api_key = os.environ["SECRET_API_KEY"]


st.title('Chatbot and Amazon Scraper')

def determine_intent(input_text):
    # Simple keyword-based intent detection
    search_triggers = ["search for", "find me", "look up", "search amazon for"]
    for trigger in search_triggers:
        if trigger in input_text.lower():
            return True
    return False

user_input = st.text_input("Ask me something or search for products:")
if user_input:
    if determine_intent(user_input):
        # Treat input as a search query
        cleaned_query = preprocess_text(user_input)
        print(cleaned_query)
        df = scrape(cleaned_query)
        if not df.empty:
            st.dataframe(df)
        else:
            st.write("No products found or failed to scrape Amazon.")
    else:
        # Process input as a chat message
        response = get_response(user_input)
        st.text_area("Bot says:", value=response, height=200)
