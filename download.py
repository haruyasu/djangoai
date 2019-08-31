from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

key = "c1b2c5effb97f2146a4b16d928740e2f"
secret = "0b4163e362c9e576"
wait_time = 1

keyword = sys.argv[1]
savedir = "./data/" + keyword

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = keyword,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'

    if os.path.exists(filepath):
        continue

    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
