<p align="center">
  <a href="https://joinandplaycoop.com/">
    <img alt="logo" src="https://i.imgur.com/2mH4I3j.png" width="120">
  </a>
  <br>
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/joinandplaycoop/Bot.svg">
  <a href="http://github.com/joinandplaycoop/Bot/fork">
    <img src="https://img.shields.io/github/forks/joinandplaycoop/Bot?label=Forks" alt="Fork">
  </a>
  <a href="https://discord.joinandplaycoop.com">
    <img src="https://discordapp.com/api/guilds/420865611279630336/widget.png?style=shield" alt="Discord">
  </a>
</p>
<h2 align="center">Join and Play Coop repository</h2>
<h3>Project Code Name: StatBotorio</h3>

`Requires Python 3`

1. [Install](#install "Goto install")
2. [Commands](#commands "Goto commands")


![Licence](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

## Install ##
## Linux Debian based setup (tested on ubuntu)

**Install python3.7 and pip 3.6 to get the lastest pip3.7**
```
apt install python3.7 python3-mysqldb python3-apt python3-pip python3.7-dev default-libmysqlclient-dev -y
```

**Clone the bot**
```
git clone https://github.com/joinandplaycoop/Bot.git
```
**Move to the Bot's folder**
```
cd Bot
```
**Install the requirements with pip and using the requirements file**
```
python3.7 -m pip install -r requirements.txt
```
**Move to src and run the bot**

```
cd src
python3.7 StatBotorio.py
```

##### If you have any issues with a module try to run this 
```
apt remove python3-apt
apt install python3-apt
apt install python-mysqldb
apt install python3.7-dev default-libmysqlclient-dev
```


**Config**

remove ".example" from the file called "config.json.example"
populate the botToken and the connection string for MySql

**Update Database schema**

If the schema is updated in the database, the models will have to be updated also.
the models are are contained in data/schema.py
use sqlcodegen to generate the models automatically with your MySql Connection string.
Here is an example:

use sqlacodegen --outfile schema.py mysql://username:password@www.ip.com:port/database

#### Even when you close the session have the bot running (not nessecary)

Run via screen (in the bot/src folder)
```
screen -dmS StatsBot python3.7 StatBotorio.py
```
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
  * online - Shows table of who is online
* Debug (realoded in python every command.  live testing)
  * t1 - test 1 command for development
  
