from abc import ABC, abstractmethod
from collections import Counter

class PricingRule(ABC):
    @abstractmethod
    def apply(self, item_counts):
        """
        Apply this pricing rule to related items.

        Returns:
            Tuple of (price_to_add, remaining_item_counts)
        """
        pass