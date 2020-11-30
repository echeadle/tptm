import movie_svc


def main():
    print_header()
    search_event_loop()


def print_header():
    """
    Simple Show header method
    :params: None
    """
    print('-' * 40)
    print('        MOVIE SEARCH APP')
    print('-' * 40)
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        search = input('Movie search text (x to exit): ')
        if search != 'x':
            results = movie_svc.find_movies(search)
            print("Found {} results.".format(len(results)))
            for r in results:
                print('{} -- {}'.format(
                    r.year, r.title
                ))
            print()
            
    print('exiting...')

if __name__ == '__main__':
    main()
