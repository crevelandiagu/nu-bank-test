import sys
import json
from app.view import get_capital_gains

def app_main():
    for line in sys.stdin:
        if line.strip() == "exit":
            break
        try:
            operations = json.loads(line)
            result = get_capital_gains(operations)
            json.dump(result, sys.stdout)
            print('\n')
            # print(json.dumps(result))
        except json.JSONDecodeError:
            print("Invalid JSON format")