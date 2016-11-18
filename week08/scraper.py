import requests as r
import json

BASE_URL = 'http://pokeapi.co/api/v2/'

def get_pokemon_data(pokenumber):
	request_url = BASE_URL + 'pokemon/%s' % pokenumber
	pokedata = r.get(request_url)
	return pokedata.json()

with open('bulbasaur.txt', 'w') as outfile:
	json.dump(get_pokemon_data(1), outfile)