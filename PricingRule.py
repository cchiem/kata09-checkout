from abc import ABC,abstractmethod

class PricingRule(ABC):
    @abstractmethod
    def calculate_pricing(self, quantity):
        pass