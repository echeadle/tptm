from actors import Wizard, Creature
import random
import time

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
        Creature('Evil Wizard', 100)
    ]

    hero = Wizard('Gandolf', 75)

    # print(creatures)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...')
        print()
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd =='r':
            print('The wizard has become unsure of his power and flees!!!!')
        elif cmd == "l":
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print('Ok, exiting game.... bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done")
            break
        print()


if __name__ == "__main__":
    main()