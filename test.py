import spotify 

token = spotify.getToken()

print(token)

print(spotify.startPlayback(token, '4a5pNRjwmzYQuEY1E7O6pj'))