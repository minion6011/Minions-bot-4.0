
@client.command()
async def info(ctx):
  await ctx.respond(
  f'''
  Client Name ➟ ({bot.user.display_name})

Friends Total ➟ ({len(bot.friends())})

Party Leader ➟ ({bot.party.leader})

Members ➟  
''')

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


 
