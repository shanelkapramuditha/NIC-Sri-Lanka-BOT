from dotenv import dotenv_values
from pyrogram import Client, filters

# Load environment variables
config = dotenv_values(".env")

app = Client(
    config["SESSION_NAME"],
    api_id=config["API_ID"],
    api_hash=config["API_HASH"],
    bot_token=config["BOT_TOKEN"],
)


@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)


app.run()
