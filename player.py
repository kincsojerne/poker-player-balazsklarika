
class Player:
    VERSION = "4.9"

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
                if game_state['current_buy_in'] < (player['stack'] * 0.1):
                    return game_state['current_buy_in']
                elif (card1 == "A" or card1 == "K" or card1 == "Q" or card1 == "J" or card1 == "10") and (card2 == "A" or card1 == "K" or card1 == "Q" or card1 == "J" or card1 == "10"):
                    return player['stack']
        '''while len(comm_cards) == 0:
            return game_state["current_buy_in"] - (us["bet"] + game_state["minimum_raise"])

        for card in comm_cards:
            if card["rank"] == card1 or card["rank"] == card2:
                return game_state["current_buy_in"] - (us["bet"] + game_state["minimum_raise"])
        if card1 == card2:
            return game_state["current_buy_in"] - (us["bet"] + game_state["minimum_raise"])
        else:
            return game_state["current_buy_in"] - (us["bet"] + game_state["minimum_raise"])'''

    def showdown(self, game_state):
        pass

