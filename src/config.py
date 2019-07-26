import json
from models import *
from dacite import from_dict

class Config(object): 

    __instance = None
    def __new__(cls):
        if Config.__instance is None:
            Config.__instance = object.__new__(cls)
            Config.loadConfig()
        return Config.__instance

    cfg : Cfg = None
   
    @classmethod
    def loadConfig(cls):
        with open('config.json') as json_data_file:
            data = json.load(json_data_file)
            model = from_dict(Cfg,data)
            Config.cfg = model
            print(Config.cfg)

Config.loadConfig()

