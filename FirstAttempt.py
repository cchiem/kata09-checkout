class CheckOut:
    def init(self, rules):
        self.rules = rules
        self.checkoutItems = {}

    def scan(self, item):
        self.checkoutItems[item] = self.checkoutItems.get(item, 0) + 1

    def total(self):
        total = 0
        for item, quantity in self.checkoutItems.items():
            rule = self.rules[item] # Rule for the item
            unit_price = rule["unitprice"]  # Unit Price for the item

            # Check for a special price
            if "special" in rule:
                special_qty = rule["special"]["quantity"] # Check for a special quantity
                special_price = rule["special"]["specialPrice"] # Check for a special Price

                items_on_special = quantity // special_qty
                remainder = quantity % special_qty

                total += items_on_special * special_price + remainder * unit_price
            else:
                total += quantity * unit_price
        return total


checkout_items = {"A": 2, "B":1}
RULES = {
    "A" : {"unitprice": 50, "special": {"quantity": 3, "specialPrice": 130 }},
    "B" : {"unitprice": 30, "special": {"quantity": 2, "specialPrice": 45 }},
    "C" : {"unitprice": 20},
    "D" : {"unitprice": 15},
}