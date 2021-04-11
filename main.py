import discord
import asyncio 
import functools
import itertools
import math  
import os
from itertools import cycle
import datetime
from datetime import date
from datetime import time
from datetime import datetime,timedelta
from discord.utils import get
from os import system 
from discord.ext import commands
import random 
from async_timeout import timeout
import platform 
import time
from discord import DMChannel
from discord.ext.commands import check

intents = discord.Intents.all()
client=discord.Client
clientdiscord=discord.Client()
client = commands.Bot(command_prefix='*' , intents=discord.Intents.all())


#for filename in os.listdir('./cogs'):
#    if filename.endswith('.py'):
 #       client.load_extension(f'cogs.{filename[:-3]}')


#@client.event
#async def on_ready():
 #   print('Online')
  #  print('Logged in as:\n{0.user.id}'.format(client))



@client.command()
async def ping(ctx):
    await ctx.send(f'```Ping: {round(client.latency * 1000)}ms```')


@client.event
async def on_ready():
     print('logged as.....')
     await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"tooshyyy#9999❤️!"))



@client.event
async def on_member_join(member):
    jllogs=discord.utils.get(member.guild.text_channels, name="name tou channel sou")
    now=datetime.now()
    ##embed##
    embed=discord.Embed(title="Member Join") ##member.guild.icon_url
    embed=discord.Embed(color=0x00ff0d)
    embed.set_author(name=f"{member}",icon_url=f"{member.guild.icon_url}")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.add_field(name="Account Creation Date:", value=f"```{client.get_user(member.id).created_at.replace(microsecond=0)}```", inline=True)
    embed.set_footer(text="{}".format(now.strftime("%m%d%Y, %H:%M:%S")))
    await jllogs.send(embed=embed)
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')



@client.command()
@commands.has_permissions(send_messages=True)
async def tsekre(ctx):
    await ctx.channel.send(f"EIMAI ENAS LOUKOUMAS https://cdn.discordapp.com/attachments/780857423836872805/817445600743915551/Snapchat-948152112.jpg")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def sanirdi(ctx):
    await ctx.channel.send(f"EIMAI ENAS CLOWN PAIDIA https://cdn.discordapp.com/attachments/579966801203691522/817498929011621888/unknown-1.png")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def oikonomou(ctx):
    await ctx.channel.send(f"KANW BARH KAI EIMAI DOULAPAS https://cdn.discordapp.com/attachments/579966801203691522/813047546053394472/IMG_20210221_160031.jpg")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def xrhstos(ctx):
    await ctx.channel.send(f"EIMAI ENAS ARXOPOFAGIOLAS POU EXEI MONOFRYDOhttps://cdn.discordapp.com/attachments/579966801203691522/812874629689245746/IMG_20210103_234827.jpg")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def drizzly(ctx):
    await ctx.channel.send(f"O MPAMPAS SAS https://cdn.discordapp.com/attachments/579966801203691522/817173665573109790/dchkdo0r.png")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def andriana(ctx):
    await ctx.channel.send(f"EXW ENA KEFALI SAN MANITARI https://cdn.discordapp.com/attachments/579966801203691522/812873825154891836/unknown-5.png")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def xarhs(ctx):
    await ctx.channel.send(f"PASADES MOU FERTE MOU ENA GIAOURTI https://cdn.discordapp.com/attachments/810335906439102505/813174642990645258/image0-1.png")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def grhgoriou(ctx):
    await ctx.channel.send(f"TSOUPAPI MOUNIANOOO https://cdn.discordapp.com/attachments/782534252175818763/816064048160047144/IMG_20210223_095049.jpg")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def Jmars(ctx):
    await ctx.channel.send(f"BARBARAAAA POU EISAIII https://cdn.discordapp.com/attachments/579966801203691522/812874210204450846/IMG_20210212_235345.jpg")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def kalamarhs(ctx):
        await ctx.channel.send(f"EIMAI O NOUMERO ENA BACHELOR TOU SERVER https://www.tovima.gr/wp-content/uploads/2011/09/21/2909988-3x4-700x933.jpg")
        return


