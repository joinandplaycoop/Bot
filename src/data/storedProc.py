from typing import List

class PlayersOnline_Result(object):

    def __init__(self, **kwargs):
        self.FKServerId : str = kwargs['FKServerId']
        self.IP : str = kwargs['IP']
        self.TotalPlayersOnline : int = kwargs.get('TotalPlayersOnline')

    @classmethod
    def execute(cls, session) -> List['PlayersOnline_Result']:
        query = 'call PlayersOnline'

        query_result = session.execute(query).fetchall()

        result : List[PlayersOnline_Result] =  list(map(PlayersOnline_Result.bind , query_result))

        return result

    @staticmethod
    def bind(x) :
        return PlayersOnline_Result(FKServerId = x[0],
                                    TotalPlayersOnline= x[1],
				                    IP= x[2])


