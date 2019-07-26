# Project Code Name: StatBotorio
![Licence](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

Requires Python 3

Install Dependencies
From repo directory, run "pip install -r requirements.txt"


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


