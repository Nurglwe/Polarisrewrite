import json
class getjson():
  def getjson(path):
    with open(path,"r") as f:
      return json.load(f)
