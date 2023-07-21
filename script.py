import discord
import os
from dotenv import load_dotenv

load_dotenv()

user_prompts = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you?": "I'm good, thank you!",
    "what's your name?": "I am ChatBot.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!"
}

class ChatBot(discord.Client):
    async def on_ready(self):
        print(f"We have logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        lowercase_content = message.content.lower()
        response = user_prompts.get(lowercase_content)
        if response:
            await message.channel.send(response)

def main():
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("Please set the BOT_TOKEN environment variable.")
    
    bot = ChatBot()
    bot.run(bot_token)

if __name__ == "__main__":
    main()