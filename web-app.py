!pip install bs4
import pandas as pd
import requests
import base64

from bs4 import BeautifulSoup
import streamlit as st

def scrape(url, pages):
    base_url = url
    page_size = 100

    reviews = []
    ratings = []

    for i in range(1, pages + 1):
        st.write(f"Scraping page {i}")

        # Create URL to collect links from paginated data
        url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

        # Collect HTML data from this page
        response = requests.get(url)

        # Parse content
        content = response.content
        parsed_content = BeautifulSoup(content, 'html.parser')

        # Find all  elements with the itemprop attribute set to "reviewRating"
        rating_elements = parsed_content.find_all("div", {"itemprop": "reviewRating"})

        for rating_element in rating_elements:
            # Find the  element with the itemprop attribute set to "ratingValue"
            rating_value_element = rating_element.find("span", {"itemprop": "ratingValue"})

            # Extract the text content of the element, which is the rating value
            rating = rating_value_element.text

            ratings.append(rating)

        st.write(f"   ---> {len(ratings)} total ratings")

        for para in parsed_content.find_all("div", {"class": "text_content"}):
            reviews.append(para.get_text())

        st.write(f"   ---> {len(reviews)} total reviews")

    if len(reviews) != len(ratings):
        difference = len(reviews) - len(ratings)
        for i in range(0, difference):
            ratings.append(0)

    # Store the ratings and reviews in a pandas DataFrame
    df = pd.DataFrame({"rating": ratings, "review": reviews})

    return df

st.header("Airline Reviews Scraper")

with st.form("input_form"):
    url = st.text_input("URL")
    pages = st.number_input("Pages", min_value=1, step=1)
    submitted = st.form_submit_button("Scrape")

if submitted:
    df = scrape(url, pages)
    st.write(df)

    # Save the DataFrame to a CSV file and offer for download
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings
    href = f'<a href="data:file/csv;base64,{b64}" download="airline_reviews.csv">Download as CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
