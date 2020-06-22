import urllib.request
import urllib.error
from lxml import etree
import csv
import unidecode
import time
from tqdm import tqdm
import json

dialogue_json = {}

def episode(link):
	time.sleep(0.1)
	article_page = link

	while True:
		# print(link)
		try:
			page = urllib.request.urlopen(article_page)
			htmlparser = etree.HTMLParser()
			tree = etree.parse(page, htmlparser)	
			text = tree.xpath('//text()')
		# /html/body/div/center/table/tbody/tr/td/p[1]/font/text()[1]
			return text

		except urllib.error.HTTPError:
			print("Error 404")
			return([None])
			# continue
		except urllib.error.URLError:
			print("Unknown Service")
			time.sleep(5)

def save_data(scenes,file_name):
	with open(file_name,"a+",encoding="UTF-8") as sfile:
		for s in scenes:
			sfile.write(" ".join(s)+"\n")

news_headline_2_lede = {}

for i in range(1,80):
		dialogue = episode("http://www.chakoteya.net/StarTrek/{}.htm".format(i))
		scenes = []
		for l in dialogue:
			for w in l.split():
				if ("[" in w or "{" in w) and w.split()[0] != '[OC]:'and w.split()[0] != '[OC}:':
					if len(scenes) > 0:
							print(scenes[-1])
					scenes.append([])

				if len(scenes) > 0:
					scenes[-1].append(w)

		save_data(scenes,"episode_chunks.txt")
