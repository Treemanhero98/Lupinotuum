import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'test':
            #await message.channel.send('pong')
            print("Received")

client = MyClient()
file = open("token.txt","r")
token = file.readline()
try:
    client.run(token)
except LoginFailure as exception:
    if str(exception) == 'Improper token has been passed.':
        print('Improper token has been passed. Did you forget to edit token.txt?')
    else:
        print(exception)
