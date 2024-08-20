import sys
import main
from faker import Faker
from app.tax_calculator import TaxProcessCalculus
from app.stock_calculator import StockProcessCalculus
from app.constant import RULE_TAX_TOTAL_PRICE, TAXES_DEFAULT, DECIMAL_PRECISION

fake_data = Faker()

def test_app_main_exit(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', ['exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = ''
    assert captured.out == expected_output

def test_app_main_error(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', ['abc'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = 'Invalid JSON format\n'
    assert captured.out == expected_output

def test_get_profit():
    stock_calculator = StockProcessCalculus()
    cost_stock = fake_data.pyint()
    stock_calculator.list_cost_stock = [cost_stock]
    data = {"operation": "buy", "unit-cost": fake_data.pyint(), "quantity": fake_data.pyint()}
    profit = stock_calculator.get_profit(data)
    fake_profit = abs(data.get("unit-cost") - cost_stock ) * data.get("quantity")
    assert profit == fake_profit

def test_losses_transaction():
    stock_calculator = StockProcessCalculus()
    cost_stock = fake_data.pyint()
    stock_calculator.list_cost_stock = [cost_stock]
    data = {"operation": "buy", "unit-cost": fake_data.pyint(), "quantity": fake_data.pyint()}
    profit = stock_calculator.get_profit(data)
    fake_profit = abs(data.get("unit-cost") - cost_stock ) * data.get("quantity")
    assert profit == fake_profit

def test_track_losses():
    stock_calculator = StockProcessCalculus()
    stock_calculator.total_losses = 100
    assert stock_calculator.track_losses(50) is False
    assert stock_calculator.total_losses == 50

def test_overall_profit():
    stock_calculator = StockProcessCalculus()
    total_losses = fake_data.pyint()
    stock_calculator.total_losses = total_losses
    cost_stock = fake_data.pyint()
    stock_calculator.list_cost_stock = [cost_stock]
    data = {"operation": "buy", "unit-cost": fake_data.pyint(), "quantity": fake_data.pyint()}
    profit = stock_calculator.overall_profit(data)
    fake_profit = abs(data.get("unit-cost") - cost_stock ) * data.get("quantity") - total_losses
    assert profit == fake_profit

def test_track_operation_buy():
    stock_calculator = StockProcessCalculus()
    data = {"operation": "buy", "unit-cost": fake_data.pyint(), "quantity": fake_data.pyint()}
    result = stock_calculator.track_operation("buy", data)
    assert result['total_stock'] == data.get("quantity")
    assert result['total_cost'] == -data.get("unit-cost")*data.get("quantity")


def test_track_operation_sell():
    stock_calculator = StockProcessCalculus()
    data = {"operation": "buy", "unit-cost": fake_data.pyint(), "quantity": fake_data.pyint()}
    result = stock_calculator.track_operation("sell", data)
    assert result['total_stock'] == -data.get("quantity")
    assert result['total_cost'] == data.get("unit-cost")*data.get("quantity")


def test_weighted_average():
    stock_calculator = StockProcessCalculus()
    total_stock, list_cost_stock=fake_data.pyint(), fake_data.pyint()
    stock_calculator.total_stock = total_stock
    stock_calculator.list_cost_stock = [list_cost_stock]
    data = {"operation": "buy", "unit-cost": fake_data.pyint(), "quantity": fake_data.pyint()}
    result = stock_calculator.weighted_average(data)

    fake_result = ((total_stock * list_cost_stock) +
                                            (data.get("quantity") * data.get("unit-cost"))) / (
                                                       total_stock + data.get("quantity"))

    assert result == round(fake_result,2)


def test_sell_price_lower():
    tax_calculator = TaxProcessCalculus()
    list_cost_stock = fake_data.pyint(100,1000)
    tax_calculator.list_cost_stock.append(list_cost_stock)

    data = {"operation": "buy", "unit-cost": fake_data.pyint(0,100), "quantity": fake_data.pyint()}
    result = tax_calculator.sell_price_lower(data)

    assert result == True


def test_sell_price_higher():
    tax_calculator = TaxProcessCalculus()
    list_cost_stock = fake_data.pyint(0, 100)
    tax_calculator.list_cost_stock.append(list_cost_stock)

    data = {"operation": "buy", "unit-cost": fake_data.pyint(100, 1000), "quantity": fake_data.pyint()}
    result = tax_calculator.sell_price_lower(data)

    assert result == False


def test_sell_total_price():

    tax_calculator = TaxProcessCalculus()

    data = {"operation": "buy", "unit-cost": fake_data.pyint(100, 1000), "quantity": fake_data.pyint()}
    result = tax_calculator.sell_total_price(data)
    result_fake = data.get("quantity")*data.get("unit-cost") <= RULE_TAX_TOTAL_PRICE
    assert result == result_fake


def test_taxes_sell_transaction():

    tax_calculator = TaxProcessCalculus()
    overall_profit = fake_data.pyint()
    result = tax_calculator.taxes_sell_transaction(overall_profit)
    assert result == round(overall_profit*TAXES_DEFAULT, DECIMAL_PRECISION)
