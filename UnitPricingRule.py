from PricingRule import PricingRule


class UnitPricing(PricingRule):
    def __init__(self, sku: str, unit_price: int):
        self.sku = sku
        self.unit_price = unit_price

    def apply(self, item_counts):
        count = item_counts.get(self.sku, 0)
        total = count * self.unit_price
        item_counts[self.sku] = 0 # counted items removed
        return total, item_counts
