from typing import List

class PlayersOnline_Result(object):

    def __init__(self, **kwargs):
        self.fk_server : str = kwargs['fk_server']
        self.number_of_players_connected : int = kwargs.get('number_of_players_connected')
        self.number_of_total_players : int = kwargs.get('number_of_total_players')
        self.date : datetime = kwargs.get('date')

    @classmethod
    def execute(cls, session) -> List['PlayersOnline_Result']:
        query = 'call PlayersOnline'

        query_result = session.execute(query).fetchall()

        result : List[PlayersOnline_Result] =  list(map(PlayersOnline_Result.bind , query_result))

        return result

    @staticmethod
    def bind(x) :
        return PlayersOnline_Result(fk_server = x[0],
                                number_of_players_connected= x[1],
                                number_of_total_players= x[2],
                                date= x[3])


