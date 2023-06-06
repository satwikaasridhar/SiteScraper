import requests
from bs4 import BeautifulSoup

url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

posting_heading = soup.find('h3', text='Search Postings')
posting_div = posting_heading.find_next('div', class_='posting')

postings = posting_div.find_all('div', class_='posting-desc')

for i, posting in enumerate(postings[:5], 1):
    est_value = posting.find('div', class_='est-value').text.strip()
    notes = posting.find('div', class_='notes').text.strip()
    description = posting.find('div', class_='description').text.strip()
    closing_date = posting.find('div', class_='closing-date').text.strip()

    print(f'Posting {i}:')
    print('Est. Value:', est_value)
    print('Notes:', notes)
    print('Description:', description)
    print('Closing Date:', closing_date)
    print()
