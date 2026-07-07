import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    # terminate the whole program
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=3))
# jSON for pretty printing


o = response.json()
for result in o["results"]:
    print(result["trackName"])