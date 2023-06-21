import spotify
import requests
import json

with open('./sections.json', 'r') as f:
    data = json.load(f)

token = spotify.getToken()

currentSong = spotify.getCurrentTrack(token)

print(currentSong['item']['name'])

id = currentSong['item']['id']
print("id:", id)

sections = spotify.getSongAnalysis(token, id)['sections']
print(sections)

drops = {}

for section in sections:
    print(section['mode'])
    if section['mode'] == 1 :
        drops[section['start']] = '255.255.255'

dropsLeft = {'left': drops}

with open('./sections.json', 'w') as f:
        json.dump(dropsLeft, f, indent=4)

print(spotify.getCurrentPosition(token)['timestamp'])