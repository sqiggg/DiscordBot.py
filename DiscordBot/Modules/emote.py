import json
import GeneralFunctions as GenFun

def emotes(message, messageObj):

    if len(message) == 0:
        return['Syntax is wrong: \n example: $emote -add kappa -link "http://goo.gl/ZEX6KN"', messageObj.channel]

    if '-help' in message:
        return["Usage, $emote -add <name> -link <\"link of image\"> -list  for list  -del <\"name\">to delete\n Please insure that there are quotes around the link \n Please use https://goo.gl/ to shorten the url.", messageObj.channel]

    elif '-list' in message:
        jsonTxt = GenFun.retrieveUrl()
        jsonTxt = jsonTxt['Emotes']
        messageTxt = ''

        for x in jsonTxt.keys():
            messageTxt = messageTxt + str(x)[0].upper() + str(x)[1:len(x)] + '\n'

        return[messageTxt, messageObj.channel]

    else:
        if '-link' in message or '-add' in message and '-list' in message or '-del' in message:

            message = message.replace(" ", "")

            jokes = GenFun.retrieveUrl()
            tmpJokes = jokes
            jokes = jokes["Emotes"]

            if '-del' in message:
                emoteToDel = message[message.find('-del"')+len('-del"'):message.rfind('"', 0, len(message))].lower()
                if len(emoteToDel) == 0:
                    return["ERROR nothing to delete",messageObj.channel]

                for x in jokes.keys():

                    if jokes[x]['trigger'] == emoteToDel:
                        jokes.pop(x, None)

                        tmpJokes['Emotes'] = jokes
                        GenFun.store(json.dumps(tmpJokes, indent=4, separators=(',', ': ')))

                        return['Deleted successfully', messageObj.channel]

                return["ERROR Something went wrong",messageObj.channel]



            if message[len(message)-1] == '"':

                add = message[message.find("-add")+len("-add"):message.find("-link")]
                link = message[message.find("-link")+len('-link"'):len(message)-1]

                if jokes.has_key(add):
                    return["That emote already exists!", messageObj.channel]
                else:
                    jokes[add] = {'response':link, 'trigger':add.lower()}

                    tmpJokes['Emotes'] = jokes

                    GenFun.store(json.dumps(tmpJokes, indent=4, separators=(',', ': ')))

                    return ["Successful", messageObj.channel]
                print "*EMOTE*"


            else:
                return['Syntax is wrong: \n example: $emote -add kappa -link "http://goo.gl/ZEX6KN"', messageObj.channel]

        else:
            return['Syntax is wrong: \n example: $emote -add kappa -link "http://goo.gl/ZEX6KN"', messageObj.channel]
            pass
