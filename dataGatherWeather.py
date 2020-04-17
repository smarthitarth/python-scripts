# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:03:40 2020
web scrapping from this url: (Weather Data for windsor from 2010 - 2019)
url='https://en.tutiempo.net/climate/0{}-{}/ws-715380.html',format(month, year)			
@author: hitarh smart
"""
import os
import time
import requests
import sys

def retrieve_HTML():
	for year in range(2010,2019):
		for month in range(1,13):
		#	print(month)
			if(month<10):
				url='http://en.tutiempo.net/climate/0{}-{}/ws-715380.html'.format(month, year)
			
			else:
				url='http://en.tutiempo.net/climate/{}-{}/ws-715380.html'.format(month, year)
		#print(year, url)
			texts = requests.get(url)
			text_utf = texts.text.encode('utf=8')
		
			if not os.path.exists("Data/HTML_Data/{}".format(year)):
				os.makedirs("Data/HTML_Data/{}".format(year))
			with open("Data/HTML_Data/{}/{}.html".format(year, month),"wb") as output:
				output.write(text_utf)
			
		sys.stdout.flush()
		
if __name__ == "__main__":
	start_time = time.time()
	retrieve_HTML()
	stop_time = time.time()
	print("Time taken {}". format(stop_time - start_time))