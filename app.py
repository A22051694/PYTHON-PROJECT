currencyDict = {}

# PYTHON-PROJECT
# Currency Converter

def load_currency_rates(filename):
    currency_dict = {}
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                currency_dict[parts[0]] = float(parts[1])
    return currency_dict

def main():
    currency_dict = load_currency_rates('CURRENCY_2')
    print("Welcome to the Currency Converter!")
    while True:
        try:
            amount = float(input("\nEnter amount in INR: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        print("\nAvailable currencies:")
        for code in currency_dict:
            print(code)
        currency = input("Enter the currency code to convert to (or 'exit' to quit): ").upper()
        if currency == 'EXIT':
            print("Exiting Currency Converter. Goodbye!")
            break
        if currency not in currency_dict:
            print("Invalid currency code. Please try again.")
            continue
        converted = amount * currency_dict[currency]
        print(f"{amount} INR is equal to {converted:.2f} {currency}")

if __name__ == "__main__":
    main()
  
