from dataclasses import dataclass
  
@dataclass
class MySql:
    connectionString : str  #example: "mysql://username:password@www.ip.com:port/database"
 
    
@dataclass
class Cfg:   
    debugMode: bool  #uses debug configuration options
    mysql : MySql
    botToken : str
    botTokenDebug : str
    cogs_dir : str
    cmdPrefix : str
    cmdPrefixDebug : str
