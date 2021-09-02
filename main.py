import keepalive
#No touch above
from better_profanity import profanity
from discord.ext import commands
import time,calendar,os,json,discord,requests,tools
from fuzzywuzzy import fuzz
#profanity.load_censor_words_from_file("profanity.txt")
client = commands.Bot(command_prefix="->")
traindex = []
def testing():
  target=tools.getjson.getjson("./storage/banned.json")
  print(target)
testing()