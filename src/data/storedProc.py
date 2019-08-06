from typing import List
from utilities.diagnostics import executionTime
from data.session import Session
import data.session
from MySQLdb import OperationalError

def sqlFunc():
    #if DB session disconects, attempt to reconect 1 time.
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except OperationalError as e:
                if 'MySQL server has gone away' in str(e):
                    data.session.connect()
                    return func(*args, **kwargs)
                print(e)
        return wrapper
    return decorator

class PlayersOnline_Result(object):

    def __init__(self, **kwargs):
        self.FKServerId : str = kwargs['FKServerId']
        self.IP : str = kwargs['IP']
        self.TotalPlayersOnline : int = kwargs.get('TotalPlayersOnline')
        self.Status : int = kwargs.get('Status')
        self.Version : int = kwargs.get('Version')
        self.IsResetting : int = kwargs.get('IsResetting')

   
        
    @classmethod
    @executionTime()
    @sqlFunc()
    def execute(cls) -> List['PlayersOnline_Result']: 

        session = Session()

        query = 'call PlayersOnline' 

        query_result = session.execute(query).fetchall()

        result : List[PlayersOnline_Result] =  list(map(PlayersOnline_Result.bind , query_result))

        return result

    @staticmethod
    def bind(x) :
        return PlayersOnline_Result(FKServerId = x[0],
                                    TotalPlayersOnline= x[1],
				                    IP= x[2],
                                    Status = x[3],
                                    Version = x[4],
                                    IsResetting = x[5])
    
    
