import pandas as pd

HOTELS_PATH = "hotels.csv"

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"

        df.to_csv(HOTELS_PATH, index=False)
    
    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        return availability == "yes"

class ReservationTicket:
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """

        return content

df = pd.read_csv(HOTELS_PATH, dtype={"id": str})

print(df)

hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()

    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    ticket = reservation_ticket.generate()
    
    print(ticket)
else:
    print("Hotel is not free.")