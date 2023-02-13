# British-airways-reviews-scraper-python
Python Data Scraper to scrape the reviews from the British Airways  websites

This is a web scraping code in Python using the libraries pandas and requests along with BeautifulSoup. The code scrapes review ratings and reviews of the British Airways from the website airlinequality.com.

The code first defines the base_url to the reviews page of British Airways and the number of pages to be scraped (pages). The page_size is set to 100. Then, two empty lists are created reviews and ratings to store the scraped data.

In the for loop, the code generates the URL for each page, makes a GET request to the URL, and collects the HTML content. The HTML content is then parsed using the BeautifulSoup library. The code finds all the <div> elements with the itemprop attribute set to "reviewRating" to scrape the ratings. The ratings are extracted from the <span> element with the itemprop attribute set to "ratingValue".

In the next step, the code finds all the <div> elements with the class "text_content" to extract the reviews. After the for loop, the code checks if the number of reviews is equal to the number of ratings, if not, the difference is calculated, and 0 is appended to the ratings list the same number of times as the difference.

Finally, the scraped ratings and reviews are stored in a pandas DataFrame and written to a CSV file named British_Aiways-reviews.csv.

In summary, this code scrapes the reviews and ratings of British Airways from the airlinequality.com website and stores the data in a CSV file for future use.



