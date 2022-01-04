

class Upgrade:
    max_level = NotImplemented

    def __init__(self):
        pass

    @staticmethod
    def get_cost(level):
        raise NotImplementedError

    @staticmethod
    def get_value(level):
        raise NotImplementedError

    @staticmethod
    def is_max(self, level):
        return level == self.max_level


class ShipSpeed(Upgrade):
    max_level = 50

    def __init__(self):
        super(ShipSpeed, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 1.82048 * level ** 1.1668 + 3.24627
        return round(cost)

    @staticmethod
    def get_value(level):
        value = 0.0662882 * level ** 1.15149 + 3.99239
        return round(value, 2)


class BulletSpeed(Upgrade):
    max_level = 50

    def __init__(self):
        super(BulletSpeed, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 1.82048 * level ** 1.1668 + 3.24627
        return round(cost)

    @staticmethod
    def get_value(level):
        value = 0.143538 * level ** 1.25424 + 4.62921
        return round(value, 2)


class BulletDamage(Upgrade):
    max_level = None

    def __init__(self):
        super(BulletDamage, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 0.451257 * level ** 1.95251 + 9.54874
        return round(cost)

    @staticmethod
    def get_value(level):
        value = 0.407461 * level ** 1.30038 + 4.12692
        return round(value, 2)


class BulletsInShot(Upgrade):
    max_level = 9

    def __init__(self):
        super(BulletsInShot, self).__init__()

    @staticmethod
    def get_cost(level):
        costs = [100, 500, 1000, 2500, 5000, 10000, 15000, 30000]
        return costs[level-1]

    @staticmethod
    def get_value(level):
        return level


class HealthCapacity(Upgrade):
    max_level = None

    def __init__(self):
        super(HealthCapacity, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 0.451257 * level ** 1.95251 + 9.54874
        return round(cost)

    @staticmethod
    def get_value(level):
        value = 0.74265 * level ** 1.52678 + 8.41349
        return round(value, 2)


class Lives(Upgrade):
    max_level = 99

    def __init__(self):
        super(Lives, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 62.5 * level - 12.5
        return round(cost)

    @staticmethod
    def get_value(level):
        return level


class MagazineSize(Upgrade):
    max_level = 97

    def __init__(self):
        super(MagazineSize, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 62.5 * level - 12.5
        return round(cost)

    @staticmethod
    def get_value(level):
        return level + 2


class ReloadTime(Upgrade):
    max_level = 50

    def __init__(self):
        super(ReloadTime, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 1.82048 * level ** 1.1668 + 3.24627
        return round(cost)

    @staticmethod
    def get_value(level):
        value = 3.15807 - 0.158066 * level ** 0.668186
        return round(value, 2)


class DropRate(Upgrade):
    max_level = 50

    def __init__(self):
        super(DropRate, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 1.82048 * level ** 1.1668 + 3.24627
        return round(cost)

    @staticmethod
    def get_value(level):
        value = 0.000226774 * level ** 2 + 0.00264101 * level + 0.299937
        return value


class CoinValue(Upgrade):
    max_level = None

    def __init__(self):
        super(CoinValue, self).__init__()

    @staticmethod
    def get_cost(level):
        cost = 40.6279 * level ** 2.58859 + 24.2367
        return round(cost)

    @staticmethod
    def get_value(level):
        return level
