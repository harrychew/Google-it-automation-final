
#!/usr/bin/env python3
import requests
import glob


url = "http://localhost/upload/"
for files in glob.glob("supplier-data/images/*.jpeg"):
	with open(files, 'rb') as file:
		r = requests.post(url, files={'file': file})
