from user import User


class RideOffer:
    def __init__(self, driver, origin, destination, contribution, seats,
                 date, time, recurring=False, days=None, notes=""):
        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.contribution = contribution
        self.seats = seats
        self.date = date
        self.time = time
        self.recurring = recurring
        self.days = days or []
        self.notes = notes


class RideRequest:
    def __init__(self, rider, origin, destination, contribution,
                 date, time, recurring=False, days=None, notes=""):
        self.rider = rider
        self.origin = origin
        self.destination = destination
        self.contribution = contribution
        self.date = date
        self.time = time
        self.recurring = recurring
        self.days = days or []
        self.notes = notes


class RideProcessor:
    def __init__(self):
        self.offers = []
        self.requests = []

    def submit_offer(self, offer):
        self.offers.append(offer)

    def submit_request(self, request):
        self.requests.append(request)

    def get_offers(self):
        return self.offers

    def get_requests(self):
        return self.requests
