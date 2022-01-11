

class Upgrade:
    max_level = None

    def __init__(self):
        self.level = 1

    def get_cost(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

    def is_max(self):
        return self.level == self.max_level

    def get_level(self):
        return self.level

    def upgrade_bought(self):
        self.level += 1


class ShipSpeed(Upgrade):
    max_level = 50

    def __init__(self):
        super(ShipSpeed, self).__init__()

    def get_cost(self):
        cost = 0.656227 * self.level ** 1.1709 + 0.696481
        return round(cost)

    def get_value(self):
        value = 0.0662882 * self.level ** 1.15149 + 3.99239
        return round(value, 2)


class BulletSpeed(Upgrade):
    max_level = 50

    def __init__(self):
        super(BulletSpeed, self).__init__()

    def get_cost(self):
        cost = 0.656227 * self.level ** 1.1709 + 0.696481
        return round(cost)

    def get_value(self):
        value = 0.143538 * self.level ** 1.25424 + 4.62921
        return round(value, 2)


class BulletDamage(Upgrade):

    def __init__(self):
        super(BulletDamage, self).__init__()

    def get_cost(self):
        cost = 0.656227 * self.level ** 1.1709 + 0.696481
        return round(cost)

    def get_value(self):
        value = 0.814922 * self.level ** 1.30038 + 8.25383
        return round(value, 2)


class BulletsInShot(Upgrade):
    max_level = 9

    def __init__(self):
        super(BulletsInShot, self).__init__()

    def get_cost(self):
        costs = [10, 25, 60, 100, 150, 210, 300, 500]
        return costs[self.level-1]

    def get_value(self):
        return self.level


class HealthCapacity(Upgrade):

    def __init__(self):
        super(HealthCapacity, self).__init__()

    def get_cost(self):
        cost = 0.656227 * self.level ** 1.1709 + 0.696481
        return round(cost)

    def get_value(self):
        value = 0.74265 * self.level ** 1.52678 + 8.41349
        return round(value, 2)


class Lives(Upgrade):
    max_level = 99

    def __init__(self):
        super(Lives, self).__init__()

    def get_cost(self):
        cost = 7.35757 * self.level ** 1.86217+2.91343
        return round(cost)

    def get_value(self):
        return self.level


class MagazineSize(Upgrade):
    max_level = 97

    def __init__(self):
        super(MagazineSize, self).__init__()

    def get_cost(self):
        cost = 0.656227 * self.level ** 1.1709 + 0.696481
        return round(cost)

    def get_value(self):
        return self.level + 2


class ReloadTime(Upgrade):
    max_level = 50

    def __init__(self):
        super(ReloadTime, self).__init__()

    def get_cost(self):
        cost = 0.656227 * self.level ** 1.1709 + 0.696481
        return round(cost)

    def get_value(self):
        value = 3.15807 - 0.158066 * self.level ** 0.668186
        return round(value, 2)


class DropRate(Upgrade):
    max_level = 71

    def __init__(self):
        super(DropRate, self).__init__()

    def get_cost(self):
        cost = 0.656227 * self.level ** 1.1709 + 0.696481
        return round(cost)

    def get_value(self):
        value = 0.01 * self.level+0.29
        return round(value, 2)


class CoinValue(Upgrade):

    def __init__(self):
        super(CoinValue, self).__init__()

    def get_cost(self):
        cost = 7.35757 * self.level ** 1.86217+2.91343
        return round(cost)

    def get_value(self):
        return self.level
