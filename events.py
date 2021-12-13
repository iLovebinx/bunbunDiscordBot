import discord
from discord import client
from discord.ext import commands

class Events(commands.Cog):
    def __innit__(self, bunbun):
        self.bunbun = bunbun

    #events
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Event is online')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        print (f'{member} has joined a server. ')

    @commands.Cog.listener()
    async def on_member_removed(self,member):
        
        print (f'{member} has left a server')


   






def setup(bunbun):
    bunbun.add_cog(Events(client))
