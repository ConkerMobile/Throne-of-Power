import random
import Dragon
class Player():
    def __init__(self, name,wins=0,health=500,moves = [], damage = {}, max_damage = 0):
        Possible_Moves = ["Punch", "Sword Slice", "Knife Swing", "Earthquake","Hypnosis","Electric Bolt","Nuclear Hit", "Lightsaber Stab"]
        Move_damage = {"Punch":70, "Sword Slice":80, "Knife Swing": 100, "Earthquake":150,"Hypnosis":200,"Electric Bolt":170,"Nuclear Hit": 180, "Lightsaber Stab": 200}
        self.wins = 0
        self.health = 500
        self.battle_health = self.health
        self.moves = []
        self.damage = {}
        self.max_damage = 0
        self.name = name
        
        for i in range(2):
            choice = random.choice(Possible_Moves)
            self.moves.append(choice)
            self.max_damage+=Move_damage[choice]
            self.damage[choice] = Move_damage[choice]
    def upgrade(self):
        upgraded = False
        """Upgrades health and damage when you have a certain amount of wins"""
        if (self.wins >= 3 and self.wins < 5):
            self.health = 600
            upgraded = True
        elif (self.wins >= 5 and self.wins < 7):
            self.health = 900
            upgraded = True
        elif (self.wins >= 7 and self.wins < 10):
            self.health = 1100
            upgraded = True
        elif (self.wins >= 10):
            self.health = 1300
            upgraded = True
        self.battle_health = self.health
        if upgraded == True:
            for i in self.moves:
                self.damage[i]+=50
            self.max_damage +=100