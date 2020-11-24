def print_header():
    print('-' * 40)
    print('           JOURNAL APP')
    print('-' * 40)
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None

    while cmd.lower().strip() != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            print('L')
        elif  == 'a':
            print('A')
        elif  != 'x':
            print(f"Sorry we don't understand '{cmd}'")
    print('Done, goodbye.')


def main():
    print_header()
    run_event_loop()


main()