@client.command()
@commands.has_permissions(send_messages=True)
async def lenio(ctx):
    await ctx.channel.send(f"EIMAI SAN YPERTROFIKH KAMPIA https://cdn.discordapp.com/attachments/784491257517965352/817740690800246784/20210114_195806.jpg")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def climmentelis(ctx):
    await ctx.channel.send(f"TRWW PSARIA TO BRADY IME MIA GATA NIAOU https://cdn.discordapp.com/attachments/804851176306769980/818104154370605076/slqndy_gata.png")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def shaggy(ctx):
    await ctx.channel.send(f"EIMAI O AXILEAS KAI NIKHSA TON EKTORA SYMBATRIOTES https://cdn.discordapp.com/attachments/579966801203691522/818256435611828284/IMG_20210307_220552.jpg")
    return


@client.command()
@commands.has_permissions(send_messages=True)
async def karagiozhs(ctx, target: discord.Member):
    await ctx.channel.send(f"KOITA TI EISAI RE CLOWN {target} https://pamebolta.gr/sites/default/files/14165091501626652274_0.jpg")
    return


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'```Kicked {member}. Reason: {reason}```')
        return


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
     await ctx.channel.purge(limit=amount)
     await ctx.send(f'```Cleared {amount} messages.```')
     return


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, target: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await target.add_roles(mutedRole)
    await ctx.channel.send(f"```Muted {target} for {reason}```")
    await target.send(f"You were muted for {reason}.")
    return


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, target: discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await target.remove_roles(mutedRole)
    await ctx.channel.send(f"Un-Muted {target}.")
    return


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, target: discord.Member, *, reason):
    await ctx.guild.ban(target,reason=reason)
    await ctx.channel.send(f'```Banned {target}. Reason: {reason}```')
    return


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    print("h")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f'```Un-Banned {user.name}#{user.discriminator}.```')
            return
    

@client.command(aliases=['8ball'])
async def _8ball(ctx, * , question):
    responses = ['```Isws```' ,
                 '```Malista symbatrioth```' ,
                 '```Bebaios```' ,
                 '```Oxi```' ,
                 '```Mallon```' ,               
                 '```Eee ekfrasou piw wraia!```' ,
                 '```re fyge apo edw re```' ,
                 '```Pithanotata```' ,
                 '```Ase me na koimhtw```' ,
                 '```Anamfisbitita nai```' ,
                 '```Anamfisbitita oxi```',
                 '```Ai re karagkiozako```',
                 '```Poly pithanon```',
                 '```Polla rwtas omws.```',
                 '```Re fyge re malaka apo edw re bro```',
                 '```Ante vre kefte me podia```']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')



@client.command()
@commands.has_permissions(send_messages=True)
async def princess(ctx, target: discord.Member):
    message = await ctx.send(f'Είσαι η Βασίλισσα μου!:smiling_face_with_3_hearts:{target.mention}')
    await asyncio.sleep(4)
    await message.edit(content=f'Θέλω να σε ιππέυσω, σε θεωρώ ελκυστική!:kissing_heart:{target.mention}')
    return


@client.command()
@commands.is_owner()
async def comboall(ctx):
    author = ctx.author

    if author.guild_permissions.administrator:
        try:
            no_of_members = 0
            for member in author.voice.channel.members:
                if not member.bot:
                    await member.edit(mute=True)
                    await member.edit(deafen=True)
                    await member.edit(voice_channel=None)
                    no_of_members += 1
                else:
                    await member.edit(mute=False)
                    await member.edit(deafen=False)
                    await ctx.send(f"I did not combed {member.name}")
            if no_of_members == 0:
                    await ctx.channel.send(f"Everyone, please disconnect and reconnect to the Voice Channel again.")
            elif no_of_members < 2:
                    await ctx.channel.send(f"Combed {no_of_members} user in {author.voice.channel}.")
            else:
                await ctx.channel.send(f"Comboed {no_of_members} users in {author.voice.channel}.")

        except discord.Forbidden:
            await ctx.channel.send(f"Please make sure I have the `Administrator`in my role **and** in your current" f"voice channel `{author.voice.channel}")

    else:
        await ctx.channel.send(f"You don't have the `Administrator` permission.")
        return



