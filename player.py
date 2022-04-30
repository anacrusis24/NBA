##### IMPORTS #####

# NBA
import nba_api as nba
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playercareerstats

# General
import pandas as pd
import numpy as np


##### PLAYER CLASS #####
class Player:
    def __init__(self, first_name, last_name, height=0, weight=0):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight

    def get_height(self):
        pass

    def get_weight(self):
        pass