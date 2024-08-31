EXAMPLE_1 = '[{"operation":"buy", "unit-cost":10.00, "quantity": 100}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}]'

EXAMPLE_2 = '''
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
{"operation":"sell", "unit-cost":20.00, "quantity": 5000},
{"operation":"sell", "unit-cost":5.00, "quantity": 5000}]
'''


EXAMPLE_3 = '''
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
{"operation":"sell", "unit-cost":5.00, "quantity": 5000},
{"operation":"sell", "unit-cost":20.00, "quantity": 3000}]
'''


EXAMPLE_4 = '''
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
{"operation":"buy", "unit-cost":25.00, "quantity": 5000},
{"operation":"sell", "unit-cost":15.00, "quantity": 10000}]
'''


EXAMPLE_5 ='''
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
{"operation":"buy", "unit-cost":25.00, "quantity": 5000},
{"operation":"sell", "unit-cost":15.00, "quantity": 10000},
{"operation":"sell", "unit-cost":25.00, "quantity": 5000}]
'''


EXAMPLE_6 = '''
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
{"operation":"sell", "unit-cost":2.00, "quantity": 5000},
{"operation":"sell", "unit-cost":20.00, "quantity": 2000},
{"operation":"sell", "unit-cost":20.00, "quantity": 2000},
{"operation":"sell", "unit-cost":25.00, "quantity": 1000}]
'''


EXAMPLE_7 = '''
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
{"operation":"sell", "unit-cost":2.00, "quantity": 5000},
{"operation":"sell", "unit-cost":20.00, "quantity": 2000},
{"operation":"sell", "unit-cost":20.00, "quantity": 2000},
{"operation":"sell", "unit-cost":25.00, "quantity": 1000},
{"operation":"buy", "unit-cost":20.00, "quantity": 10000},
{"operation":"sell", "unit-cost":15.00, "quantity": 5000},
{"operation":"sell", "unit-cost":30.00, "quantity": 4350},
{"operation":"sell", "unit-cost":30.00, "quantity": 650}]
'''


EXAMPLE_8 = '''
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
{"operation":"sell", "unit-cost":50.00, "quantity": 10000},
{"operation":"buy", "unit-cost":20.00, "quantity": 10000},
{"operation":"sell", "unit-cost":50.00, "quantity": 10000}]
'''

EXAMPLE_9 = '''
[{"operation":"buy", "unit-cost": 5000.00, "quantity": 10},
{"operation":"sell", "unit-cost": 4000.00, "quantity": 5},
{"operation":"buy", "unit-cost": 15000.00, "quantity": 5},
{"operation":"buy", "unit-cost": 4000.00, "quantity": 2},
{"operation":"buy", "unit-cost": 23000.00, "quantity": 2},
{"operation":"sell", "unit-cost": 20000.00, "quantity": 1},
{"operation":"sell", "unit-cost": 12000.00, "quantity": 10},
{"operation":"sell", "unit-cost": 15000.00, "quantity": 3}]
'''

EXAMPLE_10 = '''
[{"operation":"buy", "unit-cost": 10, "quantity": 10000},
 {"operation":"sell", "unit-cost":20, "quantity": 11000},
 {"operation":"sell", "unit-cost": 20, "quantity": 5000}]
'''


TEST_EXAMPLES = {
 "EXAMPLE_BASE": '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}]',
 "EXAMPLE_BASE_ONE": '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"sell", "unit-cost":20.00, "quantity": 5000}]',
 "EXAMPLE_1": EXAMPLE_1,
 "EXAMPLE_2": EXAMPLE_2,
 "EXAMPLE_3": EXAMPLE_3,
 "EXAMPLE_4": EXAMPLE_4,
 "EXAMPLE_5": EXAMPLE_5,
 "EXAMPLE_6": EXAMPLE_6,
 "EXAMPLE_7": EXAMPLE_7,
 "EXAMPLE_8": EXAMPLE_8,
 "EXAMPLE_9": EXAMPLE_9,
 "EXAMPLE_10": EXAMPLE_10,
}





