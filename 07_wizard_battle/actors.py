import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f'Creature {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)


    def attack(self, creature):
        print(f'The wizard {self.name} attacks {creature.name}')

       # my_roll = random.randint(1, 12) * self.level
        my_roll = self.get_defensive_roll()
       # creature_roll = random.randint(1, 12) * creature.level
        creature_roll = creature.get_defensive_roll()
        print(f'You roll {my_roll}')
        print(f' {creature.name} rolls {creature_roll}')

        if my_roll >=creature_roll:
            print(f'The wizard has handily triumphed over {creature.name}')
            return True
        else:
            print('The wizard has been DEFEATED!')
            return False


class SmallAnimal(Creature):
    pass