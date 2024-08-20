from constant import DECIMAL_PRECISION
def become_decimal_precision(number):
    return float(f"{number:.{DECIMAL_PRECISION}f}")