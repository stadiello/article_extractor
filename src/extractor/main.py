import streamlit as st
from scrap import Scraper
from bot import OllamaClient
import pandas as pd
import io
import re

def parse_bot_response(response):
    """
    Parse the response from the bot and return a dictionary of questions and answers.
    """
    if "no nawsuit" in response.lower():
        return None
    
    lines = response.strip().split('\n')
    data = {}
    for line in lines:
        if ':' in line:
            question, answer = line.split(':', 1)
            data[question.strip()] = answer.strip()
    return data

def bot(text):
    client = OllamaClient()
    return client.generation(text)

def summary(text):
    client = OllamaClient()
    return client.summary(text)

def main():
    st.title("Article extractor")
    st.subheader("Extract and summarize legal articles")

    mode = st.radio(
        "Choose the summary mode :",
        ("Efficient", 'No summary'),
        index=0
    )

    url = st.text_input("Enter the URL to scrape:")
    if st.button("Scrape"):
        if url:
            try:
                with st.spinner('Extraction in progress...'):
                    scp = Scraper()
                    result = scp.scrapUrl(url)

                    progress_placeholder = st.empty()
                    progress_bar = progress_placeholder.progress(0)
                    
                    progress_bar.progress(33)
                    st.success(f"Scraping of {url} is done!")
                    
                    with st.spinner('Data extraction...'):
                        bot_result = bot(result)
                        progress_bar.progress(66)
                        st.write(bot_result)
                        
                        # Préparer les données pour le CSV
                        parsed_data = parse_bot_response(bot_result)
                        if parsed_data:
                            df = pd.DataFrame([parsed_data])
                            csv = df.to_csv(index=False)
                            st.download_button(
                                label="Télécharger les réponses (CSV)",
                                data=csv,
                                file_name="responses.csv",
                                mime="text/csv"
                            )
                    
                    with st.spinner('Generating summary...'):
                        if mode == "Efficient":
                            summary_result = summary(result)
                        elif mode == "No summary":
                            summary_result = "No summary requested."
                        
                        progress_bar.progress(100)
                        st.write(summary_result)
                    
                    progress_placeholder.success("✅ Done!")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                import traceback
                st.error(traceback.format_exc())
        else:
            st.error("Please enter a valid URL.")

if __name__ == "__main__":
    main()