﻿import requests 
import sys 
import argparse


if __name__ == "__main__":
	
	print("\n\n<---------------------------------------------------------------------->")
	print("<----------------------------- krushna -------------------------------->")
	print("<---------------------------------------------------------------------->\n")
	

	parser = argparse.ArgumentParser()
	parser.add_argument('--u', help='Add valid URL (Ex: https://example.com)')
	parser.add_argument('--w', default='wd_main', choices=["wd_main","wd_common"], help='Choose Wordlist')

	args = parser.parse_args()
	url = args.u
	wd = args.w

	try:
		if (url is not None and wd is not None):
	
			
			if url[-1] != '/':
			    url += '/'
		
			wdname = wd+".txt"
	
			f = open(wdname, "r")
			for word in f:
				word = word.strip()
				final = url+word
			
				req = requests.get(final)
	
				if req.status_code != 200:
					print(final, end='\r')
				else:
					print("++++++++++++++++++++++++++ >   "+final+"\n")
	
	
		else:
			print('Please provide valid URL !')
			print('For more help use -h option\n\n')	

	except requests.exceptions.MissingSchema:
		print('Please provide corrrect URL  (eg: http://example.com  or  https://example.com)\n')