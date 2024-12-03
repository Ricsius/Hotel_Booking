import pandas as pd

HOTELS_PATH = "hotels.csv"

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"

        df.to_csv(HOTELS_PATH, index=False)
    
    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        return availability == "yes"

class ReservationTicket:
    def __init__(self, customer_name, hotel):
        pass

    def generate(self):
        content = f""

        return content

df = pd.read_csv(HOTELS_PATH, dtype={"id": str})

hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()

    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")