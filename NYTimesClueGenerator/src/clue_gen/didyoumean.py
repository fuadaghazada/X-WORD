from bs4 import BeautifulSoup
from googlesearch import get_page


'''
    Parsing for 'Did You Mean'

    :param str query - the given query
    :return str or None result - the corrected (meant) version of query
'''


def did_you_mean(query):
    try:
        # query = str(query).strip()
        html = get_page('http://www.google.com/search?q=' + query)
        soup = BeautifulSoup(html, 'html.parser')

        answer = soup.find('a', attrs={'class': 'gL9Hy'})

        result = answer.find('i') if answer is not None else None
        result = result.text if result is not None else None

        return result
    except Exception as e:
        raise

    return None
