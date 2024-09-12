import discord
import requests as r
api = 'https://api.fyro.ml/rickroll/'

my_secret = 'your token here'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$help'))

@client.event
async def on_message(message):
    # username = str(message.author).split('#')[0]
    # channel = str(message.channel.name)
    # print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        await message.reply("Use - $check _Your link_ to check if a link is a rick roll :)",mention_author = True)
    if message.content.startswith('$check'):
        payload = {'url':str(message.content).split('$check ')[1]}
        try:
            response = r.get(api,params=payload)
        except:
            await message.reply("Some error occured ;(",mention_author = True)
        if response.json()['isRICKROLL'] == True:

            await message.reply("That's a rick roll link! Do NOT click!",mention_author = True)
        elif response.json()['isRICKROLL'] == False:

            await message.reply("That's NOT a rick roll link! Phew.. I just saved u :)",mention_author = True)

        elif response.json()['isRICKROLL'] == 'Youtube Shorts - May or May not be RickRoll!':

            await message.reply("Well I'm not sure about youtube shorts, MAY or MAY NOT be a rick roll link, sorry :(",mention_author = True)
        else:
            await message.reply("Couldn't find any data :(",mention_author = True)
        



client.run(my_secret)