@client.command()
async def shush(ctx):
    author = ctx.author
  
    if author.guild_permissions.mute_members:  
        try:
            no_of_members = 0
            for member in author.voice.channel.members:  
                if not member.bot:  
                    await member.edit(mute=True)  
                    no_of_members += 1
                else:
                    await member.edit(mute=False)  
                    await ctx.send(f"Un-muted {member.name}")
            if no_of_members == 0:
                    await ctx.channel.send(f"Everyone, please disconnect and reconnect to the Voice Channel again.")
            elif no_of_members < 2:
                    await ctx.channel.send(f"Muted {no_of_members} user in {author.voice.channel}.")
            else:
                await ctx.channel.send(f"Muted {no_of_members} users in {author.voice.channel}.")

        except discord.Forbidden:
                await ctx.channel.send(f"Please make sure I have the `Mute Members`in my role **and** in your current" f"voice channel `{author.voice.channel}`") 
    else:
        await ctx.channel.send("You don't have the `Mute Members` permission.")
        return



"""
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def yeet(ctx, member : discord.Member):
    author = ctx.author
    my_id = "405005772783616000"

    if int(member.id) is not my_id:
        try:
            await member.edit(mute=True,deafen=True,voice_channel=None)                           
            await ctx.channel.send(f'Yeeted {member.mention}. HASTA LA VISTA BABY!')

        except discord.Forbidden:
            await ctx.channel.send(f"Please make sure I have the `Administrator` permission to do that!")
    
 
        if int(member.id) == my_id:
            await member.edit(mute=False, deafen=False)        
        else: 
            await author.edit(mute=True, deafen=True, voice_channel=None)
            await author.send(f"ΠΑΡΕ ΤΟΝ ΠΟΥΤΣΟ ΜΟΥ ΚΑΡΑΓΚΙΟΖΑΡΕ!:middle_finger:")
            return
"""

@client.command()
@commands.has_permissions(manage_messages=True)
async def combo(ctx,member : discord.Member):
    dc=discord.utils.get(ctx.guild.text_channels, name="dc-logs")
    if int(member.id)==340295037290020866 or int(member.id)==631591703945543710:
        await ctx.author.edit(mute=True,deafen=True,voice_channel=None)
        await dc.send(f'O Karagkiozhs o {ctx.author.mention} prospathise na kanei combo ton VASILIA DRIZZLY . Nomizate oti mporeite na ksegelasete ton fousekh? https://i.kym-cdn.com/entries/icons/medium/000/033/233/cover8.jpg')
        await ctx.author.send("PARTON POUTSO MOU KARAGKIOZARE")
    else:
        await dc.send(f'{member.mention} has received a combo by {ctx.author.mention}')
        await member.edit(mute=True,deafen=True,voice_channel=None)


"""
@client.command()
@commands.has_permissions(manage_messages=True)
async def lockall(ctx, channel : discord.TextChannel=None):
    guild = ctx.guild
    channels = ctx.guild.channels
    role = discord.utils.get(ctx.guild.roles, name="@everyone") #retrieve everyone role
    for channel in channels:
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.channel.send(f"```Locked all channels!```")
        return
"""



@client.command()
@commands.has_permissions(manage_messages=True)
async def lockall(ctx, channel : discord.TextChannel=None,*, reason=None):
    guild = ctx.guild
    channels = ctx.guild.channels
    role = discord.utils.get(ctx.guild.roles, name="@everyone") 
    for channel in channels:
        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)}
            await channel.set_permissions(overwrites=overwrites)
            await ctx.channel.send(f"**{ctx.author}** ・ You have Locked a Channel.\n\n**Channel:** `{channel.name}`\n**Reason:** `{reason}`")
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.channel.send(f"```Locked all channels!```")
            return



@client.command()
@commands.has_permissions(manage_messages=True)
async def unlockall(ctx, channel : discord.TextChannel=None):
    guild = ctx.guild
    channels = ctx.guild.channels
    role = discord.utils.get(ctx.guild.roles, name="@everyone") #retrieve everyone role
    for channel in channels:
#       overwrite = channel.overwrites_for(ctx.guild.default_role)
#       overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.channel.send(f"```Un-Locked all channels!```")
        return



