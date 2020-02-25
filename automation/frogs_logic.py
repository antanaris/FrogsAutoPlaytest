import json
from typing import Dict

import jsonpath
import bs4


class FrogsGame():
    """Self-learning logic for solving frogs game"""

    def __init__(self):
        # initializing game parameters
        self.NoPossibleMoves = False
        self.current_state: Dict[int, int] = {}
        self.next_moves_json = "frogs_next_step.json"

    def ReadCurrentState(self, source_code):
        htmlsource = bs4.BeautifulSoup(source_code)
        cells = htmlsource.select('img')
        i: int = 1
        for img in cells:
            if "frog0" in str(img):
                self.current_state[i] = 0
            if "frog1" in str(img):
                self.current_state[i] = 1
            if "frog2" in str(img):
                self.current_state[i] = 2
            i = i + 1

    def PrintCurrentState(self):
        print(self.current_state)

    def NextMove(self, source_code):
        # do we need to clean up frogs_next_step.json?

        # read current state from the page source & check if previous move changed the game state
        self.ReadCurrentState(source_code)
        # calculate next move
            # check in the game memory if there is a winning path

            # if no, check in the game memory if there are possible moves (which don't lead to game being lost)

            # if no game memory for self.current_state go to discovery and build the memory

        # assume the game is lost from the game model

        # actual check that there are no possible moves (try all 1 to 9 and see no difference in self.current_state)
        self.NoPossibleMoves = True
        # write next move into frog.json