import requests 

import sys 

import argparse

from datetime import datetime





if __name__ == "__main__":

	

	print('\n		 _   __  ')
	print('		| | / / ')
	print('		| |/ / ')
	print('		| |\ \ ')
	print('		| | \ \ ')


		

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




	try:

		if (url is not None and wd is not None):

	

			print("----------------------------------------------------")	

			print(" Date		-      ",dt_string)	

			print(" Wordlist 	-	"+wdname)	

			print(" URL		- 	"+url)
			print("\n 	Word Count: ", count)

			print("----------------------------------------------------\n")	

			

			if url[-1] != '/':

			    url += '/'


	

			f = open(wdname, "r")

			for word in f:

				word = word.strip()

				final = url+word

			

				req = requests.get(final, allow_redirects=False)

				code = req.status_code
				

				if code== 200 or code== 202 or code== 204 or code== 302 or code== 400 or code== 401 or code== 403 or code== 405 or code== 408 or code== 500 or code== 501 or code== 502 or code== 503 or code== 504:

					print(" +++ > "+final+" (code:"+str(code)+")")
				else:	

					print(final, end='\r')

	

	

		else:

			print('\nPlease provide valid URL !')

			print('For more help use -h option\n\n')	



	except requests.exceptions.MissingSchema:

		print('Please provide corrrect URL  (eg: http://example.com  or  https://example.com)\n')



	except requests.exceptions.ConnectionError:

		print("\n")


	except requests.exceptions.TooManyRedirects:
		print("\n")

	except KeyboardInterrupt:
		print("\nExit\n")
