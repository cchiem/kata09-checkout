from PricingRule import PricingRule


class SpecialPricing(PricingRule):
    def __init__(self, sku: str, unit_price: int, special_quantity: int, special_price: int):
        self.sku = sku
        self.unit_price = unit_price
        self.special_quantity = special_quantity
        self.special_price = special_price

    def apply(self, item_counts):
        count = item_counts.get(self.sku, 0)
        special_sets = count // self.special_quantity
        remainder = count % self.special_quantity

        total = (special_sets * self.special_price) + (remainder * self.unit_price)

        item_counts[self.sku] = 0  # counted items removed
        return total, item_counts