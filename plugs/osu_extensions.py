import misc.config as cf
import lightbulb
import hikari
from ossapi import *
import numpy as np
import matplotlib.pyplot as plt



plugin = lightbulb.Plugin("osu_commands")
osu_api = OssapiV2(cf.OSU_cid, cf.OSU_CS)


@plugin.command
@lightbulb.option("uid", "The ID number or username of the player")
@lightbulb.option("request", "what to look for (profile, location, pp, global, local, time, style, medals")
@lightbulb.command("osu", "OSU! command group")
@lightbulb.implements(lightbulb.SlashCommand)
async def osu_group(ctx):

    #Location Request
    if (ctx.options.request.lower() == "location"):
        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return
        
        await ctx.respond("Hewe's dat pwayews " + ctx.options.request.lower() + " <3")

        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)

        eb.set_thumbnail(op.avatar_url)
        eb.add_field("Location:", op.country.name, inline=True)

        await ctx.get_channel().send(embed=eb)
    #Playstyle Request
    elif (ctx.options.request.lower() == "style"):
        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return
        
        
        await ctx.respond("Hewe's dat pwayews " + ctx.options.request.lower() + " <3")

        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)

        eb.set_thumbnail(op.avatar_url)
        
        try:
            ps =  str(op.playstyle).split(".")[1]
        except:
            ps = "N/A"

        eb.add_field("Playstyle:", ps, inline=True)

        await ctx.get_channel().send(embed=eb)
    #GetPlaytime
    elif (ctx.options.request.lower() == "time"):
        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return
        
        await ctx.respond("Hewe's dat pwayews " + ctx.options.request.lower() + " <3")

        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)

        eb.set_thumbnail(op.avatar_url)
        eb.add_field("Playtime:", str(round(op.statistics.play_time/86400, 2)) + " days", inline=True)

        await ctx.get_channel().send(embed=eb)
    #Get PP
    elif (ctx.options.request.lower() == "pp"):
        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return
        
        await ctx.respond("Hewe's dat pwayews " + ctx.options.request.lower() + " <3")

        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)

        eb.set_thumbnail(op.avatar_url)
        eb.add_field("PP:", str(round(op.statistics.pp, 2)), inline=True)

        await ctx.get_channel().send(embed=eb)
    #Get medals
    elif (ctx.options.request.lower() == "medals"):
        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return
        
        await ctx.respond("Hewe's dat pwayews " + ctx.options.request.lower() + " <3")

        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)

        eb.set_thumbnail(op.avatar_url)
        eb.add_field("Medals:", str(len(op.user_achievements)), inline=True)

        await ctx.get_channel().send(embed=eb)
    #Get Local
    elif (ctx.options.request.lower() == "local"):
        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return
        
        await ctx.respond("Hewe's dat pwayews " + ctx.options.request.lower() + " rank <3")

        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)

        eb.set_thumbnail(op.avatar_url)
        eb.add_field("Local Rank:", str(op.statistics.country_rank), inline=True)

        await ctx.get_channel().send(embed=eb)
    #Get global
    elif (ctx.options.request.lower() == "global"):
        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return
        
        await ctx.respond("Hewe's dat pwayews " + ctx.options.request.lower() + " rank <3")

        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)

        eb.set_thumbnail(op.avatar_url)
        eb.add_field("Global Rank:", str(op.statistics.global_rank), inline=True)

        await ctx.get_channel().send(embed=eb)
    elif(ctx.options.request.lower() == "profile"):

        try:
            op = osu_api.user(ctx.options.uid)
        except ValueError:
            await ctx.respond("Dat pwayew doesn't exist :(")
            return

        await ctx.respond("Hewe's dat pwayews info <3")

        try:
            ps =  str(op.playstyle).split(".")[1]
        except:
            ps = "N/A"


        #Embed Creation
        eb = hikari.Embed(title=ctx.options.uid, url="https://osu.ppy.sh/users/" + ctx.options.uid)
        eb.color=hikari.Color.of(cf.OSU_EBC)


        eb.add_field("Location:", op.country.name, inline=True)
        eb.add_field("Playstyle:", ps, inline=True)
        eb.add_field("Playtime:", str(round(op.statistics.play_time/86400, 2)) + " days", inline=True)
        eb.add_field("Medals:", str(len(op.user_achievements)),inline=True)
        eb.add_field("PP:", str(round(op.statistics.pp, 2)),inline=True)
        eb.add_field("Global Rank:",str(op.statistics.global_rank),inline=True)
        eb.add_field("Local Rank:",str(op.statistics.country_rank),inline=True)

        eb.set_thumbnail(op.avatar_url)

        #Generate line graph
        try:
            x =list(range(90))
            x.reverse()

            try:
                y = op.rank_history.data
            except:
                y = [0] * 90

            fig = plt.figure(figsize=(12,5))
            ax = fig.add_subplot()
    
            ax.plot(x,y, color="pink", linewidth=2)
    
            plt.xticks(np.arange(min(x), max(x), 5))
    
            plt.title(ctx.options.uid + "'s Latest Rank History")
            plt.xlabel("Days ago")
            plt.ylabel("Rank")
    
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(False)
    
    
            plt.gca().invert_xaxis()
            plt.gca().invert_yaxis()
    
            plt.ticklabel_format(style='plain')
    
            plt.savefig("stat_hist.png")
            plt.cla()
            eb.set_image("stat_hist.png")
        except AttributeError:
            pass
            

        await ctx.get_channel().send(embed=eb)

    else:
        await ctx.respond("Invawid sewection :(")



def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)