def main():
    d ={
        'city':'Portland',
        'state': 'Oregon',
        'details': ['Cold', 'Snowy', 'Winter']
    }

    print(d['city'])
    print(d.get('country', 'USA'))

    w =  {
        "weather": {
            "description": "overcast clouds",
            "category": "Clouds"
        },
        "wind": {
            "speed": 1.28,
            "deg": 161
        },
        "units": "imperial",
        "forecast": {
            "temp": 49.28,
            "feels_like": 47.03,
            "pressure": 1031,
            "humidity": 80,
            "low": 46,
            "high": 51
        },
        "location": {
            "city": "Portland",
            "state": "OR",
            "country": "US"
        },
        "rate_limiting": {
            "unique_lookups_remaining": 49,
            "lookup_reset_window": "1 hour"
        }
    }
    print(w.get('forecast').get('temp'))

if __name__ == '__main__':
    main()