from dataclasses import dataclass
  
@dataclass
class MySql:
    host : str
    user : str
    passwd : str
    db : str
    
@dataclass
class Cfg:
    mysql : MySql
    botToken : str
    cogs_dir :str
