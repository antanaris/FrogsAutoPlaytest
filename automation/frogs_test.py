# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import frogs_logic

import json
import jsonpath


# Starting testcases
class Frogs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.lutanho.net/play/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_frogs(self):
        driver = self.driver
        game = frogs_logic.FrogsGame()
        driver.get("http://www.lutanho.net/play/frogs.html")

        while (self.is_alert_present() == False ) and (game.NoPossibleMoves == False):
        # Calculate next movement based on the changes of the game state and write json with next move
            game.NextMove(driver.page_source)
            # load next move from frogs.json and execute it if there are possible moves
            if game.NoPossibleMoves == False:
                self.executeSteps(game.next_moves_json)

            # if success -- empty frogs_next_step.json

        if self.is_alert_present():
            # game is won
            self.assertIn("Super, you solved this game", self.close_alert_and_get_its_text())
            # calculate and write the game stats to memory

            print("Game is won")
        elif game.NoPossibleMoves:
            # game is lost
            # No possible moves
            self.assertEqual(game.NoPossibleMoves, True)
            # calculate and write the game stats to memory

            print("Game is lost. No possible moves")
        else:
            # we're not supposed to get here, unless something went wrong
            print("Something went wrong")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def executeSteps(self, steps_json_url):
        step = 0
        type = ""
        selectorType = ""
        selector = ""

        driver = self.driver

        # Read the json file
        print("Preparing to load next steps json file")
        with open(steps_json_url) as json_file:
            next_steps_json = json.load(json_file)

        # Get the list of steps to execute


        # Run the steps with selenium driver
        if selectorType == "css":
            if type == "click":
                driver.find_element_by_xpath(selector).click()

if __name__ == "__main__":
    unittest.main()
