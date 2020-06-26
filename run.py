#!/usr/bin/env python3
import os, glob
import requests

text_files = glob.glob("supplier-data/descriptions/*.txt")
keys = ["name", "weight", "description", "image_name"]
feed_list = []

#parsing through the text files
for files in text_files:
	with open(files,"r") as file:
        data = {}
        reader = file.read().split("\n")
        for i in range(len(keys)):
                data.update({keys[i]:reader[i]})
        img = files.replace(".txt",".jpeg")
        data.update({keys[3]:img})
        print(data)
        feed_list.append(data)

#convert the weight value to integer
for keys in feed_list:

	i = keys["weight"][:-3] #remove lbs in 500lbs
	keys["weight"] = i

for keys in feed_list:
	keys["weight"] = int(keys["weight"])

#feed data to the website
url = "http://localhost/fruits/"
for i in range(len(feed_list)):
	response = requests.post(url, json=feed_list[i])
	response.raise_for_status()