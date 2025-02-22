def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

initial_amount = float(input("Enter the initial amount: "))
annual_rate = float(input("Enter the annual rate (as a decimal): "))
years = int(input("Enter the number of years: "))

invest(initial_amount, annual_rate, years)