import requests
import random
import pymongo
from pymongo import MongoClient

client = MongoClient()
db= client.recruit
collection1 = db.modi
collection2 = db.kejri
collection3 = db.training
collection4 = db.testing

query = "Narendra Modi"
r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 250,
        'q': query,
        't': 'images',
        'safesearch': 10,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gec$'
    }
)

response = r.json().get('data').get('result').get('items')
urls = [r.get('media') for r in response]
print(urls)
for url in range(len(urls)):
    dic= {"url" : urls[url], "label" : query}
    if url<=200:
        temp=collection1.insert_one(dic).inserted_id
        temp1=collection3.insert_one(dic).inserted_id
    else:
        temp=collection4.insert_one(dic).inserted_id

    #print(temp)

query = "Arvind Kejriwal"
r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 250,
        'q': query,
        't': 'images',
        'safesearch': 10,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gec$'
    }
)
response = r.json().get('data').get('result').get('items')
urls = [r.get('media') for r in response]
for url in range(len(urls)):
    dic= {"url" : urls[url], "label" : query}
    if url<=200:
        temp=collection2.insert_one(dic).inserted_id
        temp1=collection3.insert_one(dic).inserted_id
    else:
        temp=collection4.insert_one(dic).inserted_id

    #print(temp)