from dataclasses import dataclass
  
@dataclass
class MySql:
    connectionString : str  #example: "mysql://username:password@www.ip.com:port/database"
@dataclass
class ImageUrls:
     rockets : str

@dataclass
class Rcon:
    host : str
    port : str
    password : str
    timeout :int

@dataclass
class Cfg:   
    debugMode : bool  #uses debug configuration options
    mysql : MySql
    imageUrls : ImageUrls
    botToken : str
    botTokenDebug : str
    cogs_dir : str
    cmdPrefix : str
    cmdPrefixDebug : str
    rcon : Rcon
