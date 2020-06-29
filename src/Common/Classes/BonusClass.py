class WrongBonusException(Exception):
    """Raised set bonus is more than 1 or lower than 0"""
    pass


class Bonus:
    def __init__(self, upper: int = 1, lower: int = -1):
        self.upper = upper
        self.lower = lower
        self.value = 0

    def set_value(self, value: float):
        if self.upper >= value >= self.lower:
            self.value = value
        else:
            raise WrongBonusException()

    def set_upper(self, upper: int):
        self.upper = upper

    def set_lower(self, lower: int):
        self.lower = lower
