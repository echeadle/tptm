class Purchase:
    def __init__(
        self, street, city, zip, state, beds,
        baths, sq__ft, home_type, sale_date, price,
        latitude, longitude):
        self.longitude  = longitude
        self.latitude  = latitude
        self.price = price
        self.sale_date = sale_date
        self.type = home_type
        self.sq_ft = sq__ft 
        self.baths = baths 
        self.beds = beds 
        self.state = state
        self.zip = zip
        self.city = city
        self.street = street 



def create_from_dict(self, lookup):
        float(lookup['longitude'])
        float(lookup['latitude'])
        float(lookup['price'])
        lookup['sale_date']
        lookup['type']
        int(lookup['sq_ft'])
        int(lookup['baths'])
        int(lookup['beds'])
        lookup['state']
        lookup['zip']
        lookup['city']
        lookup['street']