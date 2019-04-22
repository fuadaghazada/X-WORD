from googlesearch import search, get_page, filter_result, get_random_user_agent

'''
	Searching a word via a query to Google Search Engine
	
	:param str word - the given word
	:param int stp - after how many result (index for last result) 
'''


def search_google(word, stp=5):
	# Search query
	query = str(word)

	query_result = search(query=query, tld='com', lang='en', num=5, start=0, stop=stp)

	results = []
	for res in query_result:
		res = filter_result(res)
		html = get_page(res, get_random_user_agent())

		results.append({'link': res, 'page': html})

	return results


# TEST
r = search_google('ICANT', 1)





