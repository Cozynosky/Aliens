from Aliens.Ship.first_ship import FirstShip


class Profile:
    def __init__(self, name="Empty"):
        self.name = name
        self.currency = 0
        self.ship = FirstShip()
