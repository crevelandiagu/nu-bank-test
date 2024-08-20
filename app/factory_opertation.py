from typing import Any


class StockOperationFactory:
    """
    Factory class to implement any stock transaction o operation like sell or buy.
    """

    @staticmethod
    def create_operation(operation_type) -> Any:
        """
        Select a diferent operation when you made a operation stock

        Args:
            operation_type str: the type of operation (buy or sell)

        Returns:
            Object Any: BuyOperationStock or SellOperationStock
        """
        if operation_type == "buy":
            return BuyOperationStock
        elif operation_type == "sell":
            return SellOperationStock
        else:
            raise ValueError("Invalid operation type")

class BuyOperationStock:
    """
    Execute calculus when you buy stock like calculate taxes or profit
    """
    def __init__(self, stock_process_calculus):
        self.calculator_stock_process = stock_process_calculus


    def get_operation_tax(self, operation_data: dict) -> dict[str, int]:
        """
        Calculate taxes when you buy stocks
        Args:
            operation_data dict: information about operation {"operation":"buy", "unit-cost":10.00, "quantity": 10}

        Returns:
            dictionary with all information about the operation like {"tax":0, ...}
        """
        stock_process = self.calculator_stock_process
        stock_process.track_operation(operation_type='buy', operation_data=operation_data)
        taxes = stock_process.taxes_buy_transaction()
        return stock_process.get_values_taxes(taxes)



class SellOperationStock:
    """
    Execute calculus when you sell stock like calculate taxes or profit
    """
    def __init__(self, stock_process_calculus):
        self.calculator_stock_process = stock_process_calculus

    def get_operation_tax(self, operation_data: dict) -> dict[str, int]:
        """
        Calculate taxes when you sell stocks
        Args:
            operation_data dict: information about operation {"operation":"buy", "unit-cost":10.00, "quantity": 10}

        Returns:
            dictionary with all information about the operation like {"tax":0, ...}
        """
        stock_process = self.calculator_stock_process
        stock_process.track_operation(operation_type='sell', operation_data=operation_data)
        if stock_process.sell_price_lower(operation_data=operation_data):
            return stock_process.get_values_taxes(tax_profit=0)

        if stock_process.sell_total_price(operation_data=operation_data):
            return stock_process.get_values_taxes(tax_profit=0)

        overall_profit = stock_process.overall_profit(operation_data)
        if stock_process.track_losses(overall_profit):
            return stock_process.get_values_taxes(tax_profit=0)

        tax_profit = stock_process.taxes_sell_transaction(overall_profit)
        return stock_process.get_values_taxes(tax_profit)