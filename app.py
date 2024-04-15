import random
import time

class Coin:
    def __init__(self):
        self.__side = [0,1]
    
    def flip(self):
        return random.choice(self.__side)
    
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def flip_coin(self):
        coin = Coin()
        return coin.flip()

class Game:
    def __init__(self, players):
        self.__winners = []
        self.__players = players
        self.__round = 0
        self.__coin_side = ["Tails", "Heads"]
        self.__symbol = ["x", "ok"]
    
    def set_next_round(self):
        self.__round += 1
        return

    def get_players(self):
        return [player.get_name() for player in self.__players]

    def get_winners_count(self):
        return len(self.__winners)

    def get_winners(self):
        return [winner.get_name() for winner in self.__winners]

    def get_round(self, flip_result):
        return self.__round

    def get_heads_tails(self, flip_result):
        return self.__coin_side[flip_result]

    def get_symbol(self, flip_result):
        return self.__symbol[flip_result]

    def play_game(self):

        while True:

            winners_count = self.get_winners_count()

            if self.__round == 0: # start first match round
                print("### Welcome To Coin Flip Game ###")
                print(f"Joined Players: {len(self.get_players())} \n")

                self.set_next_round()
                print(f"\n### Round: {self.__round} ###\n")

                self.match_round()
                print(f"\n=> Round {self.__round} Winners [ {self.get_winners_count()} ]: {self.get_winners()} \n")

            elif self.get_winners_count() == 1: # end game
                print(f"!!! Winner Found: {self.get_winners()} !!!")
                break

            else: # players for next round is winners of previous round
                self.__players = self.__winners
                
                self.set_next_round()
                print(f"\n### Round: {self.__round} ###\n")
                
                self.match_round()

                print(f"\n=> Round {self.__round} Winners [ {self.get_winners_count()} ]: {self.get_winners()} \n")

        time.sleep(1)

        return
    
    def match_round(self):
        self.__winners = [] # reset winners

        players = self.__players

        print("\n[ Symbol: Flip Result ] Player Name \n")

        for player in players: # every player flips
            
            flip_result = player.flip_coin()
            
            print(f"[ {self.get_symbol(flip_result)}: {self.get_heads_tails(flip_result)} ]  {player.get_name()}")
            
            if flip_result: # player with flip_result = 1 is winner
                self.__winners.append(player)

            time.sleep(1)
        
        if not self.get_winners_count(): # replay match_round if no winner found in current round
            self.match_round()

        print("\n")

        return

player_names = [
    "Armani Boyles",
    "Deshaun Betz",
    "Kolby Stacy",
    "Lucille Richards",
    "Bruce Crutchfield",
    "Charles Hamlin",
    "Henry Forrester",
    "Lola Jimenez",
    "Jayda Reilly",
    "Ximena Rivas",
    "Maya Newton",
    "Tamara Steward",
    "Tionne Crouch",
    "Darby Walter",
    "Johnson Rushing",
    "Austen Banks",
    "Zakary Roberson",
    "Roy Templeton",
    "Litzy Leonard",
    "Jeniffer Boswell",
    "Karleigh Miles",
    "Daron Dent",
    "Bernard Raines",
    "Molly Gibbs",
    "Giancarlo Denton",
    "Gavin Mortensen",
    "Catrina Dayton",
    "Regan Bittner",
    "Alexandre Anderson",
    "Alex Grier",
]

players = [Person(player) for player in player_names]
game = Game(players)

game.play_game()