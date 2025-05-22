from PricingRule import PricingRule


class UnitPricing(PricingRule):
    def __init__(self, unit_price):
        self.unit_price = unit_price

    def calculate_pricing(self, quantity):
        return self.unit_price * quantity