# Project Code Name: StatBotorio #

`Requires Python 3`

1. [Install](#install "Goto install")
2. [Commands](#commands "Goto commands")


![Licence](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

## Install ##
## Linux Debian based setup (tested on ubuntu)

**Install python3.7 and pip 3.6 to get the lastest pip3.7**

`apt install python3.7 python3-pip -y`

**Install pip3.7** 

`python3.7 -m pip install pip`

**Clone the bot**

`git clone https://github.com/joinandplaycoop/Bot.git`

**Move to the Bot's folder**

`cd Bot`

**Install the requirements with pip and using the requirements file**

`python3.7 -m pip install -r requirements.txt`

**Move to src and run the bot**

```
cd src
python3.7 StatBotorio.py
```
#### Even when you close the session have the bot running (not nessecary)

Run via screen (in the bot/src folder)

`screen -dmS StatsBot python3.7 StatBotorio.py`

## Commands ##
* Admin Commands
  * load [extension_name : str] - Loads an extension
  * unload [extension_name : str] - Unloads an extension
  * reload [extension_name : str] - Reloads an extension
  * cogs - Lits all extensions in directory
  * latency - Bots connection to discord
  * activity [activity : str] - Set the activity of the bot
* Player Stats
  * joined [member : discord.Member] - Says when a member joined.  (@mention player)  
  * ping1 - Debug command from player stats
* Server Stats
  * ping2 - Debug command from server stats
  
