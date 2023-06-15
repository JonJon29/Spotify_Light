import requests

url = 'https://api.spotify.com/v1/me/player'

x = requests.post(url, headers = {"Authorization": "Bearer BQCoCCSoZApsGG7UCMf0x61yiyZ9nzeP-uBxc5KGHPkjzLSt7Pg7oxYyPrRd8V1mT5-TV9737V6R_CZmQJYA422YAQaZveqPEveG4Ay94d2yVTxKR1EQ5w9XJgji5gEX_-fkwJkHxLqLcTA4pcyIHrwU0n_soKyaBr2Rqh0WM04h4-eMMLktBbXzymSbBhE5wXn2W5Ovljy3fA"})

print(x.text)