import hikari
import lightbulb
import misc.config as cf
from plugs import osu_extensions, casuals
import csv


client = lightbulb.BotApp(cf.dc_token, default_enabled_guilds=cf.dc_guilds)


#-----------------------------------
# IMPORT BANNED TERMS FOR AUTOMOD
#-----------------------------------

b_words = []

with open('misc/bannedwords.txt', 'r') as fd:
    b_words = fd.readlines()

#--------------------
#   E V E N T S
#--------------------

@client.listen(hikari.MessageCreateEvent)
async def hi_ferisu(event):
    if event.content is None:
        return

    #Automod
    for i in b_words:
        if i.lower() in event.content.lower():
            await event.message.delete()
            await event.get_channel().send("Naughty " + event.author.username + "!! don't say those wowds!")
            return

    #Hey ferisu reply
    if ("hi ferisu" in event.content.lower() or "hey ferisu" in event.content.lower()) and hikari.MessageCreateEvent.author:
        await event.get_channel().send("Hoi :3")

    #ping pong
    elif event.content.lower() == "ping":
        await event.get_channel().send("pong")


#------------------------------------
#    P L U G I N  I M P O R T S
#------------------------------------

osu_extensions.load(client)
casuals.load(client)


client.run()
