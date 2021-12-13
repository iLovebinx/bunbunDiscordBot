import discord
from discord import client
from discord.ext import commands


class command_moderation(commands.Cog):
    def __innit__(self, bunbun):
        self.bunbun = bunbun

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Moderation Online')

    #start of commands
    @commands.command (invoke_without_command=True) 
    async def help(self,ctx):
        
        embed=discord.Embed(title="Help", description="Bun Bun bot offers a wide arange of things, such as moderation, minigames, a global currency system, and much much more. Visit bunbuns website to see the full list of commands !!", color=0xf7cad5)

        
        embed.set_footer(text="Sincearly Brandon ")
        
        await ctx.send(embed=embed)

    @commands.command () #clear
    async def clear(self,ctx, amount = 5):
        if  (not ctx.author.guild_permissions.manage_messages):
            
            await ctx.send ('i dont know you ! i only let people with the manage messages permission to purge')
        
        amount += 1 

        if amount > 101:
            await ctx.send ('my power is not strong enough to delete more than 100 messages at a time. try 99 and spam the command :)')

        elif amount <100:
    
            await ctx.channel.purge(limit = amount)
            await ctx.send (f'bye bye {amount} messages!!!')

    @commands.command () #kick
    async def kick (self,ctx, member : discord.Member, *, reason = None):
        if  (not ctx.author.guild_permissions.KICK_MEMBERS):
            
            await ctx.send (f'i dont know you ! i only let people with the KICK_MEMBERS permission to kick peoples')

        else:
            
            await member.kick(reason = reason)
            await ctx.send (f'bye bye {member.mention} no one liked you anyways !!!!')

    @commands.command () #ban
    async def ban (self,ctx, member : discord.Member, *, reason = None):
        if (not ctx.author.guild_permissions.BAN_MEMBERS):
            
            await ctx.send (f'i dont know you ! i only let people with the BAN_MEMBERS permission to kick peoples')

        else:
        
            await member.ban(reason = reason)
            await ctx.send ('{member.mention} has been banned by the all powerfuil {ctx.author} mwahahahaha, oh wait you probably wont see the message, why? because youre banned hehe')

    @commands.command ()
    async def unban (self,ctx, *, member):
        
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                
                await ctx.guild.unban(user)
                await ctx.send (f'Unbanned {user.mention}, we forgive youu')
                
                return

                

def setup(bunbun):
    bunbun.add_cog(command_moderation(client))

