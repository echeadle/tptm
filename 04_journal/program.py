def print_header():
    print('-' * 40)
    print('           JOURNAL APP')
    print('-' * 40)
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_data = []


    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif  cmd != 'x':
            print(f"Sorry we don't understand '{cmd}'")

    print('Done, goodbye.')


def list_entries(data):
    print(data)


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    data.append(text)

def main():
    print_header()
    run_event_loop()


main()