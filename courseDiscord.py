import os
from courseLookup import lookup, allInfo
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def look(ctx, s, n):
    values = lookup(s.upper(), n)
    if("down" in values):
        await ctx.channel.send("Website is down! Try again in a little bit. :(")
    else:
        a,b,c,d,e = allInfo(values)
        if(not a):
            await ctx.channel.send("error! couldnt find the course.")
        else:
            index = 0
            i = 0
            flag = None
            while True:
                if(flag == True):
                    break
                while True:
                    embedVar = discord.Embed(title="Spring 2021", color=0x00ff00)
                    embedVar.add_field(name="Class Number", value =a[i], inline=True)
                    index+=1
                    embedVar.add_field(name="Course Info", value=b[i], inline=True)
                    index+=1
                    embedVar.add_field(name="Meeting Info", value=c[i], inline=True)
                    index+=1
                    embedVar.add_field(name="Seats", value=d[i], inline=True)
                    index+=1
                    embedVar.add_field(name="Comments", value=e[i], inline=False)
                    index+=1
                    i+=1
                    if(index == 23):
                        if(i == len(a)):
                            flag = True
                            break
                        index = 0
                        embedVar.add_field(name="\u200b", value="\u200b", inline = False)
                        await ctx.channel.send(embed=embedVar)
                        await ctx.channel.send("Here you go {}!".format(ctx.message.author.mention))
                        break
                    if(i == len(a)):
                        flag = True
                        await ctx.channel.send(embed=embedVar)
                        await ctx.channel.send("Here you go {}!".format(ctx.message.author.mention))
                        break
                    await ctx.channel.send(embed=embedVar)

@bot.command()
async def helpme(ctx):
    embedVar = discord.Embed(color=0x00ff00)
    embedVar.add_field(name="!look" ,value="<Subject 'CSI'> <Course Number '201'> ")
    await ctx.channel.send(embed=embedVar)



bot.run(TOKEN)