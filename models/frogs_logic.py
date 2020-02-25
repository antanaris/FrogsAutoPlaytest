import json

import bs4


class FrogsGame():
    """Self-learning for solving frogs game using memory"""

    def __init__(self):
        # initializing game parameters
        self.NoPossibleMoves = False
        self.current_state = ""
        self.next_moves_json = "next_step.json"
        self.moves = []
        self.memory = "../models/frogs.mm"

    def ReadCurrentState(self, source_code):
        htmlsource = bs4.BeautifulSoup(source_code)
        cells = htmlsource.select('img')
        i: int = 1
        for img in cells:
            if "frog0" in str(img):
                self.current_state = self.current_state + "0"
            if "frog1" in str(img):
                self.current_state = self.current_state + "1"
            if "frog2" in str(img):
                self.current_state = self.current_state + "2"
            i = i + 1

    def PrintCurrentState(self):
        print(self.current_state)

    def NextMove(self, source_code):
        # check if we have the current state memory
        with open(self.memory) as json_file:
            frog_memory = json.loads(json_file.read())

        def cs(i):
            state = str(self.current_state)
            return state[i]

        def cell_dict(i):
            return dict(order=cs(i), state=0, result=0, winning_path=0, loosing_path=0)

        def new_memory():
            return dict({cs: [cell_dict(1), cell_dict(2), cell_dict(3), cell_dict(4), cell_dict(5), cell_dict(6), cell_dict(7), cell_dict(8), cell_dict(9)]})
        #print(str(new_memory()))
        print(cs(1))

        # do we need to clean up frogs_next_step.json?

        # defining possible actions
        i = int(1)
        i_min = 1
        i_max = 9
        def possible_action(i):
            return dict(type="click", selectorType="css", selector="tr > :nth-child(" + str(i) + ") img")

        with open(self.memory) as json_file:
            frog_memory = json.loads(json_file.read())

        # read current state from the page source & check if previous move changed the game state
        self.ReadCurrentState(source_code)
        print("Current state: " + self.current_state +". Calculating next move")
        # calculate next move
            # check in the game memory if there is a winning path

            # if no, check in the game memory if there are possible moves (which don't lead to game being lost)

            # if no game memory for self.current_state go to discovery and build the memory

        # assume the game is lost from the game model

        # actual check that there are no possible moves (try all 1 to 9 and see no difference in self.current_state)
        self.NoPossibleMoves = True
        # write next move into frog.json

    def is_won(self, alert_text):
        moves = 0
        time = 0
        # TODO: extract number of moves and time from the alert text
        # print("Game is won in " + str(moves) + " moves, " + str(time) + " sec")
        print(alert_text)
        # update game memory with info about winning path

    def is_lost(self):
        print("Game is lost. No possible moves")
        # update game memory with info about loosing path