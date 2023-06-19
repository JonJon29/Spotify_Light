import requests 
import base64
import json

client_ID = ''
client_secret = ''
refresh_token = ''

join = client_ID + ":" + client_secret
bytes = join.encode('ascii')
encoded = base64.b64encode(bytes)

def getToken():
    url = 'https://accounts.spotify.com/api/token'
    body = {
        'grant_type' : 'refresh_token',
        'refresh_token' : refresh_token,
        }
    headers = {
        'Authorization': "Basic " + encoded.decode("utf-8") ,
        'Content-Type': 'application/x-www-form-urlencoded'}

    res = requests.post(url, data=body, headers=headers)
    dict = json.loads(res.text)

    return dict['access_token']

def getCurrentTrack(token):
    url = 'https://api.spotify.com/v1/me/player/currently-playing'
    headers = {
        'Authorization' : 'Bearer ' + str(token)
    }

    res = requests.get(url, headers=headers)
    song = json.loads(res.text)

    return song

def getSongAnalysis(token, id):
    url = 'https://api.spotify.com/v1/audio-analysis/' + id

    headers = {
            'Authorization' : 'Bearer ' + str(token)
        }
    res = requests.get(url, headers=headers)
    analysis = json.loads(res.text)

    return analysis

def getCurrentPosition(token):
    url = 'https://api.spotify.com/v1/me/player'

    headers = {
            'Authorization' : 'Bearer ' + str(token)
        }
    res = requests.get(url, headers=headers)
    player = json.loads(res.text)

    return player
