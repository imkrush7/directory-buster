import requests 

import sys 

import argparse

from datetime import datetime





if __name__ == "__main__":

	

	print('\n\n		 _   __  ')
	print('		| | / / ')
	print('		| |/ / ')
	print('		| |\ \ ')
	print('		| | \ \ \n\n')


		

	parser = argparse.ArgumentParser()

	parser.add_argument('--u', help='Add valid URL (Ex: https://example.com)')

	parser.add_argument('--w', default='wd_common', choices=["wd_main","wd_common"], help='Choose Wordlist')



	args = parser.parse_args()

	url = args.u

	wd = args.w

	


	count = 0
	wdname = wd+".txt"
	with open(wdname, 'r') as f:
	    for line in f:
	        count += 1



	now = datetime.now()

	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")



	print("----------------------------------------------------\n")	

	print(" Date		-      ",dt_string)	

	print(" URL		- 	"+url)

	print(" Wordlist 	-	"+wdname)	
	print("\n 	Word Count: ", count, "\n")

	print("----------------------------------------------------\n")	



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

					print("++++++++++++++++++++++++++ >   "+final)

	

	

		else:

			print('Please provide valid URL !')

			print('For more help use -h option\n\n')	



	except requests.exceptions.MissingSchema:

		print('Please provide corrrect URL  (eg: http://example.com  or  https://example.com)\n')



	except requests.exceptions.ConnectionError:

		print("\n")


	except KeyboardInterrupt:
		print("\nExit\n")
