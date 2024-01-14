import discord
from discord import app_commands
from discord.ext import commands
from trelloAPI import *

def run_discord_bot():
    
    intents = discord.Intents.default()
    #Enter your Discord Token here
    TOKEN = "YOUR TOKEN"

    client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

    @client.command()
    async def syncBot(ctx):    
        print("Started synching the bot.")        
        commands = await client.tree.sync()
        print("These are the commands that are synched:",commands)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running.')
        
    @client.tree.command()
    async def edit_bug(interaction: discord.Interaction,card_id:str,text:str):
        
        bugCard = change_card_on_trello_list(cardId=card_id,cardDescription=text)

        if bugCard:
            reply = f"I edited a trello card for this issue.\nClick here to watch it: {bugCard.url}\nCard_ID: {bugCard.id}"
        else:
            reply = f"Couldn't find the trello ID."

        await interaction.response.send_message(reply)

    @client.event
    async def on_message(message):
        if client.user in message.mentions:
            content = message.content.replace(f"<@{client.user.id}>", "").strip()
            
            if message.reference:
                referenced_message = await message.channel.fetch_message(message.reference.message_id)                
                referenced_message.content += f"\nLink: {message.jump_url}" 
                bugCard = new_card_on_trello_list(content,referenced_message.content)
                
            else:
                
                linkToMessage = f"Link: {message.jump_url}"
                bugCard = new_card_on_trello_list(content,linkToMessage)
            
            reply = f"I created a trello card for this issue.\nClick here to watch it: {bugCard.url}\nCard_ID: {bugCard.id}"
            
            await message.reply(reply)

    client.run(TOKEN)

run_discord_bot()