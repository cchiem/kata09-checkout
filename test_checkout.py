import pytest
from Checkout import Checkout
from ComboPricingRule import ComboPricing
from SpecialPricingRule import SpecialPricing
from UnitPricingRule import UnitPricing


@pytest.fixture
def rules():
    return [
        ComboPricing(required_items={'A': 1, 'B': 1, 'C': 1}, combo_price=80),  # Combo: A + B + C = $80
        SpecialPricing(sku='A', unit_price=50, special_quantity=3, special_price=130),  # 3A = $130
        SpecialPricing(sku='B', unit_price=30, special_quantity=2, special_price=45),  # 2B = $45
        UnitPricing(sku='C', unit_price=20),
        UnitPricing(sku='D', unit_price=15),
    ]


def price(goods: str, rules) -> int:
    co = Checkout(rules)
    for item in goods:
        co.scan(item)
    return co.total()


# ------------------------------------------
# PARAMETERIZED TOTAL TESTS
# ------------------------------------------

@pytest.mark.parametrize("items, expected", [
    ("", 0),
    ("A", 50),
    ("AB", 80),
    ("AA", 100),
    ("AAA", 130),              # Special pricing applies
    ("AAAA", 180),
    ("AAAAA", 230),
    ("AAAAAA", 260),           # Two specials
    ("AAAB", 160),
    ("AAABB", 175),            # 3A special + 2B special
    ("AAABBD", 190),           # + D unit
    ("DABABA", 190),           # Same total in any scan variation
])
def test_pricing_combinations(items, expected, rules):
    assert price(items, rules) == expected


# ------------------------------------------
# UNIT PRICING
# ------------------------------------------

@pytest.mark.parametrize("items, expected", [
    ("C", 20),
    ("D", 15),
    ("CCCC", 80),
    ("DDDD", 60),
])
def test_unit_prices(items, expected, rules):
    assert price(items, rules) == expected


# ------------------------------------------
# SPECIAL PRICING
# ------------------------------------------

def test_special_applies_then_unit(rules):
    assert price("AAAA", rules) == 180     # 130 + 50
    assert price("AABCAA", rules) == 210   # 130(A) + 80(combo)


# ------------------------------------------
# COMBO PRICING
# ------------------------------------------

def test_combo_applies_once(rules):
    assert price("ABC", rules) == 80


def test_combo_applies_then_unit(rules):
    assert price("ABCA", rules) == 130     # 80 combo + 50 extra A


# ------------------------------------------
# INCREMENTAL SCANS
# ------------------------------------------

def test_incremental_total(rules):
    co = Checkout(rules)
    assert co.total() == 0
    co.scan("A")
    assert co.total() == 50
    co.scan("B")
    assert co.total() == 80                # Combo formed
    co.scan("A")
    assert co.total() == 130               # 1A leftover, 2A = 100, 1B = 30
    co.scan("A")
    assert co.total() == 160               # 3A = 130 + 30(B)
    co.scan("B")
    assert co.total() == 175               # 3A = 130 + 2B = 45


# ------------------------------------------
# EDGE CASES
# ------------------------------------------

def test_combo_extra_items(rules):
    assert price("AABCBC", rules) == 160
    # 2 combos of ABC = 160
