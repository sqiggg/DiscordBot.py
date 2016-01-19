# DiscordBot.py
A [Discord](https://discordapp.com/) Bot using [Discord.py](https://github.com/Rapptz/discord.py) with a rollbot and emote support.

**Features**
* Cloud integration with a local database and a cloud database running on the NodeJs server.
* Trigger words for jokes

**Thing to work on**
* Update to OAuth API when Discord make an official API
* Going to add an edit function to the `$emote` command
* Adding databases to seperate channels


**Requirements**
* *Python 2.7*
* *Discord.py* - cam be got with `pip install discord.py`
* *json* - comes with Python 2.7
* *urllib2* - comes with Python 2.7
* *random* - comes with Python 2.7

**Commands**
* `$roll <dice>d<times>` rolls some dice
* `$emote [-list] [-add <name>, -link "<link to image/gif>"]` adds a trigger to the url/text
