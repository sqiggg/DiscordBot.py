import discord
import re

#import files
import sys
sys.path.insert(0, 'Modules/')
import rollBot
import emote
import GeneralFunctions as GenFun

#starting a discord bot for more documentation see https://github.com/Rapptz/discord.py
client = discord.Client()
client.login('username', "password")

#FUNCTION
def send(message, channel):
    #simple send command again see https://github.com/Rapptz/discord.py
    client.send_message(channel, message)
def response(message):

    #gets message from user and sees what to do with it
    json = GenFun.retrieveUrl()
    json = json['Emotes']

    #checking if there are any trigger words for emotes that need to be dealt with
    for x in json.keys():

        if re.search(r"\b" + re.escape(str(json[x]['trigger'])) + r"\b", str(message.content).lower()):
            textMessage = json[x]['response']
            client.send_message(message.channel, textMessage)

    #checking for a mention in a conversation
    if 'bot ' in str(message.content).lower() or ' bot' in str(message.content).lower():
        #casually interupting the conversation
        textMessage = "You mentioned me " + str(message.author) + '!'
        client.send_message(message.channel, textMessage)

    #checking this phrase
    if 'press f to pay respect' in str(message.content).lower().strip():
        textMessage = 'f'
        #spamming f exactly enough times to fill up the screen on a normal brower window
        for x in range(0, 23):
            client.send_message(message.channel, textMessage)
def commands(message):

    #commands
    #checking if the roll command has been used
    if str(message.content).startswith('$roll'):
        command = str(message.content)[len('$roll'):len(message.content)]
        #dealing with multiple spaces
        command = command.strip(' ')
        #logging it to the console
        print str(message.author) + " used the *roll* command"


        if len(command) == 0:
            #error message
            send("Syntax is wrong: \n example: $roll 2d6", message.channel)
        else:

            if 'd' not in command:
                #error message
                send("Syntax is wrong: \n example: $roll 2d6", message.channel)
                pass
            else:
                #sending the command to the rollbot
                returnData = rollBot.rollBot(command, message)
                send(returnData[0],returnData[1])

    #checking for the emote command
    if str(message.content).startswith('$emote'):
        command = str(message.content)[len('$emote'):len(message.content)]

        #sending the emote command to emote
        returnData = emote.emotes(command, message)
        send(returnData[0],returnData[1])

        #updating the cloud database
        GenFun.sendJson(GenFun.retrieve())


    #printing the rules
    if str(message.content).startswith('$rules'):

        #getting the json from the cloud
        rules = GenFun.retrieveUrl()
        rules = rules["Rules"]
        rulestxt = ''

        #Printing them
        for x in range(1, len(rules.keys())+1):
            rulestxt = rulestxt + str(rules[str(x)]) + '\n'
        send(rulestxt,message.channel)

#END OF FUNCTIONS
@client.event
def on_message(message):

    if message.author.id != client.user.id:
        #logging the message to the console
        print str(message.author) + ': ' + str(message.content)

        if message.content.startswith('$'):
            commands(message)

        response(message)

@client.event
def on_ready():
    #initial retrieve
    GenFun.retrieveUrl()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


#running the client
client.run()
