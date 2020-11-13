import discord
import random
from mcstatus import MinecraftServer
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import requests
import json
import base64
import urllib.parse
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import twitter
import os
import numpy as np
import aiohttp



client=discord.Client()
INFO = open('commands.md', 'r')
INFOTEXT = INFO.read()



bot = commands.Bot(command_prefix='+', description="Hello i am Kemics Bot")
bot.remove_command('help')



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.listening, name="+commands"))
    bot.remove_command('help')


    
@bot.command()
async def appuz(ctx):
    if ctx.author.id == 508894910582226954:
        await ctx.send("you cant do this")
    else:
        await ctx.send("https://tenor.com/view/fortnite-vs-minecraft-floss-dance-gif-15393970")


        
        
        
@bot.command(pass_context=True)
async def giphy(ctx, *, search):

    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=IqNaLrLXKz1MsOXRfRVYUGyH4hbmNZfC')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=IqNaLrLXKz1MsOXRfRVYUGyH4hbmNZfC&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()
    await ctx.send(embed=embed)

    
    
    
    
@bot.command()
async def snape(ctx):
    await ctx.send("https://tenor.com/view/oh-no-udint-snape-harry-potter-oh-no-udidnt-severus-snape-gif-15145672")


    
@bot.command()
async def command(ctx):
    embed = discord.Embed(title="Commands help", description="{}".format(INFOTEXT),timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    await ctx.send(embed=embed)



@bot.command()

async def twitter(ctx):


    import twitter
    import json
    CONSUMER_KEY = 'gzHlo3jDG5K2uuhG3gueLVzGO'
    CONSUMER_SECRET = 'vx5F2CDYGLatSUTzUXpRN6uyePVo4mUUkj1gR5tPS3EeFz6XYj'
    OAUTH_TOKEN = '1293871946463981570-9C3lyLNyPHWn0H6RbMBABhiBZ2hzvO'
    OAUTH_TOKEN_SECRET = 'JV2428J9ZOQ4JPQPy4mOvAxBTvt0cB77esZE0Zjc7jGTU'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    INDIA_WOE_ID = 23424848
    india_trends = twitter_api.trends.place(_id=INDIA_WOE_ID)
    tmp = []



    for trending in india_trends[0]['trends']:
        nam=trending['name']
        tmp.append("```"+nam+"```")

    tempo="".join(tmp)
    embed = discord.Embed(title="Trending in India", description=f"{tempo}",timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    await ctx.send(embed=embed)







@bot.command()
async def twitterglobal(ctx):


    import twitter
    import json
    CONSUMER_KEY = '#'
    CONSUMER_SECRET = #'
    OAUTH_TOKEN = '#O'
    OAUTH_TOKEN_SECRET = '#'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    INDIA_WOE_ID = 1
    india_trends = twitter_api.trends.place(_id=INDIA_WOE_ID)
    tmpr = []



    for trending in india_trends[0]['trends']:
        nam=trending['name']
        tmpr.append("```"+nam+"```")

    tempo="".join(tmpr)
    embed = discord.Embed(title="Trending WorldWide", description=f"{tempo}",timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    await ctx.send(embed=embed)



@bot.command()
async def bans(ctx):
    async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.ban):
        await ctx.send('{0.user} banned {0.target}'.format(entry))


@bot.command()
async def info(ctx):


    embed = discord.Embed(title=f"{ctx.guild.name}", description="Official discord server of Arun Triads", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(),)
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/729329283251830855/753947641196576808/ATG_Avatar_Icon.jpg")

    print("works")

    await ctx.send(embed=embed)

@bot.command()
async def users(ctx):


    embed = discord.Embed(title=f"{ctx.guild.name}", description="Official discord server of Arun Triads",timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())

    embed.add_field(name="Member count", value=f"{ctx.guild.member_count}")
    embed.set_thumbnail(url="https://i.ibb.co/LRFZ3Td/Ke-Mi-CS-Icon-in-Black.jpg")
    await ctx.send(embed=embed)


    
    
@bot.command()
async def triads(ctx):


        from apiclient.discovery import build

        class YoutubeSubscriberCount(object):
            def __init__(self, api_key='#'):
                self.api_key = api_key
                self.youtube = build('youtube', 'v3', developerKey=api_key)

            @property
            def get(self):
                res = self.youtube.channels().list(id="UCoEVb6S2u7PL5pABBMp8x-A", part="statistics").execute()
                return res['items'][0]['statistics']['subscriberCount']

            @property
            def got(self):
                res = self.youtube.channels().list(id="UCoEVb6S2u7PL5pABBMp8x-A", part="statistics").execute()
                return res['items'][0]['statistics']['viewCount']

            @property
            def video(self):
                res = self.youtube.channels().list(id="UCoEVb6S2u7PL5pABBMp8x-A", part="statistics").execute()
                return res['items'][0]['statistics']['videoCount']

            @property
            def comments(self):
                res = self.youtube.channels().list(id="UCoEVb6S2u7PL5pABBMp8x-A", part="statistics").execute()
                return res['items'][0]['statistics']['commentCount']

        obj = YoutubeSubscriberCount()

        embed = discord.Embed(title="Arun Triads Youtube  ", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="  Subscribers  ", value="```"     f"{obj.get}"   "```")
        embed.add_field(name="   Views   ", value="```"f"{obj.got}""```")
        embed.insert_field_at(index=5,name="   Total Videos Uploaded   ", value="```"f"{obj.video}""```")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/729329283251830855/753947641196576808/ATG_Avatar_Icon.jpg")
        print("works")
        await ctx.send(embed=embed)


        
        
        
@bot.command()
async def pewds(ctx):

        from apiclient.discovery import build

        class YoutubeSubscriberCount(object):
            def __init__(self, api_key='#'):
                self.api_key = api_key
                self.youtube = build('youtube', 'v3', developerKey=api_key)

            @property
            def get(self):
                res = self.youtube.channels().list(id="UC-lHJZR3Gqxm24_Vd_AJ5Yw", part="statistics").execute()
                return res['items'][0]['statistics']['subscriberCount']

            @property
            def got(self):
                res = self.youtube.channels().list(id="UC-lHJZR3Gqxm24_Vd_AJ5Yw", part="statistics").execute()
                return res['items'][0]['statistics']['viewCount']

            @property
            def video(self):
                res = self.youtube.channels().list(id="UC-lHJZR3Gqxm24_Vd_AJ5Yw", part="statistics").execute()
                return res['items'][0]['statistics']['videoCount']

            @property
            def comments(self):
                res = self.youtube.channels().list(id="UC-lHJZR3Gqxm24_Vd_AJ5Yw", part="statistics").execute()
                return res['items'][0]['statistics']['commentCount']

        obj = YoutubeSubscriberCount()



        embed = discord.Embed(title="Pewdiepie Youtube  ", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="  Subscribers  ", value="```"     f"{obj.get}"   "```")
        embed.add_field(name="   Views   ", value="```"f"{obj.got}""```")
        embed.insert_field_at(index=5,name="   Total Videos Uploaded   ", value="```"f"{obj.video}""```")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/729329283251830855/747670153491120128/5339509023269a4a019da5ec9e2a276b.jpg")
        print("works")
        await ctx.send(embed=embed)



        
@bot.command()
async def aswin(ctx):
    from apiclient.discovery import build

    class YoutubeSubscriberCount(object):
        def __init__(self, api_key=#'):
            self.api_key = api_key
            self.youtube = build('youtube', 'v3', developerKey=api_key)

        @property
        def get(self):
            res = self.youtube.channels().list(id="UCkTKN2BwU3Wlvy0HO-QQLWw", part="statistics").execute()
            return res['items'][0]['statistics']['subscriberCount']

        @property
        def got(self):
            res = self.youtube.channels().list(id="UCkTKN2BwU3Wlvy0HO-QQLWw", part="statistics").execute()
            return res['items'][0]['statistics']['viewCount']

        @property
        def video(self):
            res = self.youtube.channels().list(id="UCkTKN2BwU3Wlvy0HO-QQLWw", part="statistics").execute()
            return res['items'][0]['statistics']['videoCount']

        @property
        def comments(self):
            res = self.youtube.channels().list(id="UCkTKN2BwU3Wlvy0HO-QQLWw", part="statistics").execute()
            return res['items'][0]['statistics']['commentCount']

    obj = YoutubeSubscriberCount()

    embed = discord.Embed(title=" Scary Ghost Gaming  ", description="", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="  Subscribers  ", value="```"     f"{obj.get}"   "```")
    embed.add_field(name="   Views   ", value="```"f"{obj.got}""```")
    embed.insert_field_at(index=5, name="   Total Videos Uploaded   ", value="```"f"{obj.video}""```")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/729329283251830855/756462099613614110/unnameddf.jpg")
    print("works")
    await ctx.send(embed=embed)



    
@bot.command()
async def nobi(ctx):
    from apiclient.discovery import build

    class YoutubeSubscriberCount(object):
        def __init__(self, api_key=#'):
            self.api_key = api_key
            self.youtube = build('youtube', 'v3', developerKey=api_key)

        @property
        def get(self):
            res = self.youtube.channels().list(id="UC4fsEDhxGMWfPZhcGN8cQMQ", part="statistics").execute()
            return res['items'][0]['statistics']['subscriberCount']

        @property
        def got(self):
            res = self.youtube.channels().list(id="UC4fsEDhxGMWfPZhcGN8cQMQ", part="statistics").execute()
            return res['items'][0]['statistics']['viewCount']

        @property
        def video(self):
            res = self.youtube.channels().list(id="UC4fsEDhxGMWfPZhcGN8cQMQ", part="statistics").execute()
            return res['items'][0]['statistics']['videoCount']

        @property
        def comments(self):
            res = self.youtube.channels().list(id="UC4fsEDhxGMWfPZhcGN8cQMQ", part="statistics").execute()
            return res['items'][0]['statistics']['commentCount']

    obj = YoutubeSubscriberCount()

    embed = discord.Embed(title=" Nobzz Gaming  ", description="", timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.blue())
    embed.add_field(name="  Subscribers  ", value="```"     f"{obj.get}"   "```")

    embed.add_field(name="   Views   ", value="```"f"{obj.got}""```")
    embed.insert_field_at(index=5, name="   Total Videos Uploaded   ", value="```"f"{obj.video}""```")

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/729329283251830855/756463273842573332/unnamed.jpg")

    

    print("works")

    await ctx.send(embed=embed)


@bot.command()
async def cruzo(ctx):
    from apiclient.discovery import build

    class YoutubeSubscriberCount(object):
        def __init__(self, api_key='#'):
            self.api_key = api_key
            self.youtube = build('youtube', 'v3', developerKey=api_key)

        @property
        def get(self):
            res = self.youtube.channels().list(id="UCyx8hcDUyTpeGdPql-s4Jkg", part="statistics").execute()
            return res['items'][0]['statistics']['subscriberCount']

        @property
        def got(self):
            res = self.youtube.channels().list(id="UCyx8hcDUyTpeGdPql-s4Jkg", part="statistics").execute()
            return res['items'][0]['statistics']['viewCount']

        @property
        def video(self):
            res = self.youtube.channels().list(id="UCyx8hcDUyTpeGdPql-s4Jkg", part="statistics").execute()
            return res['items'][0]['statistics']['videoCount']

        @property
        def comments(self):
            res = self.youtube.channels().list(id="UCyx8hcDUyTpeGdPql-s4Jkg", part="statistics").execute()
            return res['items'][0]['statistics']['commentCount']

    obj = YoutubeSubscriberCount()

    embed = discord.Embed(title=" Cruzo Gaming  ", description="", timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.blue())
    embed.add_field(name="  Subscribers  ", value="```"     f"{obj.get}"   "```")

    embed.add_field(name="   Views   ", value="```"f"{obj.got}""```")
    embed.insert_field_at(index=5, name="   Total Videos Uploaded   ", value="```"f"{obj.video}""```")

    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/729329283251830855/759677982746083328/unnamed_1.jpg")

    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    print("works")

    await ctx.send(embed=embed)



@bot.command()
async def minecraft(ctx, username='Shrek'):
    '''
    Shows MC account info, skin and username history
    '''
    uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'
                        .format(username)).json()['id']

    url = json.loads(base64.b64decode(requests.get(
        'https://sessionserver.mojang.com/session/minecraft/profile/{}'
            .format(uuid)).json()['properties'][0]['value'])
                     .decode('utf-8'))['textures']['SKIN']['url']

    names = requests.get('https://api.mojang.com/user/profiles/{}/names'.format(uuid)).json()
    history = "**Name History:**\n"
    for name in reversed(names):
        history += name['name'] + "\n"


    embed = discord.Embed(title=f"{username}", description="Skin",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.set_image(url="{}".format(url))
    await ctx.send(embed=embed)



  

@bot.command(helpinfo='Wikipedia summary', aliases=['w', 'wiki'])
async def wikipedia(ctx, *, query: str):
    sea = requests.get(
        ('https://en.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

    if sea['searchinfo']['totalhits'] == 0:
        await ctx.send('Sorry, your search could not be found.')
    else:
        for x in range(len(sea['search'])):
            article = sea['search'][x]['title']
            req = requests.get('https://en.wikipedia.org//w/api.php?action=query'
                               '&utf8=1&redirects&format=json&prop=info|images'
                               '&inprop=url&titles={}'.format(article)).json()['query']['pages']
            if str(list(req)[0]) != "-1":
                break
        else:
            await ctx.send('Sorry, your search could not be found.')
            return
        article = req[list(req)[0]]['title']
        arturl = req[list(req)[0]]['fullurl']
        artdesc = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/'+article).json()['extract']
        lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'], "%Y-%m-%dT%H:%M:%SZ")
        embed = discord.Embed(title='**'+article+'**', url=arturl, description=artdesc, color=0x3FCAFF)
        embed.set_footer(text='Wiki entry last modified',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.set_author(name='Wikipedia', url='https://en.wikipedia.org/',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.timestamp = lastedited
        await ctx.send('**Search result for:** ***"{}"***:'.format(query), embed=embed)


        
        
        
 @bot.command(helpinfo='Searches the web (or images if typed first)')
async def google(ctx, *, searchquery: str):

    searchquerylower = searchquery.lower()
    if searchquerylower.startswith('images '):
        await ctx.send('<https://www.google.com/search?tbm=isch&q={}>'
                       .format(urllib.parse.quote_plus(searchquery[7:])))
    else:
        await ctx.send('<https://www.google.com/search?q={}>'
                       .format(urllib.parse.quote_plus(searchquery)))


        
        
@bot.command(helpinfo='Picks randomly between multiple choices')
async def pick(ctx, *choices: str):
    await ctx.send((random.choice(choices)) + ', I choose you!')



 @bot.command()
async def trends(ctx):
    from pytrends.request import TrendReq
    pytrend = TrendReq()

    today_searches_df = pytrend.today_searches(pn='IN')
    print(today_searches_df.head(20))
    embed = discord.Embed(title="Daily trending searches", description=f"{today_searches_df}", timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    await ctx.send(embed=embed)



@bot.command()
async def crn(ctx):
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'

    SHORT_HEADERS = ['SNo', 'State', 'Indian-Confirmed(Including Foreign Confirmed)', 'Cured', 'Death']

    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_contents(soup.tr.find_all('th'))

    stats = []
    all_rows = soup.find_all('tr')

    for row in all_rows:
        stat = extract_contents(row.find_all('td'))

        if stat:
            if len(stat) == 4:
                # last row
                stat = ['', *stat]
                stats.append(stat)
            elif len(stat) == 5:
                stats.append(stat)

    stats[-1][0] = len(stats)
    stats[-1][1] = "Total Cases"
    objects = []
    for row in stats:
        objects.append(row[1])

    y_pos = np.arange(len(objects))

    performance = []
    for row in stats[:len(stats) - 1]:
        performance.append(int(row[2]))

    performance.append(int(stats[-1][2][:len(stats[-1][2]) - 1]))

    table = tabulate(stats, headers=SHORT_HEADERS)
    print(table)


bot.run("Token")
