import discord, random, asyncio, json, os
from discord.ext import commands

owo = ["owo", "w"]

cf = ["cf", "coinflip"]
slot = ["s", "slot"]

hunt = ["h", "hunt"]
battle = ["b", "battle"]

with open("data.json", "r") as f:

    data = json.load(f)

bot = commands.Bot(command_prefix=data["prefix"], help_command=None, user_bot=True)


@bot.event
async def on_ready():

    os.system("cls")
    print(f"{bot.user} aktif!") 
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Owo Kasıyorum"))


@bot.command(aliases=["calistir", "çalıştır", "başlat", "open", "aç", "ac"])
async def baslat(payload):

    stop = 0

    if stop == 0:

        if payload.author.id == data["root"]:

            channel = bot.get_channel(data["channelid"])

            while True:
                
                for i in range(5):

                    if payload.author.id == 408785106942164992:

                        if payload.channel.id == data["channelid"]:

                            if "Beep Boop. Please DM me" in payload.content:

                                stop = 1

                    await channel.send(f"{random.choice(owo)} {random.choice(hunt)}")
                    await asyncio.sleep(random.randint(1, 3))
                    await channel.send(f"{random.choice(owo)} {random.choice(battle)}")
                    await asyncio.sleep(random.randint(2, 5))

                    await channel.send(f"{random.choice(owo)} {random.choice(cf)} {random.randint(10, 100)}")
                    await asyncio.sleep(random.randint(1, 3))
                    await channel.send(f"{random.choice(owo)} {random.choice(slot)} {random.randint(10, 100)}")
                    await asyncio.sleep(random.randint(13, 17))

                await channel.send(f"{random.choice(owo)} use {random.randint(51, 57)}")
                await asyncio.sleep(random.randint(1, 3))
                await channel.send(f"{random.choice(owo)} use {random.randint(65, 71)}")
                await asyncio.sleep(random.randint(1, 3))
                await channel.send(f"{random.choice(owo)} use {random.randint(72, 78)}")
                await asyncio.sleep(random.randint(1, 3))

bot.run(data["token"])