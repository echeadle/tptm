def print_header():
    print('-' * 40)
    print('           JOURNAL APP')
    print('-' * 40)
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')

        if cmd == 'L':
            print('L')

        elif cmd == 'A':
            print('A')

    print('Done, goodbye.')


def main():
    print_header()
    run_event_loop()


main()