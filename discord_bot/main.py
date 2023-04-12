import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

from discord_bot.laptop_filter import LaptopFilter

from table2ascii import table2ascii as t2a, PresetStyle

load_dotenv()

token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

laptop_filter = LaptopFilter(file_name="../resources/all_laptops.csv")


@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as exception:
        print(exception)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}", ephemeral=True)


@bot.tree.command(name="recommend")
@app_commands.describe(max_price="The budget for the laptop, in dollars",
                       min_rating="The smallest admissible rating for the laptop (optional)")
async def recommend(interaction: discord.Interaction, max_price: int, min_rating: int = None):
    df_with_filtered_laptops = laptop_filter.sort_and_filter_by(price=max_price, rating=min_rating)
    # await interaction.response.send_message(f"{interaction.user.name} said: {max_price} with {min_rating}",
    #                                         ephemeral=True)
    output = t2a(
        header=df_with_filtered_laptops.columns.tolist(),
        body=df_with_filtered_laptops.values.tolist()
    )

    print(output)

    await interaction.response.send_message(f"```\n{df_with_filtered_laptops}\n```",
                                            ephemeral=True)


bot.run(token)
