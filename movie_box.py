import BeautifulSoup
import webbrowser
import requests
import csv
import re

# A-Z
letters = [chr(c) for c in range(65, 91)]
URL_a = "http://www.boxofficemojo.com/movies/alphabetical.htm?letter=" + letter + "&page=" + number "&p=.htm"
title_links = []
for letter in letters:
	for n in range(0,15):
		try:
			page =requests.get("http://www.boxofficemojo.com/movies/alphabetical.htm?letter=" + str(letter) + "&page=" + str(n) "&p=.htm")
			soup = BeautifulSoup(page.text, "html.parser")
			for link in soup.final_all("a")
				title = link.get("href")
				title_links.append(title)
		except HTTPError:
			print ('Error')
			pass
for movie in title_links:
	Box_office_data = requests.get(movie)
	soup = BeautifulSoup(Box_office_data.text, "html.parser")

	bold_info = soup.find_all("b") 
	bold_list = []

	titles = []   
	for b in bold_info:
		if len(bold_list)>=10:
			if 'n/a' in b_list[9]:  #no domestic release, only want domestic predictions
				pass	
			else:	#has a domestic release, what we want
				title=b_list[1]
				titles.append(title)
				domestic=b_list[2]
				genre=b_list[5]
				time=b_list[6]
				rating=b_list[7]
				budget=b_list[8]
		
	actors=soup.findAll('a', "href"= re.compile('Actor&id'))
	actor_list=[]
	for p in actors:
		actor_list.append(p.encode_contents())
	for p in range(0,2):
		actor1 =actor_list[0]
		actor2 = actor_list[1]

	director = soup.find_all("a", "href" = re.compile("Director&id"))
	director_list=[]
	for p in directors:
		director_list.append(p.encode_contents())
	for p in range(0,2):
		director1 = director_list[0]
		director2 = director_list[1]

	release_date = soup.find_all("a", "href" = re.compile("schedule"))
	release_list = []
	for d in release_list:
			release_list.append(d.encode_contents())
		release = release_list[0]	

with open("/home/emasterson/documents/python_proj/box_office.csv", "w") as f:
        fieldnames = ("title","domestic","genre,time","rating,budget","actor1","actor2","director1","director2","release")
        output = csv.writer(f, delimiter=",")
        output.writerow(fieldnames)
        


















