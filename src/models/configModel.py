from dataclasses import dataclass

class configModel(object):
    """Config Model"""
    
@dataclass
class Cfg:
    mysql: dict
    botToken: str

@dataclass
class MySql:
    host: str
    user: str
    passwd: str
    db: str