@client.command()
@commands.has_permissions(administrator=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = ctx.channel or channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.channel.send(f"```Channel Locked.```")
    return   


@client.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = ctx.channel or channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.channel.send(f"```Channel Un-Locked.```")
    return


@client.command()
@commands.has_permissions(administrator=True)
async def amalia(ctx):
    await ctx.channel.send(f"EIMAI MIA OPTASIA DEITE ME RE TSARLATANOI https://cdn.discordapp.com/attachments/579966801203691522/820624896086245417/20210305_102338.jpg")
    return


"""
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def move(ctx, member: discord.Member, reason=None):
    author = ctx.message.author
    channel = author.voice.channel
    
    if author.guild_permissions.move_members:
        try:
            await member.move_to(author, reason=reason)
            await member.move_to(channel, reason=reason)

        except discord.Forbidden:
            await ctx.channel.send("Please make sure I have the `Move Members` in my role!")
            
    else:
        await ctx.channel.send(f"Make sure you have the right permissions to do that!")
        return
"""



"""
@client.command()
@commands.has_permissions(administrator=True)
async def massmove(ctx, member: discord.Member):
    server = ctx.guild
    all_members = server.members

    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("You are not connected to voice!")
    for members in all_members:
        if members.voice:
            await members.move_to(channel)
            await ctx.channel.send(f":no_entry:Mass moved all voice members to author's voice!:no_entry:")
            return
"""


@client.command()
@commands.is_owner()
@commands.has_permissions(administrator=True)
async def massmove(ctx):
    server = ctx.guild
    author = ctx.author
    all_members = server.members

    if author.voice:
        move_channel = author.voice.channel
    else:
        await ctx.send(f"You have to be in a Voice Channel to use this command, {ctx.author.mention}")
        return
    for member in all_members:
        if(member.voice and not member.voice.afk):
            await member.move_to(move_channel)
    await ctx.send(f":no_entry:Mass moved everyone to {str(move_channel)}:no_entry:")
    return
            

@client.command()
@commands.has_permissions(administrator=True)
async def move(ctx, member: discord.Member=None):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("You are not connected to voice!")
    if not member:
        await ctx.send("Who am I trying to move? Use *move @user")
    await member.move_to(channel)
    await ctx.channel.send(f'Moved {member.mention} in authors voice!')
    return



@client.command()
async def speak(ctx):
    author = ctx.author
  
    if author.guild_permissions.administrator:  
        try:
            no_of_members = 0
            for member in author.voice.channel.members:  
                if not member.bot:  
                    await member.edit(mute=False)  
                    no_of_members += 1
                else:
                    await member.edit(mute=True)  
                    await ctx.send(f"Muted {member.name}")
            if no_of_members == 0:
                    await ctx.channel.send(f"Everyone, please disconnect and reconnect to the Voice Channel again.")
            elif no_of_members < 2:
                    await ctx.channel.send(f"Un-Muted {no_of_members} user in {author.voice.channel}.")
            else:
                await ctx.channel.send(f"Un-Muted {no_of_members} users in {author.voice.channel}.")

        except discord.Forbidden:
                await ctx.channel.send(f"Please make sure I have the `Mute Members`in my role **and** in your current" f"voice channel `{author.voice.channel}`") 
    else:
        await ctx.channel.send("You don't have the `Mute Members` permission.")
        return


"""
@client.event
async def on_message(message):
    words = ["Miss"]

    for i in range(len(words)):  
        if words[i] in message.content:
            for j in range(30):
                await message.channel.send("XRONIA POLLA SYMBRATRIOTHSA MISS:heart:-tooshyyy")
"""              


@client.command()
@commands.has_permissions(administrator=True)
async def tooshyy(ctx):
    await ctx.channel.send(f"se eipe ntumenh me maura rouxa? auto einai prosvolh! https://cdn.discordapp.com/attachments/579966801203691522/825504172472139796/9k.png")
    return

          

@client.command()
@commands.is_owner()
@commands.has_permissions(administrator=True)
async def displayembed(ctx):
    embed = discord.Embed(
        title = 'Bot Update' ,
        description = '**Move Command fixed!From now on you can now move users in your voice channel**:heart:'
                        
                             ,
        colour = discord.Colour.dark_blue())


    embed.set_footer(text='Οτιδήποτε χρειαστείτε στείλτε μου ιδιωτικό μήνυμα!')
#   embed.set_image(url='https://cdn.discordapp.com/attachments/579966801203691522/828210562629369856/ikona.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/579966801203691522/828210562629369856/ikona.jpg')
    embed.set_author(name='tooshyy' ,
    icon_url='https://cdn.discordapp.com/attachments/579966801203691522/817563092241088522/ezgif.com-gif-maker.gif')


    await ctx.channel.send(embed=embed)
    return












































































client.run('ODAyMjY4Nzc3ODI3NTMyODk3.YAsxBg.LOjf0YqEA6-k4IuQiKM8P1G8l7E')