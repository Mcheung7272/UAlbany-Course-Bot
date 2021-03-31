import os
from courseLookup import lookup, allInfo
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
import sqlite3

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

conn = sqlite3.connect(SQL DATABASE)
c = conn.cursor()

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

@bot.command(name='whatis')
async def basicLookup(ctx, prefix, num):
    if 'DROP' in prefix.upper() or '(' in prefix or ')' in prefix or '*' in prefix:
        await ctx.send('No. Stop trying.')
        return
    elif 'DROP' in num.upper() or '(' in num or ')' in num or '*' in num:
        await ctx.send('No. Stop trying.')
        return
    if prefix.upper() == 'AMAT':
        prefix = 'MAT'
    c.execute('SELECT * FROM ualbany_courses WHERE Subject_Prefix LIKE ? AND Subject_Number LIKE ?', ('%' + prefix.upper() + '%',num + '%',))
    together = c.fetchone()
    embedVar = discord.Embed(title="Course Lookup for " + prefix.upper() + ' ' + num, color=0x00ff00)
    embedVar.add_field(name="Course Name", value=together[2] + ' | ' + together[0] + ' ' + together[1], inline=False)
    embedVar.add_field(name="Course Description", value=together[3], inline=False)
    embedVar.add_field(name="Subject", value=together[4], inline=False)
    await ctx.send(embed=embedVar)
        
@bot.command(name='subjects')
async def allSubjects(ctx):
    prefix = []
    f = open("prefix.txt", 'r')
    for line in f:
        prefix.append(line.replace('\n', ''))
    c.execute('SELECT DISTINCT subject FROM ualbany_courses')
    together = c.fetchall()
    word = ''
    for i in range(len(together)):
        word = word + (str)(together[i]).replace('(','').replace(')', '').replace(',', '').replace("'", '').replace('"', '') + ' ' + (str)(prefix[i]).replace(',', '').replace("'", '').replace('"', '') + '\n'
    await ctx.send(""" ```\nSubject and Prefix:\n \n{}\nSubjects Missing: Art, Communication, Global History, Music, Portuguese\n```""".format(word))

@bot.command(name='coursesfor')
async def coursesFor(ctx, subject):
    if ctx.author.id == (int)('274354935036903424'):
        await ctx.send('Go away James. Stop trying to drop my tables.')
        return
    if 'DROP' in subject.upper() or '(' in subject or ')' in subject or '*' in subject:
        await ctx.send('No. Stop trying.')
        return
    c.execute('SELECT * FROM ualbany_courses WHERE Subject_Prefix = ?', (subject.upper(),))
    together = c.fetchall()
    if len(together) == 0:
        await ctx.send('Zero Results. Make sure you searched with proper prefix. Use !subjects if you need it.')
        return
    skipped = []
    for i in range(len(together)):
        try:
            embedVar = discord.Embed(title="Courses for " + subject.upper(), color=0x00ff00)
            embedVar.add_field(name="Course Name, Prefix & Number:", value=together[i][2] + ' | ' + together[i][0] + ' | ' + together[i][1], inline=False)
            embedVar.add_field(name="Course Description", value=together[i][3], inline=False) 
            await ctx.send(embed=embedVar)
        except:
            skipped.append('Skipped lookup for ' + together[i][2] + ' | ' + together[i][0] + ' | ' + together[i][1] + '. Description too long to embed.')
            continue
    if(len(skipped) > 0):
        for x in skipped:
            await ctx.send(x)
    
@bot.command()
async def helpme(ctx):
    embedVar = discord.Embed(color=0x00ff00)
    embedVar.add_field(name="!look" ,value="<Subject 'CSI'> <Course Number '201'> ")
    await ctx.channel.send(embed=embedVar)

@basicLookup.error
async def basicLookupError(ctx,error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Sorry, Bad arguments. Please try again. Make sure you search by proper prefix and number. Use !subjects if you need the proper prefix.')
    if isinstance(error, commands.CommandError):
        await ctx.send("Sorry, couldn't find the class. Make sure you search by proper prefix and number. Use !subjects if you need the proper prefix.")

@coursesFor.error
async def coursesForerror(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Sorry, Bad arguments. Please try again. Make sure you search by proper prefix and number. Use !subjects if you need the proper prefix.')




bot.run(TOKEN)
