# Author: Helen Wong
# GitHub username: helen-m-wong
# Date: 11/30/22
# Description: Represents a text-based version of the two-player Mancala board game. Defines Mancala class to create
# and initialize the board. Defines Player class to create players for the game. Mancala class contains methods
# that allows user to take turns based on player number. Players are not enforced to take turns in order for
# testing purposes.
#
# General Rules:
# On each turn, the player 'picks up' all the seeds in the chosen pit on the player’s side and places one seed in each
# of the pits to the right until no seeds remain. If the player’s store is reached, a seed is added to the store.
# Seeds may be added to the other player's pits but not their store.
#
# The game ends when one player’s pits are empty. At this point, the other player takes the seeds remaining in
# their own pits and adds them to their store. Whoever has the most seeds when the game ends is the winner.
#
# Special Rules:
# 1. If the last seed lands in the player’s store, the player takes another turn.
# 2. If the last seed lands in one of the player’s pits and if that pit was previously empty, the player takes all
# the seeds in the other player's opposite pit and the last seed played their own and adds them into their own store.

class InvalidPitIndex(Exception):
    """User-defined exception for invalid pit index number (>6 or <=0)"""
    pass


class Mancala:
    """Represents mancala game, played by 2 players."""

    def __init__(self):
        """Constructor for Mancala class.

        Initializes players to empty list
        Initializes board starting state in the format: [player1 pit1, player1 pit2, player1 pit3, player1 pit4,
        player1 pit5, player1 pit6, player1 store, player2 pit1, player2 pit2, player2 pit3, player2 pit4,
        player2 pit5, player2 pit6, player2 store]
        Initializes state to None"""

        self._players = []
        self._board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._state = None

    def get_players(self):
        """Returns list of player names"""
        return self._players

    def get_board(self):
        """Returns current state of board"""
        return self._board

    def get_player_1_pits(self):
        """Returns list with player 1's seed numbers from pit 1 to 6"""
        return self._board[0:6]

    def get_player_2_pits(self):
        """Returns list with player 2's seed numbers from pit 1 to 6"""
        return self._board[7:13]

    def get_player_1_store(self):
        """Returns number of seeds in player 1's store"""
        return self._board[6]

    def get_player_2_store(self):
        """Returns number of seeds in player 2's store"""
        return self._board[13]

    def get_state(self):
        """Returns state of game. Will return "ended" if game has ended, otherwise returns None."""
        return self._state

    def set_state(self, state):
        """Sets state of game to new state"""
        self._state = state

    def player_1_pits_sum(self):
        """Returns sum of player 1's seeds from pit 1 to 6"""
        player_1_sum = 0
        for index in range(0, 6):
            player_1_sum += self._board[index]
        return player_1_sum

    def player_2_pits_sum(self):
        """Returns sum of player 2's seeds from pit 1 to 6"""
        player_2_sum = 0
        for index in range(7, 13):
            player_2_sum += self._board[index]
        return player_2_sum

    def create_player(self, name):
        """Takes one parameter: name of player. Returns player object created by Player class.
        Adds name of player to end of players list"""
        player = Player(name)
        player_name = player.get_name()
        self._players.append(player_name)
        return player

    def play_game(self, player_num, pit_index):
        """Takes two parameters: (1) player number (either 1 or 2) and (2) pit index [1,6].

        If user inputs invalid pit index number, returns error message.
        If game is ended, returns “Game is ended”.

        'Picks up' all the seeds in pit (represented by pit_index) on player_num's side and places one seed
        in each of the pits to the right until no seeds remain. If player_num's store is reached, a seed is
        added to the store. Seeds may be added to the other player's pits but not their store.

        Special Rules:
        1. If the last seed lands in player_num's store, prints message for player to take another turn.
        2. If the last seed lands in one of player_num's pits and if that pit was previously empty, take all the
        seeds in the other player's opposite pit and the last seed played on player_num's side and
        add them into player_num's store.

        At end of turn, returns list with current state of board."""

        # checks for invalid pit index number
        try:
            if pit_index > 6 or pit_index <= 0:
                raise InvalidPitIndex
        except InvalidPitIndex:
            return "Invalid number for pit index"

        # checks if game has already ended
        if self.player_1_pits_sum() == 0 or self.player_2_pits_sum() == 0:
            return "Game is ended"
        # records number of seeds in player's specified pit at start of turn and sets indexed value to 0;
        # calls recursive helper method to distribute seeds and check if game is ended after the turn
        elif player_num == 1:
            num_seeds = self._board[pit_index-1]
            self._board[pit_index-1] = 0
            return self.rec_play_game(player_num, pit_index, num_seeds)
        elif player_num == 2:
            num_seeds = self._board[pit_index+6]
            self._board[pit_index+6] = 0
            return self.rec_play_game(player_num, pit_index+7, num_seeds)

    def rec_play_game(self, player_num, index, num_seeds):
        """Recursive play game helper method. Recursively distributes seeds across board following special rules.
        Calls end_check method to check if game has ended after turn."""

        if player_num == 1:
            if num_seeds == 0:
                # checks if special rule 1 is applicable
                if index == 7 and self.player_1_pits_sum() != 0:
                    print("player 1 take another turn")
                    return self.get_board()
                # checks if special rule 2 is applicable
                if index in range(1, 7) and self._board[index-1] == 1:
                    # determines total number of seeds to be added to player 1's store
                    extra_seeds = self._board[12-(index-1)] + 1
                    self._board[12-(index-1)] = 0
                    self._board[index-1] = 0
                    # adds seeds to player 1's store
                    self._board[6] += extra_seeds
                    return self.end_check()
                else:
                    return self.end_check()
            # prevents seeds from being added to player 2's store
            if index == 13 and num_seeds != 0:
                return self.rec_play_game(player_num, 0, num_seeds)
            else:
                self._board[index] += 1  # adds 1 seed to next pit
                num_seeds -= 1  # decrements number of seeds by 1
                index += 1  # moves to next pit
                return self.rec_play_game(player_num, index, num_seeds)

        if player_num == 2:
            if num_seeds == 0:
                # checks if special rule 1 is applicable
                if index == 14 and self.player_2_pits_sum() != 0:
                    print("player 2 take another turn")
                    return self.get_board()
                # checks if special rule 2 is applicable
                if index in range(8, 14) and self._board[index-1] == 1:
                    # determines total number of seeds to be added to player 2's store
                    extra_seeds = self._board[12 - (index-1)] + 1
                    self._board[12 - (index-1)] = 0
                    self._board[index-1] = 0
                    # adds seeds to player 2's store
                    self._board[13] += extra_seeds
                    return self.end_check()
                else:
                    return self.end_check()
            # prevents index from going out of range before seeds are all distributed
            if index == 14 and num_seeds != 0:
                return self.rec_play_game(player_num, 0, num_seeds)
            # prevents seeds from being added to player 1's store
            if index == 6:
                return self.rec_play_game(player_num, 7, num_seeds)
            else:
                self._board[index] += 1
                num_seeds -= 1
                index += 1
                return self.rec_play_game(player_num, index, num_seeds)

    def end_check(self):
        """Returns list of current state of board after checking if game has ended after turn.
        If sum of either player's pits is 0, the game is ended and the other player takes the seeds
        remaining in their own pits and adds them to their store.
        If game is ended, set_state method is called to update state of the game."""

        # takes all seeds remaining in player 2's pits and adds them to player 2's store
        if self.player_1_pits_sum() == 0:
            self._board[13] += self.player_2_pits_sum()
            for index in range(7, 13):
                self._board[index] = 0
            self.set_state("ended")  # updates state of the game
            return self._board
        # takes all seeds remaining in player 1's pits and adds them to player 1's store
        elif self.player_2_pits_sum() == 0:
            self._board[6] += self.player_1_pits_sum()
            for index in range(0, 6):
                self._board[index] = 0
            self.set_state("ended")  # updates state of the game
            return self._board
        else:
            return self._board

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
        """If game is ended and tied: returns "It's a tie".
        If game is ended and isn't tied: returns "Winner is player 1(or 2, based on actual winner): player's name".
        If game is not ended yet, returns "Game has not ended"."""

        if self.get_state() == "ended":
            # stores number of seeds in each player's store in a variable for easy comparison
            player_1_seeds = self.get_player_1_store()
            player_2_seeds = self.get_player_2_store()
            if player_1_seeds == player_2_seeds:
                return "It's a tie"
            elif player_1_seeds > player_2_seeds:
                return f"Winner is player 1: {self._players[0]}"
            elif player_2_seeds > player_1_seeds:
                return f"Winner is player 2: {self._players[1]}"
        else:
            return "Game has not ended"


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
    print(game.play_game(1, 1))
    print(game.play_game(1, 2))
    print(game.play_game(1, 3))
    print(game.play_game(1, 4))
    print(game.play_game(1, 5))
    print(game.play_game(1, 6))
    print(game.return_winner())


if __name__ == "__main__":
    main()
