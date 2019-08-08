from dataclasses import dataclass
from models.factorioModels import Model
from typing import List


@dataclass
class MySql(Model): 
    connectionString : str  #example: "mysql://username:password@www.ip.com:port/database"

@dataclass
class ImageUrls(Model): 
     rockets : str
     playTime : str

@dataclass
class Rcon(Model): 
    host : str
    port : str
    password : str

@dataclass
class Server(Model): 
    serverName : str
    rcon :Rcon

@dataclass
class Cfg(Model):   
    debugMode : bool  #uses debug configuration options
    mysql : MySql
    imageUrls : ImageUrls
    botToken : str
    botTokenDebug : str
    cogs_dir : str
    cmdPrefix : str
    cmdPrefixDebug : str
    servers : List[Server]
    rconTimeout :int
