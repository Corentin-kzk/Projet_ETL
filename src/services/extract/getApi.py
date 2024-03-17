import requests
import json

url_dnd5eapi = "https://www.dnd5eapi.co/api/monsters"

headers = {
  'Accept': 'application/json'
}
def getMonstersListApi(url: str):
  response = requests.get(url, headers=headers)
  data = response.json()
  return data