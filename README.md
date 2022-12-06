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

