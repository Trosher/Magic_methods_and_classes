from collections import Counter

class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
        self.check = {"11": [2, 2], "01": [3, -1], \
                      "10": [-1, 3], "00": [0, 0]}

    def play(self, player1, player2):
        if not issubclass(type(player1), type(Player())) \
        or not issubclass(type(player2), type(Player())):
            print("the game can only be played with objects inherited from the player class")
        elif self.matches == 0:
            print("The number of matches for a game cannot be equal to 0")
        else:
            for round_ in range(1, self.matches+1):
                actionFirstPlayer = player1.ActionSelection(round_)
                actionSecondPlayer = player2.ActionSelection(round_)
                player1.lastEnemyAction = actionSecondPlayer
                player2.lastEnemyAction = actionFirstPlayer
                self.registry[str(player1)] += self.check[str(int(actionFirstPlayer)) + str(int(actionSecondPlayer))][0]
                self.registry[str(player2)] += self.check[str(int(actionFirstPlayer)) + str(int(actionSecondPlayer))][1]               

    def top3(self):
        topList = list(self.registry.most_common(3))
        for top in topList:
            print(top[0], str(top[1]))


class Player(object):
    def __init__(self):
        self.name = "Player"
        self.lastEnemyAction = True
        
    def __str__(self):
        return self.name
    
    def __eq__(self, other: str):
        return self.name == other
    
class Cheater(Player):
    def __init__(self):
        self.name = "Cheater"
        self.lastEnemyAction = True
    
    def ActionSelection(self, round):
        return False
    
class Cooperator(Player):
    def __init__(self):
        self.name = "Cooperator"
        self.lastEnemyAction = True
    
    def ActionSelection(self, round):
        return True
    
class Copycat(Player):
    def __init__(self):
        self.name = "Copycat"
        self.lastEnemyAction = True
        
    def ActionSelection(self, round):
        res = True
        if (round != 1):
            res = self.lastEnemyAction
        return res
    
class Grudger(Player):
    def __init__(self):
        self.name = "Grudger"
        self.cheatEnemy = False
        self.lastEnemyAction = True
        
    def ActionSelection(self, round):
        res = False
        if round != 0 and not self.lastEnemyAction:
            self.cheatEnemy = True
        elif round == 0 or not self.cheatEnemy:
            self.cheatEnemy = False
            res = True
        
        return res
    
class Detective(Player):
    def __init__(self):
        self.name = "Detective"
        self.cheatEnemy = False
        self.dictToFirstForRound = {1:True, 2:False,
                                    3:True, 4:True}
        self.lastEnemyAction = True
       
    def ActionSelection(self, round):
        res = False
        if round == 0:
            self.cheatEnemy = False
        if round <= 4:
            res = self.dictToFirstForRound[round]
            if not self.lastEnemyAction:
                self.cheatEnemy = True
        elif self.cheatEnemy:
            res = self.lastEnemyAction
        return res
 
def main():
    game = Game(10)
    players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective()]
    numberForPlayer2 = 0;
    for player1 in players[:len(players) - 1]:
        for player2 in players[numberForPlayer2:]:
            game.play(player1, player2)
        numberForPlayer2 += 1
    game.top3()
            

if __name__ == "__main__":
    main()
            