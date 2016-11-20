
def get_next_target():
	start_link = page.find('<a href=')
	if start_link == -1:
			return None, 0
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote


#page = contents of some web page as string
def print_all(page):
	while True:
		url, endpos=get_next_target(page)
		if url:
			print url
			page=page[endpos:]
		else:
			break

print_all(get_page('http://xkcd.com/353'))
## beautiful suite python library to process HTML pages  soup