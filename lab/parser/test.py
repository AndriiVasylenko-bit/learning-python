import requests
from bs4 import BeautifulSoup

url = "https://trends.rbc.ru/trends/industry/5e845cec9a794747bf03e2c9"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element with class "article__text__main"
    article_text_main = soup.find('div', class_='article__text__main')

    # Extract and print the text within the <p> tags
    paragraphs = article_text_main.find_all('p')
    for paragraph in paragraphs:
        print(paragraph.get_text().strip())
else:
    print(f"Error: Unable to retrieve the content. Status Code: {response.status_code}")
