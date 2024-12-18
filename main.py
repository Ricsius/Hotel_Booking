import pandas as pd

HOTELS_PATH = "hotels.csv"
CARDS_PATH = "cards.csv"
CARDS_SECURITY_PATH = "card_security.csv"
DF = pd.read_csv(HOTELS_PATH, dtype={"id": str})
DF_CARDS = pd.read_csv(CARDS_PATH, dtype=str).to_dict(orient="records")
DF_CARDS_SECURITY = pd.read_csv(CARDS_SECURITY_PATH, dtype=str)

class Hotel:
    def id_exists(hotel_id):
        found_hotel = DF.loc[DF["id"] == hotel_id]

        return len(found_hotel) == 1

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = DF.loc[DF["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        DF.loc[DF["id"] == self.hotel_id, "available"] = "no"

        DF.to_csv(HOTELS_PATH, index=False)
    
    def available(self):
        availability = DF.loc[DF["id"] == self.hotel_id, "available"].squeeze()

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

class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, 
                     "holder": holder, "cvc": cvc}
        
        return card_data in DF_CARDS
    
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = DF_CARDS_SECURITY.loc[DF_CARDS_SECURITY["number"] == self.number, "password"].squeeze()

        return password == given_password

print(DF)

hotel_id_exists = False

while not hotel_id_exists:
    hotel_id = input("Enter the id of the hotel: ")
    hotel_id_exists = Hotel.id_exists(hotel_id)

    if not hotel_id_exists:
        print("The hotel does not exist.")


hotel = Hotel(hotel_id)

if hotel.available():
    card_number = input("Enter your credit card number: ")
    creadit_card = SecureCreditCard(number=card_number)
    expiration = input("Enter your credit card expiration date (mm/dd): ")
    holder_name = input("Enter your credit card holder name: ")
    cvc_code = input("Enter your credit card cvc code: ")

    if creadit_card.validate(expiration=expiration, holder=holder_name, cvc=cvc_code):
        card_password = input("Enter your credit card authentication password: ")

        if creadit_card.authenticate(given_password=card_password):
            hotel.book()

            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            ticket = reservation_ticket.generate()
    
            print(ticket)
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment.")
else:
    print("Hotel is not free.")