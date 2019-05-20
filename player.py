
class Player:
    VERSION = "5.01"

    def betRequest(self, game_state):
        players = game_state["players"]
        comm_cards = game_state["community_cards"]
        card1 = ""
        card2 = ""
        us = ""
        for player in players:
            if player["id"] == game_state["in_action"]:
                card1 = player["hole_cards"][0]["rank"]
                card2 = player["hole_cards"][1]["rank"]
                card1suit = player["hole_cards"][0]["suit"]
                card2suit = player["hole_cards"][1]["suit"]

                us = player
                if (card1 in "AKQJ") and (card2 in "AKQJ") :
                    return player['stack']
                elif card1suit == card2suit:
                    return game_state["current_buy_in"] - player["bet"]
                else:
                    return 0

    def showdown(self, game_state):
        pass

