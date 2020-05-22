try:
	import requests
except:
	import os
	os.system('pip install requests')
import os 
os.system('clear')
url = input('Enter Website URL Here : ')
#print('Add http:// or https://')
par = input('Enter Parameter Here (eg : id =5 :- 5 is Parameter) : ') 
try:
	with open('pyload.txt') as payload:
		pass
except:
	print('Payload File Not Found...')
	print('If You Have A Custom File Add Ot To This Folder As pyload.txt')
	exit()

with open('pyload.txt') as payload:
	for i in payload:
		payloads = str(i)
		url1 = url.replace(par,payloads)
		urs= requests.get(url1)
		stc= (urs.status_code)
		if stc ==200 or '200':
			print(f'\nUrl : {url1}  :-Status : 200\n \n')
		elif stc == 403 or '403':
			print('\nUrl: {url1} Is Forbidden\n \n')
		else:
			print(f'Url : {url1} Not Found\n \n')
