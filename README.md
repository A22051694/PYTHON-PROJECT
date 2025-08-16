# Currency Converter

A simple Python project to convert INR to other currencies using offline rates.

## Usage

1. Run `python app.py`.
2. Enter the amount in INR.
3. Choose a currency code from the list.
4. Get the converted amount.
5. Type 'exit' to quit.

## Currency Rates

Rates are stored in `CURRENCY_2` as tab-separated values:
```
USD	80.502593
EUR	83.373695
...
```

## Requirements
- Python 3.x

## Notes
- Rates are sample values and may not reflect real-time exchange rates.
# PYTHON-PROJECT
CURRENCY CONVERTER
with open('Currency_2.txt') as f:
    lines = f.readlines()

currencyDict = {}
for lines in lines:
    parsed= lines.split('\t')
    currencyDict[parsed[0]]=parsed[1]

amount = int(input("Enter amount:\n"))
print("Enter the type of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please write one of these values: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")

