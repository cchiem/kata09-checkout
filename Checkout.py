class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.scanned_items = {}

    def scan(self, item):
        self.scanned_items[item] = self.scanned_items.get(item, 0) + 1

    def total(self):
        total = 0
        for item, quantity in self.scanned_items.items():
            pricing_rule = self.pricing_rules[item]
            total += pricing_rule.calculate_pricing()
        return total


