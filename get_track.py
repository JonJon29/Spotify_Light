import spotify
import requests
import json

token = spotify.getToken()

currentSong = spotify.getCurrentTrack(token)

print(currentSong['item']['name'])

id = currentSong['item']['id']

print(spotify.getSongAnalysis(token, id)['sections'])