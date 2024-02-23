import requests

class ListMonsters:

  headers = {
    'Accept': 'application/json'
  }

  def __init__(self, path):
    self.path = path

  def getApi(self, headers=headers):
    try:
      response = requests.get(self.path, headers)
      data = response.json()
      return data
    except Exception as e:
      print(f"An error has occurred ==> {e}")
      raise