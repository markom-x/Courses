import json
import requests
import sys
if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ sys.argv[1])
r = response.json()
#kljlkj


    
for result in r["results"]:
    print(result["trackName"])
