import os
import re
import discord
from discord import app_commands
from discord.ext import commands

# --- CONFIGURATION ---
TOKEN = os.getenv("DISCORD_TOKEN")  # récupéré depuis Render (jamais dans le code)
GUILD_ID = 1291147657892331604
TRAVIAN_URL = "https://ts4.x1.international.travian.com/position_details.php"

# --- INITIALISATION ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- ÉVÉNEMENT DE CONNEXION ---
@bot.event
async def on_ready():
    print(f"🤖 Connecté en tant que {bot.user}")
    try:
        guild = discord.Object(id=GUILD_ID)
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
        print("✅ Commandes synchronisées avec ton serveur !")
    except Exception as e:
        print(f"⚠️ Erreur de synchronisation : {e}")

# --- COMMANDE SLASH ---
@bot.tree.command(name="coord", description="Donne un lien Travian TS4 pour les coordonnées")
@app_commands.describe(coords="Coordonnées au format x/y (ex: -10/25)")
async def coord(interaction: discord.Interaction, coords: str):
    try:
        if "/" not in coords:
            await interaction.response.send_message(
                "⚠️ Format invalide ! Utilise `/coord coords: -10/25`",
                ephemeral=True
            )
            return

        x_str, y_str = coords.split("/")
        x, y = int(x_str), int(y_str)

        if not (-200 <= x <= 200 and -200 <= y <= 200):
            await interaction.response.send_message(
                f"⚠️ Coordonnées invalides : ({x}, {y}) doivent être entre -200 et 200.",
                ephemeral=True
            )
            return

        link = f"{TRAVIAN_URL}?x={x}&y={y}"
        await interaction.response.send_message(
            f"🌍 **Coordonnées :** ({x}, {y})\n🔗 [Voir sur la carte]({link})"
        )

    except ValueError:
        await interaction.response.send_message(
            "⚠️ Les coordonnées doivent être des nombres valides !",
            ephemeral=True
        )

# --- DÉTECTION AUTOMATIQUE ---
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    match = re.search(r"(-?\d{1,3})/(-?\d{1,3})", message.content)
    if match:
        x = int(match.group(1))
        y = int(match.group(2))
        if -200 <= x <= 200 and -200 <= y <= 200:
            url = f"{TRAVIAN_URL}?x={x}&y={y}"
            await message.channel.send(
                f"🌍 **Coordonnées détectées :** ({x}, {y})\n🔗 [Voir sur la carte TS4]({url})"
            )

    await bot.process_commands(message)

# --- LANCEMENT ---
print("🟢 Démarrage du bot Travian en cours...")
bot.run(TOKEN)
