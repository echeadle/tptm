import collections

Location = collections.namedtuple('Location', 'city state country')


def main():
    # Show the header
    show_header()

    # Get the location request
    location_text  = input('Where do you want the weather report (e.g. Salt Lake, US? ')
    print(f'You selcted {location_text}')

    # Convert plaintext over to data we can use
    loc = convert_plaintext_location(location_text)

    print(loc)

    # Get report from the API.
    data = call_weather_api()
    # Report the weather


def convert_plaintext_location(location_text):
    """
    Convert user input to location API can use

    :param location_text: City (required), State (optional), Country (optional)
    """
    if not location_text or not location_text.strip():
        return None

    location_text = location_text.lower().strip()
    parts = location_text.split(',')

    city = ""
    state = ""
    country = "us"
    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country == parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()
        country = parts[2].strip()
    else:
        return None

    # print(f'City={city}, State={state}, Country={country}')
    # loc = city, state, country

    return Location(city, state, country)


def show_header():
    print('-' * 40)
    print('           WEATHER CLIENT')
    print('-' * 40)
    print()

if __name__ == '__main__':
    main()