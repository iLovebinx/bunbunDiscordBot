import discord
from discord.ext import commands
import os
import json
import random


bunbun = commands.Bot (command_prefix= "!")
bunbun.remove_command ("help")


async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@bunbun.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await bunbun.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@bunbun.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        exp = users[str(id)]['experience']
        embed=discord.Embed(color=0xf7cad5)
        embed.add_field(name="Level", value= lvl, inline=False)
        embed.add_field(name="EXP", value= exp, inline=True)
        await ctx.send(embed=embed)
        
    else:
        id = member.id
    
        with open('users.json', 'r') as f:
            users = json.load(f)
            exp = users[str(id)]['experience']
        lvl = users[str(id)]['level']


        embed=discord.Embed(title = member, color=0xf7cad5)
        embed.add_field(name="Level", value= lvl, inline=False)
        embed.add_field(name="EXP", value= exp, inline=True)
        await ctx.send(embed=embed)
        


async def get_level_data ():
    with open("levels.json", "r") as f:
        users = json.load(f)
    return users 

@bunbun.command(aliases = ["bal", "Balance", "BALANCE" "bankamt", "wallet"])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

   
    embed=discord.Embed(color=0xf7cad5)
    embed.add_field (name = ctx.author, value = "your balance is")
    embed.add_field(name = "Wallet", value = wallet_amt, inline=False)
    embed.add_field(name = "Bank",value = bank_amt, inline=False)
    await ctx.send(embed=embed)

@bunbun.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f"you got {earnings} bunbunbucks yay!")


    users[str(user.id)]["wallet"] += earnings

    with open("bunbank.json", "w") as f:
        json.dump(users,f)


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)]  = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open ("bunbank.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("bunbank.json", "r") as f:
        users = json.load(f)
    return users


async def load (ctx, extension):
    bunbun.load_extension(f'cogs.{extension}')

async def unload (ctx, extension):
    bunbun.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bunbun.load_extension (f'cogs.{filename[:-3]}')


   



 


bunbun.run('OTE3ODIwMzc3MTU2MTYxNTc2.Ya-Q1g.vLgaf_GGZLsHRIuTVVGPRrG0smU') 