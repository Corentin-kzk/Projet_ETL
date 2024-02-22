import requests

class ListMonsters:

  headers = {
    'Accept': 'application/json'
  }

  def __init__(self, path):
    self.path = path

  def getApi(self, headers=headers):
    response = requests.get(self.path, headers)
    data = response.json()
    return data