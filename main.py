import requests
from bs4 import BeautifulSoup
from requests.api import get
import webbrowser

def get_article():

    reponnse = requests.get(
    url="https://en.wikipedia.org/wiki/Special:Random",
    )

    soup = BeautifulSoup(reponnse.content, 'html.parser')

    return soup

while True:

    option = input('Do you want to see another article [Y/N]: ')

    if option == 'y':
        soup = get_article()
        title = soup.find(id="firstHeading").string
        print('')
        print(title)
        print('')
        intrested = input('Are you intrested [Y/N]: ')
        print('')
        if intrested == 'y':
            new_title = title.replace(' ', '_')
            webbrowser.open(f'https://en.wikipedia.org/wiki/{new_title}')
        else:
            continue
    else:
        break