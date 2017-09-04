import discord
from discord.ext import commands

class SelfbotUtility:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def nickme(self, ctx, *, name):
        """Set your nickname. An alternative to discord's built-in /nick, meant for use specifically on mobile devices."""
        await self.bot.change_nickname(ctx.message.author, name)
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def sendempty(self, ctx):
        """Send an empty message."""
        await self.bot.say(chr(173))
        await self.bot.delete_message(ctx.message)
    
    @commands.command(pass_context=True)
    """Delete the last message you sent. Short command name for fast use."""
    async def d(self, ctx):
        await self.bot.delete_message(self.bot.lastmsg)
        await self.bot.delete_message(ctx.message)
    
    @commands.command(pass_context=True)
    async def e(self, ctx, *, content):
        """Edit your last message. Short command name for fast use."""
        await self.bot.edit_message(self.bot.lastmsg, new_content=content)
        await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(SelfbotUtility(bot))
