import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Comment,Tag
from time import sleep
import csv
import sys
import os
import shutil 
import urllib
from urllib.parse import urlparse
import json

# create a directory to save images
directory = './images/'

if os.path.exists(directory):
	shutil.rmtree(directory)
	os.makedirs(directory)
else:
	os.makedirs(directory)

# create a csv file to save metadata including texts
csvfile = open('deardata.csv', 'w',newline='')
dearwriter = csv.writer(csvfile)

# write a header
dearwriter.writerow(['week', 'title', 'author', 'visual_img', 'legend_img', 'text'])

# retrieve project names and urls
url = 'http://www.dear-data.com/by-week/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser") # 

print("Scraping... ", url)
if(response.status_code != 200):
    print("You can't scrape ", url, ", status:", response.status_code)
    sys.exit()

projects = soup.find_all('a', attrs={'class':'project'})


# for each project
i = 0
while i<len(projects):#len(projects) 
	
	project = projects[i]

	# retrieve project info
	proj_url = 'http://www.dear-data.com' + project['href']
	title = project.find('div', attrs={'class':'project-title'})

	# derive week
	week = title.string.split(':')[0][-2:]

	print("Scraping... ", title.string)
	response = requests.get(proj_url)
	if(response.status_code != 200):
		print("You can't scrape this", response.status_code)
		if response.status_code==429:
			print('Too many requests, retry')
			sleep(5)
			continue
	i+=1

	html = response.text
	soup = BeautifulSoup(html, "html.parser") # 

	# remove comments 
	comments = soup.findAll(text=lambda text:isinstance(text, Comment))
	[comment.extract() for comment in comments]

	# find two blocks, each of which represents each designer

	blocks = soup.find_all('div', attrs={'class':['sqs-col-6']})
	if len(blocks)!=2:
		print('blocks in wrong format!') # check, there should be two columns
		exit()

	# for each designer
	authors = ['Giorgia', 'Stefanie']
	
	for block, author in zip(blocks, authors):
		row = [] # represents a csv row
		row.append(week) # week
		row.append(title.string) # title

		print(week, author)
		row.append(author)# author

		# find images (n=2, front and back)
		gallery = block.find('div', attrs={'class':'sqs-block-gallery'})
		# print(gallery)
		images = gallery.find_all('img', attrs={'class':'thumb-image'})
		# print(images)
		if len(images)!=2:
			print('images in wrong format!') # check, there should be two columns
			exit()
		for image in images:# two images
			# row.append(image['href'])
			filename = os.path.basename(urlparse(image['data-image']).path)
			filename = '_'.join([week,filename])
			row.append(filename)
			urllib.request.urlretrieve(image['data-image'],directory+filename)

		# extract text
		rest = block.find('div', attrs={'class':['sqs-col-5']})
		text_block = rest.contents[0].find('div', attrs={'class':'sqs-block-content'})
		
		# parse text
		text = []		
		for idx, child in enumerate(text_block.children):


			
			if idx==0 and child.name=='h2':
				continue
			elif child.name=='p':
				# cleaning - handling edge cases
				for e in child.find_all('br'):
					if e.previous_sibling is None:
						e.extract()
					else:
						e.insert_after(' ')
				# remove empty tags and other edge cases
				for e in child.find_all():
					if len(e.text)==0 or (e.name=='strong'and e.text=='Giorgia'):
						e.extract()				
					if e.name=='strong' and e.text.strip()=='THIS IS THE WORST CARD EVER.':
						e.name='span'
				# header within  a span...
				for span in child.find_all('span'):
					if span.previous_sibling is None and span.contents[0].name=='strong':# header exists
						for c in reversed(span.contents):
							span.parent.insert(0,c)
						span.extract()


				if len(child.text)==0:
					continue
				if child.contents[0].name=='strong':# header exists
					# print('----subheader', child.strong)
					segment = {'header':'', 'content':''}
					segment['header'] = child.contents[0].get_text().strip()
					text.append(segment)
					sibling = child.contents[0].next_sibling
					
					# same header separated by two strong tags
					if sibling is not None and sibling.name=='strong':
						segment['header'] += ' ' +sibling.get_text()
						sibling = sibling.next_sibling
					
					while sibling is not None:
						# if sibling.string is not None:
						if isinstance(sibling,NavigableString):
							segment['content'] += sibling.string
						else:
							segment['content'] += sibling.get_text()
						sibling = sibling.next_sibling
					# print(len(child.contents), list(map(lambda x:x, child.contents)))
				else: # otherwise
					if len(text)>0:
						# add it to the content of the header
						text[-1]['content']+=child.get_text()
					
					else:# if text is not separated by headers
						text.append({'header':'', 'content':child.get_text()})
			else:
				if len(text)>0:
					text[-1]['content']+=child.get_text()
				else:
					text.append({'header':'', 'content':child.get_text()})
		# row.append('$'.join(texts))	
		for item in text:
			print('header:', item['header']) 			
			print('content:', item['content'][:50])
		row.append(json.dumps(text))
		dearwriter.writerow(row)	
	