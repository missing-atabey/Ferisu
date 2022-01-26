import random
import hikari
import lightbulb
import csv



plugin = lightbulb.Plugin("casuals")

#-------------------------
#   V A R I A B L E S
#-------------------------

#-------------------------------------------------------
#     I M P O R T   Q U O T E S  F R O M  T X T
#-------------------------------------------------------

manifesto_quotes = []

with open('misc/Manifesto.txt', 'r', encoding="utf-8") as fd:
    manifesto_quotes = fd.readlines()
        
che_quotes = []

with open('misc/Guevara.txt', 'r', encoding="utf-8") as fd:
    che_quotes = fd.readlines()
        
        

#-----------------------------
#     C O M M A N D S
#-----------------------------

@plugin.command
@lightbulb.command("salute", "Salutes Ferisu")
@lightbulb.implements(lightbulb.SlashCommand)
async def salute(ctx):
    await ctx.respond("I sawute you comwade! :3")
    

@plugin.command
@lightbulb.command("manifestoquote", "generates a random quote from The Communist Manifesto")
@lightbulb.implements(lightbulb.SlashCommand)
async def manifestoquote(ctx):
    await ctx.respond("Hewe's youw manifesto quote :)")
    
    eb = hikari.Embed(color="#e60000")
    eb.add_field("Communist Manifesto Quote:", random.choice(manifesto_quotes))
    eb.set_thumbnail("https://www.biography.com/.image/t_share/MTgwOTcxNTk5NTIyOTY0ODQw/gettyimages-515410892.jpg")
    
    await ctx.get_channel().send(eb)
    
@plugin.command
@lightbulb.command("chequote", "generates a random quote (in spanish) by Ernesto \"Che\" Guevara")
@lightbulb.implements(lightbulb.SlashCommand)
async def chequote(ctx):
    await ctx.respond("Hewe's youw Che quote :)")
    
    eb = hikari.Embed(color="#e60000")
    eb.add_field("Ernesto \"Che\" Guevara:", random.choice(che_quotes))
    eb.set_thumbnail("https://klimbim2014.files.wordpress.com/2018/06/che-guevara-color.jpg")
    
    await ctx.get_channel().send(eb)
    
    
#
#
#


def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)
