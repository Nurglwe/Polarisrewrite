import keepalive
#No touch above
from better_profanity import profanity
from discord.ext import commands
import time,calendar,os,json,discord,requests,tools
from fuzzywuzzy import fuzz
profanity.load_censor_words_from_file("./storage/profanity.txt")
intents = discord.Intents.all() # Imports all the Intents
intents.members=True
client = commands.Bot(command_prefix="->",intents=intents)

@client.event
async def on_ready():
  print("Ready")

@client.command()
async def purge(ctx, no:int):
  await ctx.channel.purge(limit=no)



@client.command()
async def ping(ctx):
  await ctx.send('Pong, {} Ms'.format(round(client.latency * 1000,2)))


@client.event
async def on_member_join(payload):
  joins=tools.getjson("./storage/join.json")
  bans=tools.getjson("./storage/banned.json")
  ato=tools.alltheobject(client)
  invs= await ato.guild.invites()

  if str(payload.id) in bans:
    await payload.ban( reason = "On banned list")

  for invite in invs:
    y=invite.code
    if not(y in joins):
      b={y:1}
      joins.update(b)
      tools.writejson("./storage/join.json",joins)

    elif joins[y]<invite.uses:
      v={y:invite.uses}
      joins.update(v)
      tools.writejson("./storage/join.json",joins)

  embed=tools.embedhandler("User joined",0x008080,ato.delc,client)
  await tools.embedhandler.sendembed(embed, {"Username:":payload.name,"Tag:":payload.discriminator,"ID:":payload.id,"Join code:":y})
  
@client.event
async def on_member_remove(payload):
  print('Remove')
  ato=tools.alltheobject(client)
  embed=tools.embedhandler("Member left",0xFFA500,ato.delc,client)
  info={"Username:":payload.name,"Tag:":payload.discriminator,"ID:":payload.id}
  await tools.embedhandler.sendembed(embed,info)

@client.event
async def on_message_delete(message):
  ato=tools.alltheobject(client)
  embed = tools.embedhandler("Deleted message",0x01031f,ato.delc,client)
  await tools.embedhandler.sendembed(embed,{"Sent by:":str(message.author.name),"User ID:":str(message.author.id),"Message.ID":str(message.id),"Link:":"https://discordapp.com/channels/{}/{}/{}".format(message.guild.id,message.channel.id,message.id)})

@client.event
async def on_raw_message_delete(payload):
  embed = tools.embedhandler("Mass message deletion",0x000000,tools.alltheobject.guild,client)
  await tools.embedhandler.sendembed(embed, {"Message IDs:":payload.message_ids,"Amount of messages:":len(payload.message_ids)})





token=os.getenv("TOKEN")    
client.run(token)