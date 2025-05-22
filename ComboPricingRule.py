from PricingRule import PricingRule


class ComboPricing(PricingRule):
    def __init__(self, required_items, combo_price):
        # required_items: dict of required SKUs and their quantities, e.g., {'A': 1, 'B': 1, 'C': 1}
        # combo_price: total price for the combo
        self.required_items = required_items
        self.combo_price = combo_price

    def apply(self, item_counts):
        # How many complete sets of the combo can we form
        sets_possible = min(item_counts[item] // qty for item, qty in self.required_items.items())
        total = sets_possible * self.combo_price

        # Subtract used items
        for item, qty in self.required_items.items():
            item_counts[item] -= sets_possible * qty

        return total, item_counts
