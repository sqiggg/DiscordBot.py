import random
#a roll bot
def rollBot(message, messageObj):

    #getting the times and die from the syntax $roll <dice>d<number> e.g $roll 2d6
    times = int(message[0:message.find('d')])
    die = int(message[message.find('d')+1:len(message)])

    rolls = []
    total = 0

    #rolling and calculating the total
    for x in range(times):
        currentRoll = random.randint(1, die)
        rolls.append(currentRoll)
        total += currentRoll

    #-----
    rollsStr = str(rolls[0])
    rolls = rolls[0:]

    for x in rolls:
        rollsStr = str(rollsStr) + ' + ' + str(x)
    #------

    #sending the message with bold and italic formating. See the Discord formating page to find out the Syntax
    # https://support.discordapp.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-
    message = '*' + str(messageObj.author) + ' rolled ' + str(times) + 'd' + str(die) + ':*\n' + rollsStr + ' = **' + str(total) + '**'


    return[message, messageObj.channel]
