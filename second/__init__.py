from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'second'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def group_by_arrival_time_method(subsession, waiting_players):
    print('called group_by_arrival_time_method')
    print(waiting_players)
    
    if len(waiting_players) >= 4:
        return waiting_players[:4]


# PAGES
class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True


class Results(Page):
    pass


page_sequence = [ResultsWaitPage, Results]
