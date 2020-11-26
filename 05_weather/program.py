def main():
    # Show the header
    show_header()

    # Get the location request
    location_text  = input('Where do you want the weather report (e.g. Salt Lake, US? ')
    print(f'You selcted {location_text}')

    # Convert plaintext over to data we can use
    location = convert_plaintext_location(location_text)
    print(f'Location = {location}')

    # Get report from the API.
    # Report the weather
    
def convert_plaintext_location(location_text):
    """
    Convert user input to location API can use
    :param location_text: City (required), State (optional), Country (optional)
    """
    pass

def show_header():
    print('-' * 40)
    print('           WEATHER CLIENT')
    print('-' * 40)
    print()

if __name__ == '__main__':
    main()