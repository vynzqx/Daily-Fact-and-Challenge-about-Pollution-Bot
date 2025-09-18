import discord
from discord.ext import commands
import random,os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as Facts and Challenge about Pollution Bot')

@bot.command()
async def hello(ctx):
    await ctx.send('Hi! I am a bot {Facts dan challenge about pollution}!')

@bot.command()  
async def fact(ctx):
    facts = [
        "Air pollution kills an estimated 7 million people worldwide each year, Rescue: Use public transport, bike, or walk instead of driving; support clean energy; plant trees.",
        "A single plastic bottle can take 450 years to decompose, Rescue: Use reusable bottles and bags; avoid single-use plastics; participate in local clean-up events.",
        "Around 1 million seabirds and 100,000 marine animals die annually from plastic pollution, Rescue: Reduce plastic use; support bans on single-use plastics; educate others about the impact of plastic pollution.",
        "Noise pollution can cause stress, sleep problems, and even heart disease, Rescue: Use noise-cancelling headphones; create quiet zones; advocate for noise regulations in your community.",
        "Deforestation contributes to about 15% of global greenhouse gas emissions, Rescue: Support sustainable paper/wood products; plant trees; reduce unnecessary paper use (go digital).",
        "The Great Pacific Garbage Patch is a massive area in the Pacific Ocean filled with plastic debris, Rescue: Participate in beach clean-ups; reduce plastic consumption; support organizations working to clean the oceans.",
        "Light pollution affects the natural behaviors of wildlife, including migration and reproduction, Rescue: Use outdoor lighting only when necessary; install motion sensors; advocate for 'dark sky' initiatives in your community.",
        "Recycling one aluminum can saves enough energy to power a TV for three hours, Rescue: Recycle properly; reduce consumption; support products made from recycled materials.",
        "About 91% of the world’s population lives in places where air quality exceeds WHO limits, Rescue: Support clean energy initiatives; reduce vehicle emissions; plant trees and support green spaces.",
    ]
    await ctx.send(random.choice(facts))

@bot.command()  
async def challenge(ctx):
    challenges = [
        "🚶‍♀️ Walk or cycle instead of using a car for short distances.",
        "♻️ Bring your own bag when shopping—say no to single-use plastics.",
        "🌳 Plant one small plant at home or in your community.",
        "💡 Turn off lights and unplug devices when not in use to save energy.",
        "🥤 Use a reusable bottle or cup instead of disposable ones.",
        "🍴 Have a meat-free day once a week—animal agriculture produces lots of greenhouse gases.",
        "🧹 Pick up 5 pieces of trash whenever you go outside.",
        "🚰 Refill instead of buying bottled water for one full day.",
        "🌳 Spend 15 minutes outside without electronics, just to appreciate nature.",
        "📱 Reduce your screen time by 30 minutes and use that time to read about environmental issues.",
        "🛍️ Buy second-hand clothes or items instead of new ones.",
        "🍽️ Avoid food waste by planning your meals and using leftovers."
    ]
    await ctx.send(random.choice(challenges))

@bot.command()
async def pngr(ctx):
    folder = os.listdir('pngr')
    img = random.choice(folder)
    direktori = f'pngr/{img}'
    with open(direktori, 'rb') as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)


bot.run("Put ur token here")
