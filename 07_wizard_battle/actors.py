class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level


    def attack(self, creature):
        print(f'The wizard {self.name} attacks {creature.name}')
        
class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f'Creature {self.name} of level {self.level}'