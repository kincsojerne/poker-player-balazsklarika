
class Player:
    VERSION = "4.5"

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
                us = player
        for card in comm_cards:
            if comm_cards[card]["rank"] == card1 or comm_cards[card]["rank"] == card2:
                return game_state["current_buy_in"] - (us["bet"] + game_state["minimum_raise"])
        if card1 == card2:
            return game_state["current_buy_in"] - (us["bet"] + game_state["minimum_raise"])
        else:
            return 0

    def showdown(self, game_state):
        pass

