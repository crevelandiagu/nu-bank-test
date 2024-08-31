from symbol import pass_stmt

from .constant import DECIMAL_PRECISION


class StockProcessCalculus:
    """
    Stock calculator for implemente a diferente calculos for each stock transactions
    """
    def __init__(self):
        """
        Initialize stock values and acumulated diferent values (this is the value)
        """
        self.total_stock = 0
        self.total_cost = 0
        self.total_profit = 0
        self.total_losses = 0
        self.list_cost_stock = []
        self.list_weighted_average = 0
        self.error_count = 0

    def get_values(self) -> dict:
        """
        Get values for each stock transaction
        Returns dict:   return a general information for each stock transaction

        """
        return {
            'total_stock': self.total_stock,
            'total_cost': self.total_cost,
            'total_profit': self.total_profit,
            'total_losses': self.total_losses,
            'list_weighted_average': self.list_weighted_average,
            'error': self.error_msj
        }

    def get_profit(self, data: dict) -> float:
        """
        Calculate profit or gains for each stock transaction
        Args:
            data dict: information about operation {"operation":"buy", "unit-cost":10.00, "quantity": 10}

        Returns float:
            profit value
        """
        buy_value = self.list_cost_stock[-1]
        sell_value = data.get("unit-cost")
        sell_stock_quantity = data.get("quantity")
        profit_value = abs(sell_value - buy_value) * sell_stock_quantity
        return round(profit_value, DECIMAL_PRECISION)

    def losses_transaction(self, data: dict) -> float:
        """
        Calculate losses for each stock transaction with profit equations
        Args:
            data dict: information about operation {"operation":"buy", "unit-cost":10.00, "quantity": 10}

        Returns flaat:
            profit losses
        """
        return self.get_profit(data)

    def track_losses(self, overall_profit: float) -> bool:
        """
        calculate if losses is bigger than profit or lower and pay the all debt or you need other transactions
        Args:
            overall_profit float: profit value when you need pat tax

        Returns bool:
            If you need pay or no taxes for that transaction
        """
        if overall_profit <= 0:
            self.total_losses = -overall_profit
            return True
        if self.total_losses != 0:
            self.total_losses -= overall_profit
        return False


    def overall_profit(self, data) -> int:
        """
        Final value after to pay losses
        Args:
            data dict: information about operation

        Returns float:
            profit value minus losses
        """
        return self.get_profit(data) - self.total_losses

    def total_amount_transaction(self, quantity, price) -> float:
        """
        Calculate total amount transaction
        Args:
            quantity int: quantity of stock you buy or sell
            price: price of stock you buy or sell

        Returns:
            a final price you pay for sell or buy stock
        """

        total_cost = quantity * price
        return round(total_cost, DECIMAL_PRECISION)

    def weighted_average(self, data: dict) -> float:
        """
        Calculate a new purchase weighted average
        Args:
            data dict: information about operation 

        Returns float:
            new purchase value
        Examples:
                have bought 10 stocks for $ 20.00, sold 5 and bought other 5 for $ 10.00, the weighted average is
                ((5 x 20.00) + (5 x 10.00)) / (5 + 5) = 15.00 .
        """


        quantity = data.get("quantity")
        price = data.get("unit-cost")

        current_stock_quantity = self.total_stock
        weighted_average_price = self.list_cost_stock[-1]
        new_stock_quantity = quantity
        new_price = price
        new_weighted_average_price = ((current_stock_quantity * weighted_average_price) +
                                            (new_stock_quantity * new_price)) / (
                                                       current_stock_quantity + new_stock_quantity)
        self.list_weighted_average = new_weighted_average_price
        self.list_cost_stock.append(new_weighted_average_price)
        return round(new_weighted_average_price, DECIMAL_PRECISION)

    def track_operation(self, operation_type: str, operation_data: dict) -> dict:
        """
        track and save data in the object after each operation
        Args:
            operation_type str: type of operation like buy or sell
            operation_data dict: information about operation

        Returns dict:
            Returns a dictionary with general information
        """
        quantity = operation_data.get("quantity")
        price = operation_data.get("unit-cost")

        if operation_type == "buy":
            list_cost_stock = self.list_cost_stock
            if list_cost_stock and list_cost_stock[-1] != price and self.total_stock != 0:
                self.weighted_average(operation_data)
                self.total_stock += quantity
                self.total_cost -= self.total_amount_transaction(quantity, price)
                return self.get_values()

            self.total_stock += quantity
            self.total_cost -= self.total_amount_transaction(quantity, price)
            self.list_cost_stock.append(price)
            return self.get_values()

        elif operation_type == "sell":
            stock_sell = operation_data.get("quantity")
            if self.error_count >= 3:
                self.error_msj = "Your account is blocked"
                self.error_count += 1
                # ALERT
                return self.get_values()
            if (self.total_stock - stock_sell) < 0:
                self.error_msj = "Can't sell more stocks than you have"
                self.error_count += 1
                return self.get_values()

            self.total_stock -= quantity
            self.total_cost += self.total_amount_transaction(quantity, price)

        return self.get_values()


class ValidationTransaction(StockProcessCalculus):

    def __init__(self):
        self.tax_operation = 0

    def track_operation(self):
        pass

    def validate_amount_stok(self):
        # busines logic
        pass