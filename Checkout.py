from collections import Counter

class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.scanned_items = Counter()

    def scan(self, sku: str):
        self.scanned_items[sku] += 1

    def total(self) -> int:
        total_price = 0
        items = self.scanned_items.copy()

        for rule in self.pricing_rules:
            price, items = rule.apply(items)
            total_price += price

        return total_price
