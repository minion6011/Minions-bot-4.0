import fortnitepy
import PirxcyPinger
import json
import discord
from discord.ext import commands as dcommands
import os
import BenBotAsync
from fortnitepy.ext import commands


client = dcommands.Bot(  command_prefix="!",)

filename = 'auths.json'


def get_device_auth_details():
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            return json.load(fp)
    return {}

def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details

    with open("auths.json", 'w') as fp:
        json.dump(existing, fp)

device_auth_details = get_device_auth_details().get("your email", {})
bot = commands.Bot(
  command_prefix="!",
  auth=fortnitepy.AdvancedAuth(
        email="your email",
        password="your password",
        prompt_authorization_code=True,
        prompt_code_if_invalid=True,
        delete_existing_device_auths=True,
        **device_auth_details
    )
)

prefix = bot.command_prefix

@bot.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)

@bot.event
async def event_ready():
  await client.start("Your discord token")    
 

@bot.event
async def event_party_invite(invite):
  await invite.accept()

@bot.event
async def event_friend_request(request):
  await request.accept()

@bot.command()
async def info(ctx):
  await ctx.respond(
  f'''
  Client Name ➟ ({bot.user.display_name})

Friends Total ➟ ({len(bot.friends())})

Party Leader ➟ ({bot.party.leader})

Members ➟ 
''')

@commands.dm_only()
@bot.command()
@commands.dm_only()
async def cid(ctx, *, skin):
  await bot.party.me.set_outfit(asset=skin)

@commands.dm_only()
@bot.command()
@commands.dm_only()
async def eid(ctx, *, skin):
  await bot.party.me.set_emote(asset=skin)

@commands.dm_only()
@bot.command()
@commands.dm_only()
async def skin(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No skin was given, try: {prefix}skin (skin name)')
    elif content.upper().startswith('CID_'):
        await bot.party.me.set_outfit(asset=content.upper())
        await ctx.send(f'Skin set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                name=content,
                backendType="AthenaCharacter"
            )
            await bot.party.me.set_outfit(asset=cosmetic.id)
            await ctx.send(f'Skin set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a skin named: {content}')

@commands.dm_only()
@bot.command()
@commands.dm_only()
async def backpack(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No backpack was given, try: {prefix}backpack (backpack name)')
    elif content.lower() == 'elimina':
        await bot.party.me.clear_backpack()
        await ctx.send('Backpack impostato: Nessuno')
    elif content.upper().startswith('BID_'):
        await bot.party.me.set_backpack(asset=content.upper())
        await ctx.send(f'Backpack set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaBackpack"
            )
            await bot.party.me.set_backpack(asset=cosmetic.id)
            await ctx.send(f'Backpack set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a backpack named: {content}')

@commands.dm_only()
@bot.command()
async def emote(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No emote was given, try: {prefix}emote (emote name)')
    elif content.lower() == 'floss':
        await bot.party.me.clear_emote()
        await bot.party.me.set_emote(asset='EID_Floss')
        await ctx.send(f'Emote set to: Floss')
    elif content.lower() == 'scenario':
        await bot.party.me.clear_emote()
        await bot.party.me.set_emote(asset='EID_KPopDance03')
        await ctx.send(f'Emote set to: Scenario')
    elif content.lower() == 'none':
        await bot.party.me.clear_emote()
        await ctx.send(f'Emote set to: None')
    elif content.upper().startswith('EID_'):
        await bot.party.me.clear_emote()
        await bot.party.me.set_emote(asset=content.upper())
        await ctx.send(f'Emote set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaDance"
            )
            await bot.party.me.clear_emote()
            await bot.party.me.set_emote(asset=cosmetic.id)
            await ctx.send(f'Emote set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find an emote named: {content}')



@client.command()
async def cid(ctx, *, skin):
  await bot.party.me.set_outfit(asset=skin)


@client.command()
async def eid(ctx, *, skin):
  await bot.party.me.set_emote(asset=skin)

@client.command()
async def skin(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No skin was given, try: {prefix}skin (skin name)')
    elif content.upper().startswith('CID_'):
        await bot.party.me.set_outfit(asset=content.upper())
        await ctx.send(f'Skin set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                name=content,
                backendType="AthenaCharacter"
            )
            await bot.party.me.set_outfit(asset=cosmetic.id)
            await ctx.send(f'Skin set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a skin named: {content}')


@client.command()
async def backpack(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No backpack was given, try: {prefix}backpack (backpack name)')
    elif content.lower() == 'elimina':
        await bot.party.me.clear_backpack()
        await ctx.send('Backpack impostato: Nessuno')
    elif content.upper().startswith('BID_'):
        await bot.party.me.set_backpack(asset=content.upper())
        await ctx.send(f'Backpack set to: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaBackpack"
            )
            await bot.party.me.set_backpack(asset=cosmetic.id)
            await ctx.send(f'Backpack set to: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a backpack named: {content}')


@client.command()
async def emote(ctx, *, content = None):
    if content is None:
        await ctx.send(f'No emote was given, try: {prefix}emote (emote name)')
    elif content.lower() == 'floss':
        await bot.party.me.clear_emote()
        await bot.party.me.set_emote(asset='EID_Floss')
        await ctx.send(f'Emote set to: Floss')
    elif content.lower() == 'scenario':
        await bot.party.me.clear_emote()
        await bot.party.me.set_emote(asset='EID_KPopDance03')
        await ctx.send(f'Emote set to: Scenario')
    elif content.lower() == 'none':
        await bot.party.me.clear_emote()
        await ctx.send(f'Emote messa: nessuna')
    elif content.upper().startswith('EID_'):
        await bot.party.me.clear_emote()
        await bot.party.me.set_emote(asset=content.upper())
        await ctx.send(f'Emote messa: {content}')
    else:
        try:
            cosmetic = await BenBotAsync.get_cosmetic(
                lang="en",
                searchLang="en",
                matchMethod="contains",
                name=content,
                backendType="AthenaDance"
            )
            await bot.party.me.clear_emote()
            await bot.party.me.set_emote(asset=cosmetic.id)
            await ctx.send(f'Ho messo l emote: {cosmetic.name}')
        except BenBotAsync.exceptions.NotFound:
            await ctx.send(f'Non ho trovato un emote col nome: {content}')


bot.run()
