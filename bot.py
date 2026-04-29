import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command("flag")
async def flag(ctx, country):
    await ctx.send(f"https://flagsapi.com/{country}/flat/64.png")

@bot.command("topla")
async def topla(ctx, *nums):
    sum = 0
    for number in nums:
        sum += int(number)
    await ctx.send(f"Sum equals: {sum}")

bot.run("TOKEN")
