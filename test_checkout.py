from Checkout import Checkout
from ComboPricingRule import ComboPricing
from SpecialPricingRule import SpecialPricing
from UnitPricingRule import UnitPricing

RULES = [
    ComboPricing(required_items={'A': 1, 'B': 1, 'C': 1}, combo_price=80),  # Combo: A + B + C = $80
    SpecialPricing(sku='A', unit_price=50, special_quantity=3, special_price=130),  # 3A = $100
    SpecialPricing(sku='B', unit_price=30, special_quantity=2, special_price=45),  # 3A = $100
    UnitPricing(sku='C', unit_price=20),
    UnitPricing(sku='D', unit_price=15),
]

def price(goods: str) -> int:
    co = Checkout(RULES)
    for item in goods:
        co.scan(item)
    return co.total()

def test_totals():
    assert price("") == 0
    assert price("A") == 50
    assert price("AB") == 80

    # 2 * A = 100
    assert price("AA") == 100

    # 3A's = 130 special pricing
    assert price("AAA") == 130

    assert price("AAAA") == 180
    assert price("AAAAA") == 230
    assert price("AAAAAA") == 260
    assert price("AAAB") == 160
    assert price("AAABB") == 175

    # 3 A's for 130 + 2 B's for 45 + 1 D for 15 = 190
    assert price("AAABBD") == 190

    # Same as above in any variation of scanning the item
    assert price("DABABA") == 190

def test_special_pricing():
    # A B C = 100 special pricing
    assert price("ABCA") == 130
    assert price("AAABC") == 180

def test_incremental():
    co = Checkout(RULES)
    assert co.total() == 0
    co.scan("A")
    assert co.total() == 50
    co.scan("B")
    assert co.total() == 80
    co.scan("A")
    assert co.total() == 130
    co.scan("A")
    assert co.total() == 160
    co.scan("B")
    assert co.total() == 175