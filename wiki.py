import requests
from bs4 import BeautifulSoup

def wiki_summary():
    user = input('what do you wanna know about? : ')
    formatted_input = user.replace(' ','_')
    url = f"https://en.wikipedia.org/wiki/{formatted_input}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        first_par = ''
        for p in soup.find_all('p'):
            if p.text.strip():
                first_par = p.text
                break

        if first_par:
            print(f"wikipedia summary of {user}:\n{first_par}")
        else:
            print('could not find it enter a valid name')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

print('Your PocketPedia:')
wiki_summary()
