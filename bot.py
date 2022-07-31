import discord, asyncio

client = discord.Client()

@client.event
async def on_ready(): 
    print("성공!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("헤헷"))

@client.event
async def on_message(message):
    if message.content == "안녕": 
        await message.channel.send ("응".format(message.author, message.author.mention))
    if message.content == "야": 
        await message.channel.send ("뭐".format(message.author, message.author.mention))
    if message.content == "에휴": 
        await message.channel.send ("어쩌라고".format(message.author, message.author.mention))
    if message.content == "ㅉㅉ": 
        await message.channel.send ("응 아니야".format(message.author, message.author.mention))


client.run('MTAwMzIwMzY3MjAzNTA0NTQ0OQ.GdGBUE.iSXNmHdLRAlB0QCKx8Ap4EmZBfeX5B_ZHRDQkI')