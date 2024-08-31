from collections import OrderedDict

from .factory_opertation import StockOperationFactory
from .tax_calculator import TaxProcessCalculus


def get_capital_gains(transaction):
    tmp_dict = OrderedDict()

    stock_tax_process_calculus = TaxProcessCalculus()

    for number_transaction, data_tansaction in enumerate(transaction):
        operation_type = data_tansaction.get("operation")

        operation_obj = StockOperationFactory.create_operation(operation_type)
        info_transaction = operation_obj(stock_tax_process_calculus).get_operation_tax(data_tansaction)

        data_tansaction.update(info_transaction)
        tmp_dict[f'transaction_{number_transaction}'] = data_tansaction

    result = [{"tax": value["tax"]} if value['error'] == '' else {"error": value["error"]} for value in tmp_dict.values()]
    return result

