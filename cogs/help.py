# Import modules
from discord.ext import commands

# Help Command Initialize constructor
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        message = ("```List of commands:\n"
                  "\n"
                  ",p - Play a song via Youtube link, or search\n"
                  ",s - Skip the current song\n"
                  ",loop - Loop the current song\n"
                  ",queue - Show the current queue\n"
                  ",remove - remove song in queue by order number\n"
                  ",pause - Pause song\n"
                  ",resume - Resume playing\n"
                  ",skipall - Empty the queue and skip current song\n"
                  ",leave - Bot will leave the current channel\n"
                  ",delete - Delete specified ammount of bot's messages\n"
                  ",help - List all commands available```")
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Help(bot))