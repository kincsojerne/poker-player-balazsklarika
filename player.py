
class Player:
    VERSION = "3.2"

    def betRequest(self, game_state):
        players = game_state["players"]
        card1 = ""
        card2 = ""
        us = ""
        for player in players:
            if player["id"] == game_state["in_action"]:
                card1 = player["hole_cards"][0]["rank"]
                card2 = player["hole_cards"][1]["rank"]
                us = player
        if card1 == card2:
            return game_state["current_buy_in"] - (us["bet"] + game_state["minimum_raise"])
        else:
            return 900

    def showdown(self, game_state):
        pass

