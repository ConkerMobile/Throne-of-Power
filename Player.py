import random
class Player():
    def __init__(self):
        Possible_Moves = ["Punch", "Sword Slice", "Knife Swing", "Thundering Earthquake","Hypnosis","Electric Bolt","Nuclear Hit", "Lightsaber Stab"]
        Move_damage = {"Punch":70, "Sword Slice":80, "Knife Swing": 100, "Thundering Earthquake":150,"Hypnosis":200,"Electric Bolt":170,"Nuclear Hit": 180, "Lightsaber Stab": 200}
        self.health = 500
        self.moves = []
        self.damage = 0
        for i in range(2):
            self.moves.append(random.choice(Possible_Moves))
            self.damage
        