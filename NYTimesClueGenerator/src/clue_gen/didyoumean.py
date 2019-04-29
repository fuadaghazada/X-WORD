from bs4 import BeautifulSoup
from googlesearch import get_page


'''
    Parsing for 'Did You Mean'

    :param str query - the given query
    :return str or None result - the corrected (meant) version of query
'''


def did_you_mean(query, trace = False):
    try:
        # Trace
        if trace is True:
            print("\t\t\"Did You Mean (from Google) check\" for the query: \"" + query + "\"")

        # query = str(query).strip()
        html = get_page('http://www.google.com/search?q=' + query)
        soup = BeautifulSoup(html, 'html.parser')

        answer = soup.find('a', attrs={'class': 'gL9Hy'})

        result = answer.find('i') if answer is not None else None
        result = result.text if result is not None else None

        # Trace
        if trace is True and result is None:
            print("\t\tNo correction from \"Did You Mean check\" for the query: \"" + query + "\"\n")
        else:
            print("\t\t\"" + query + "\" is replaced with \"" + result +"\"\n")

        return result
    except Exception as e:
        pass

    # Trace
    if trace is True:
        print("\t\tPassed \"Did You Mean check\" for the query: \"" + query + "\"\n")

    return None
