import json
import random
import bs4


class FrogsGame():
    """Logic for playing frogs game"""

    def __init__(self):
        # initializing game parameters
        self.game_url = "http://www.lutanho.net/play/frogs.html"
        self.NoPossibleMoves = False
        self.previous_state = ""
        self.current_state = ""
        self.next_moves_json = "next_step.json"
        self.next_move = ""
        self.moves = []
        self.memory = "../models/frogs.mm"

    def read_current_state(self, source_code):
        htmlsource = bs4.BeautifulSoup(source_code)
        cells = htmlsource.select('img')
        self.current_state = ""
        i: int = 1
        for img in cells:
            if "frog0" in str(img):
                self.current_state = self.current_state + "0"
            if "frog1" in str(img):
                self.current_state = self.current_state + "1"
            if "frog2" in str(img):
                self.current_state = self.current_state + "2"
            i = i + 1
        return self.current_state

    def print_current_state(self):
        print(self.current_state)

    def write_next_move(self, selector_type, selector, action_type):
        # TODO: Add ability to write several steps at a time, if they all can be executed in one go
        next_steps = {"steps": []}
        next_steps["steps"].append({
            "action": action_type,
            "selectorType": selector_type,
            "selector": selector
        })
        with open(self.next_moves_json, "w") as jsonfile:
            json.dump(next_steps, jsonfile)

    def calculate_possible_moves(self):
        possible_moves = []
        gs = self.current_state # gs -- game state
        for i in range(0,8):
            if gs[i] == "1":
                if gs[i+1] == "0":
                    possible_moves.append(i+1)
                elif (gs[i+1] == "1" or gs[i+1] == "2") and gs[i+2] == "0":
                    possible_moves.append(i + 1)
            elif gs[i] == "2":
                if gs[i-1] == "0":
                    possible_moves.append(i+1)
                elif (gs[i-1] == "1" or gs[i-1] == "2") and gs[i-2] == "0":
                    possible_moves.append(i + 1)
        return possible_moves

    def NextMove(self, source_code):
        # assigning previous and current state
        self.previous_state = self.current_state
        self.current_state = self.read_current_state(source_code)
        print("Previous: " + self.previous_state + ". Current: " + self.current_state)

        # check if the game is not started
        if self.current_state == "":
            self.write_next_move("url", self.game_url, "get")
        else:
            # defining possible actions
            possible_moves = self.calculate_possible_moves()

            # check if there are no possible moves
            if len(possible_moves) == 0:
                self.NoPossibleMoves = True
            elif len(possible_moves) == 1:
                # writing next action instruction
                selector = "tr > :nth-child(" + str(possible_moves[0]) + ") img"
                self.write_next_move("css", selector, "click")
            else:
                print("Calculated possible moves: " + str(possible_moves))
                i = random.randrange(1, len(possible_moves))
                print ("Click on the cell " + str(possible_moves[i]) + ". Current value in " + self.current_state)
                # writing next action instruction
                selector = "tr > :nth-child(" + str(possible_moves[i]) + ") img"
                self.write_next_move("css", selector, "click")

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