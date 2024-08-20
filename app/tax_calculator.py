from .stock_calculator import StockProcessCalculus
from .constant import TAXES_DEFAULT, RULE_TAX_TOTAL_PRICE, DECIMAL_PRECISION

class TaxProcessCalculus(StockProcessCalculus):
    """
    Proces each transaction and get tax value, Calculate a tax value for different rules in each transaction
    """
    def __init__(self):
        """
        build a new instance of StockProcessCalculus for get a profit value a calculate tax
        """
        super().__init__()
        self.tax = TAXES_DEFAULT
        self.rule_tax_total_price = RULE_TAX_TOTAL_PRICE

    def sell_price_lower(self, operation_data: dict) -> bool:
        """
        Returns true is the price sell is lower than last buy value
        Args:
            operation_data dict: information about operation {"operation":"buy", "unit-cost":10.00, "quantity": 10}

        Returns:
            true if you need pay tax or not
        """
        price = operation_data.get("unit-cost")

        if price < self.list_cost_stock[-1]:
            self.total_losses += self.losses_transaction(operation_data)
            return True

        return False

    def sell_total_price(self, operation_data: dict) -> bool:
        """
        Returns true is the total price for sale stock is lower than an specific value
        Args:
            operation_data: information about operation {"operation":"buy", "unit-cost":10.00, "quantity": 10}

        Returns:

        """
        quantity = operation_data.get("quantity")
        price = operation_data.get("unit-cost")

        if quantity * price <= self.rule_tax_total_price:
            return True

        return False

    def taxes_sell_transaction(self, overall_profit: int) -> float:
        """
        Calculate the tax for each sell transaction
        Args:
            overall_profit float: value of overall profit

        Returns float:
            tax
        """
        return round(overall_profit*(self.tax), DECIMAL_PRECISION)

    def taxes_buy_transaction(self) -> float:
        """
              Calculate the tax for each buy transaction
              Args:
                  overall_profit float: value of overall profit

              Returns float:
                  tax
              """
        return 0

    def get_values_taxes(self, tax_profit: float) -> dict:
        """
        Get values for each stock transaction
        Returns dict:   return a general information for each stock transaction with tax value

        """
        return {
            **self.get_values(),
            'tax': round(tax_profit , DECIMAL_PRECISION),
        }