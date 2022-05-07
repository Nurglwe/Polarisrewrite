import json,discord,os

def getjson(path):
  with open(path,"r") as f:
    return json.load(f)

def writejson(path,data):
  with open(path,"w")as f:
    json.dump(data,f)

def getdiscordutils(objects,key):
  return discord.utils.get(objects, id=int(os.getenv("{}".format(key))))

class embedhandler:
  def __init__(self,title,colour,channel,client):
    self.title=title
    self.colour=colour
    self.sendto=channel
    self.client=client
  async def sendembed(self,args):
    embed=discord.Embed(title=self.title,colour=self.colour)
    keys=list(args.keys())
    vals=list(args.values())
    for i in range(len(vals)):
      embed.add_field(name=keys[i],value=vals[i],inline=False)
    if not(self.channel is None):
      await self.sendto.send(embed=embed)


class alltheobject:
  def __init__(self,client):
    self.guild=discord.utils.get(client.guilds,id=int(os.getenv("GUILD")))
    self.delc=discord.utils.get(self.guild.channels,id=int(os.getenv("DELC")))
