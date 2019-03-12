import requests
import random
import pymongo
from pymongo import MongoClient
import urllib

client = MongoClient()
db= client.recruit
collection1 = db.modi
collection2 = db.kejri
collection3 = db.training
collection4 = db.testing

cursor= collection1.find({})
count=1
for doc in cursor:
	print(count,doc['url'])
	try:
		urllib.urlretrieve(doc['url'], "modi/"+str(count)+".jpg")
		count+=1
	except:
		print("error")


cursor= collection2.find({})
count=1
for doc in cursor:
	print(count,doc['url'])
	try:
		urllib.urlretrieve(doc['url'], "kejri/"+str(count)+".jpg")
		count+=1
	except:
		print("error")