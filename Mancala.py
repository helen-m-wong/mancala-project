# Author: Helen Wong
# GitHub username: helen-m-wong
# Date: 11/29/22
# Description:

class InvalidPitIndex(Exception):
    """User-defined exception for invalid pit index number (>6 or <=0)"""
    pass


class Mancala:
    """Represents mancala game, played by 2 players. Players are not enforced to take turns in order for
    testing purposes"""

    def __init__(self):
        """Constructor for Mancala class."""

        self._players = []
        self._player_1_pits = [4, 4, 4, 4, 4, 4]
        self._player_2_pits = [4, 4, 4, 4, 4, 4]

        self._player_1_store = 0
        self._player_2_store = 0

        self._state = None

    def get_players(self):
        """FILL IN LATER"""
        return self._players

    def get_player_1_pits(self):
        """FILL IN LATER"""
        return self._player_1_pits

    def get_player_2_pits(self):
        """FILL IN LATER"""
        return self._player_2_pits

    def get_player_1_store(self):
        """FILL IN LATER"""
        return self._player_1_store

    def get_player_2_store(self):
        """FILL IN LATER"""
        return self._player_2_store

    def get_state(self):
        """FILL IN LATER"""
        return self._state

    def create_player(self, name):
        """Takes one parameter: name of player. Uses Player class to create player for Mancala class."""
        player = Player(name)
        player_name = player.get_name()
        self._players.append(player_name)
        return player

    def play_game(self, player_num, pit_index):
        """Takes two parameters: (1) player number (either 1 or 2) and (2) pit index. If user inputs invalid
        pit index number, returns error message. If game is ended, returns “Game is ended”. If player wins
        an extra round due to special rule, prints message that player takes another round. At end of turn,
        returns list of current seed number for both players pits and stores."""
        try:
            if pit_index > 6 or pit_index <= 0:
                raise InvalidPitIndex
        except InvalidPitIndex:
            print("Invalid number for pit index")
        return

    def print_board(self):
        """Prints the current board information including:
            number of seeds in player 1's store
            number of seeds in player 1's pits from 1 to 6 in a list
            number of seeds in player 2's store
            number of seeds in player 2's pits from 1 to 6 in a list"""

        store_1 = self.get_player_1_store()
        pits_1 = self.get_player_1_pits()
        store_2 = self.get_player_2_store()
        pits_2 = self.get_player_2_pits()
        print(f"player1:\nstore: {store_1}\n{pits_1}\nplayer2:\nstore: {store_2}\n{pits_2}")
        return

    def return_winner(self):
        """Takes no parameters.
If game is ended, returns message declaring which player is the winner and their name.

If game is a tie, return message stating the game is a tie.

If game is not ended yet, return message stating game has not ended yet."""
        return


class Player:
    """Represents player in mancala game"""

    def __init__(self, name):
        """Constructor for Player class. Takes name of player as parameter."""
        self._name = name

    def get_name(self):
        """Returns name of player"""
        return self._name


game = Mancala()
player1 = game.create_player("Lily")
player2 = game.create_player("Lucy")
game.print_board()
print(game.get_players())
game.play_game(1, 7)
