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
        self._board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._state = None

    def get_players(self):
        """FILL IN LATER"""
        return self._players

    def get_board(self):
        """FILL IN LATER"""
        return self._board

    def get_player_1_pits(self):
        """FILL IN LATER"""
        return self._board[0:6]

    def get_player_2_pits(self):
        """FILL IN LATER"""
        return self._board[7:13]

    def get_player_1_store(self):
        """FILL IN LATER"""
        return self._board[6]

    def get_player_2_store(self):
        """FILL IN LATER"""
        return self._board[13]

    def get_state(self):
        """FILL IN LATER"""
        return self._state

    def set_state(self, state):
        """FILL IN LATER"""
        self._state = state

    def player_1_pits_sum(self):
        """FILL IN LATER"""
        player_1_sum = 0
        for index in range(0, 6):
            player_1_sum += self._board[index]
        return player_1_sum

    def player_2_pits_sum(self):
        """FILL IN LATER"""
        player_2_sum = 0
        for index in range(7, 13):
            player_2_sum += self._board[index]
        return player_2_sum

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
            return "Invalid number for pit index"

        if self.player_1_pits_sum() == 0 or self.player_2_pits_sum() == 0:
            self.set_state("ended")
            return "Game is ended"
        elif player_num == 1:
            num_seeds = self._board[pit_index-1]
            self._board[pit_index-1] = 0
            return self.rec_play_game(player_num, pit_index, num_seeds)
        elif player_num == 2:
            num_seeds = self._board[13-pit_index]
            self._board[13-pit_index] = 0
            return self.rec_play_game(player_num, 14-pit_index, num_seeds)

    def rec_play_game(self, player_num, index, num_seeds):
        """FILL IN LATER"""

        if player_num == 1:
            if num_seeds == 0:
                if index == 7:
                    print("player 1 take another turn")
                    return self.get_board()
                if index in range(1, 7) and self._board[index-1] == 1 and self._board[12-(index-1)] >= 1:
                    extra_seeds = self._board[12-(index-1)] + 1
                    self._board[12-(index-1)] = 0
                    self._board[index - 1] = 0
                    self._board[6] += extra_seeds
                    return self.get_board()
                else:
                    return self.get_board()
            if index == 13 and num_seeds != 0:
                return self.rec_play_game(player_num, 0, num_seeds)
            else:
                self._board[index] += 1
                num_seeds -= 1
                index += 1
                return self.rec_play_game(player_num, index, num_seeds)

        if player_num == 2:
            if num_seeds == 0:
                if index == 14:
                    print("player 2 take another turn")
                    return self.get_board()
                if index in range(8, 13) and self._board[index-1] == 1:
                    if self._board[12-(index-1)] >= 1:
                        extra_seeds = self._board[12 - (index - 1)] + 1
                        self._board[12 - (index - 1)] = 0
                        self._board[index-1] = 0
                        self._board[13] += extra_seeds
                        return self.get_board()
                else:
                    return self.get_board()
            if index == 14 and num_seeds != 0:
                return self.rec_play_game(player_num, 0, num_seeds)
            if index == 6:
                return self.rec_play_game(player_num, 7, num_seeds)
            else:
                self._board[index] += 1
                num_seeds -= 1
                index += 1
                return self.rec_play_game(player_num, index, num_seeds)

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


def main():  # Runs if file is run as a script
    game = Mancala()
    player1 = game.create_player("Lily")
    player2 = game.create_player("Lucy")
    game.print_board()
    print(game.get_players())
    print(game.play_game(1, 7))
    print(game.play_game(1, 3))
    print(game.play_game(1, 6))
    print(game.play_game(2, 5))
    print(game.play_game(2, 6))


if __name__ == "__main__":
    main()
