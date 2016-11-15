# Buiding a primitive search engine in python without the use of exteral libraries 
# using inverted indexes to add keywords and URLs
# Course work for Udacity's Search Engine Course


def add_to_index(index, keyword, url):

	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return


	index.append([keyword,[url]])
	
def lookup(index,keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return []


def add_page_to_index(index,url,content):
	words = content.split()
	for i in words:
		add_to_index(index, i, url)

def get_page(url):
	try:
		import urllib
	 	return urllib.urlopen(url).read()
	except:
		return ""
		

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
	return index



index = []
add_to_index(index,'udacity','http://udacity.com')
add_page_to_index(index, 'fake.test', "Another something judgement learn")
print index
print lookup(index, 'something')
