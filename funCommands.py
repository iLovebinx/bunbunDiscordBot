import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.core import command
import random


class funCommands(commands.Cog):
    def __innit__(self, bunbun):
        self.bunbun = bunbun

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Fun Command Online')


# commands


    @commands.command(
        aliases=[
        "8ball",
        "8Ball",
        "8bAll",
        "8BAll",
        "8BaLl",
        "8bALl",
        "8BALl",
        "8balL",
        "8BalL",
        "8bAlL",
        "8BAlL",
        "8baLL",
        "8BaLL",
        "8bALL",
        "8BAL",
    ]
)

# eight ball
    async def eight_ball(self, ctx, *, question):

        responses = [
            "im trying to think as hard as i can, but i cant :(",
            "if i knew, i would tell you !",
            "i know it will happen if you wanted it to",
            "lets manifest together then !"
            "maybe it will, maybe it wont, youre asking my penut brain silly ! "
            "thinking about it is gonna make my head explode !"
            "im not a genie !!!!!!",
    ]

        await ctx.send(f" {ctx.author} asked: {question} \n\nBunbun thinks: {random.choice(responses)}")


    

    @commands.command(aliases = ["topic", "Topics", "topIcs"])



# eight ball
    async def topics(self, ctx,):

        responses = [ "What was the last funny video you saw?", " What is something you are obsessed with?", "What three words best describe you?", "What would be your perfect weekend?", " What’s your favorite number? Why?", " What’s your favorite way to waste time?"
           
    ]

        await ctx.send(f" {random.choice(responses)}")


    


def setup(bunbun):
    bunbun.add_cog(funCommands(bunbun))

