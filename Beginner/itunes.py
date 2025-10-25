import json
import requests
import sys


if(len(sys.argv) != 2 ):
    sys.exit()

respond = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = respond.json()

for result in o['results']:
    print(result['trackName'])