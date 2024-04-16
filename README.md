
# Flip Coin

Players compete with their luck for winning the game.
## Screenshots

![Screenshot from 2024-04-15 22-26-13](https://github.com/seejn/flip-coin/assets/52706007/def80458-4d77-480f-8139-7c2c85c0baa9)


## Installation
Requirement: python

```
git clone https://github.com/seejn/flip-coin.git
```
```
cd flip-coin
```
```
python app.py
```

## Initialization of Game
winners = []
players
coin_side = ["Tails", "Heads"]
sym = ["x", "ok"]
round = 0

## Process
1) play_game()
    criteria:
        a) round == 0 -> match_round()
        b) len(winners) == 1 -> end_game()
        c) len(winners) > 1 -> players = winners -> match_round()

2) match_round()
    criteria:
        a) empty winners
        b) every player flips if "heads" this player append to winners
        c) if every player flip "tails" replay match_round()

3) play_game() until single winner

## Credit

https://www.youtube.com/shorts/iEwvKcuwstk
