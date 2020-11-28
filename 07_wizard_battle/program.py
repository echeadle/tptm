from actors import Wizard, Creature
import random

def main():
    print_header()
    game_loop()

def print_header():
    print('-' * 40)
    print('           WIZARD GAME APP')
    print('-' * 40)
    print()

def game_loop():

    creatures=[
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 5),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    # print(creatures)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...')
        print()
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            print('attack')
        elif cmd =='r':
            print('runnaway')
        elif cmd == "l":
            print('look around')
        else:
            print('Ok, exiting game.... bye!')
            break

if __name__ == "__main__":
    main()