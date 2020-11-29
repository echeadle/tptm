class Purchase:
    def __init__(
        self, street, city, zip, state, beds,
        baths, sq__ft, home_type, sale_date, price,
        latitude, longitude):
        self.longitude  = longitude
        self.latitude  = latitude
        self.price = price
        self.sale_date = sale_date
        self.home_type = home_type
        self.sq_ft = sq__ft 
        self.baths = baths 
        self.beds = beds 
        self.state = state
        self.zip = zip
        self.city = city
        self.street = street 
