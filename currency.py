# Dictionary storing exchange rates
exchange_rates = {
    "USD": 0.00067,
    "EUR": 0.00062,
    "GBP": 0.00054
}

# Function to convert NGN to other currencies
def convert_currency(amount_ngn, rates):
    for currency, rate in rates.items():
        converted_amount = amount_ngn * rate
        print(f"{currency}: {converted_amount:.2f}")

# Collect user input
amount = float(input("Enter amount in Nigerian Naira (NGN): "))

# Display results
print("\nConverted Amounts:")
convert_currency(amount, exchange_rates)
