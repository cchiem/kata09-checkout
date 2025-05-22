from math import remainder

from PricingRule import PricingRule


class SpecialPricingRule(PricingRule):
    def __init__(self, unit_price, special_quantity, special_price):
         self.unit_price = unit_price
         self.special_quantity = special_quantity
         self.special_price = special_price

    def calculate_pricing(self, quantity):
        full_sets = quantity // self.special_quantity # 5 // 3 = 1 * special price applys to 1 set
        remaining = quantity % self.special_quantity # 5 % 3 = 2 * unitprice applys to the remaining 2 items

        return self.special_price * full_sets + self.unit_price * remaining
