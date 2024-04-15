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

players = ["henry", "robert", "john", "Jane", "thor"]


class Game:
    def __init__(self, players):
        self.__winners = []
        self.__players = players
        self.__round = 0
        self.__coin_side = ["Tails", "Heads"]
        self.__result_symbol = ["x ", "ok "]

    def start(self):
        if not len(self.__winners):
            self.__winners = self.__players
       
        print("### Welcome To Coin Flip Game ###")
        print(f"Joined Players: {self.get_winners()} \n")

        while len(self.__winners) > 1:

            self.__round += 1

            if len(self.__winners) > 1:
                self.__players = self.__winners
            
            print(f"### Round: {self.__round} ###")
            self.match_play()
            print(f"Round {self.__round} Winners: {self.get_winners()} \n")
            time.sleep(1)
        
        print(f"!!! Winner Found: {[winner.get_name() for winner in self.__winners]} !!!")


    def match_play(self):
        self.__winners = []
        print("Player-Name: Flip-Result")
        while True:
            for player in self.__players:
                flip_result = player.flip_coin()
                print(f"{self.__result_symbol[flip_result]} {player.get_name()}: {self.__coin_side[flip_result]}")
                if flip_result:
                    self.__winners.append(player)
                time.sleep(1)

            if len(self.__winners) > 0:
                break
            else:
                continue

    def get_winners(self):
        return [winner.get_name() for winner in self.__winners]

  
player_names = [
    "Elian Koch",
    "Martina Barclay",
    "Josh Menard",
    "Bryce Wertz",
    "Ameer Merrick",
    "Elsie Adair",
    "Lorenzo Patton",
    "Laisha Schroeder",
    "Geovanni Mosier",
    "Ryland Hernandez",
    "Jayden Witt",
    "Garret Cooke",
    "Tyanna Gonzales",
    "Marshall Kinsey",
    "Sydni Leahy",
    "Helena Faust",
    "Anastasia Heredia",
    "Jaela Slater",
    "Nicolle Cody",
    "Lyric Limon",
]

players = [Person(player) for player in player_names]
game = Game(players)

game.start()