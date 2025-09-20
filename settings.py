# Settings for the bot.
import dotenv
import os

dotenv.load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Discord bot token from environment variable
BOT_STATUS = os.getenv("BOT_STATUS", "Example Bot")  # Status text of the bot
BOT_PREFIX = os.getenv("BOT_PREFIX", ".")  # Command prefix
