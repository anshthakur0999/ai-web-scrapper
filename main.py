import streamlit as st
from scrape import scrape_website ,split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_ollama

st.title('AI Web Scrapper')

url = st.text_input('Enter a Website URL:')

if st.button('Scrape'):
    try:
        st.write('Scraping...')
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        
        st.session_state.dom_content = cleaned_content
        
        with st.expander('View Content'):
            st.text_area('DOM Content', cleaned_content, height=300)
            
    except Exception as e:
        st.error(f"Error occurred while scraping: {str(e)}")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe What you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)