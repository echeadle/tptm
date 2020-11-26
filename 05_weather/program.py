def main():
    # Show the header
    show_header()
    # Get the location request
    location_text  = input('Where do you want the weather report (e.g. Salt Lake, US? ')
    print(f'You selcted {location_text}')
    # Convert plaintext over to data we can use
    # Get report from the API.
    # Report the weather
    

def show_header():
    print('-' * 40)
    print('           WEATHER CLIENT')
    print('-' * 40)
    print()

if __name__ == '__main__':
    main()