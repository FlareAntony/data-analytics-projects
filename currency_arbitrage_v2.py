print("--- REMOTE USD TO THB ARBITRAGE CALCULATOR ---")
usd_input = input("Enter your monthly remote U.S. salary ($): ")
exchange_rate_input = input("Enter current exchange rate (1 USD to THB, e.g., 34): ")

salary_usd = float(usd_input)
exchange_rate = float(exchange_rate_input)

rent_thb = float(input("Monthly Rent cost (THB): "))
food_thb = float(input("Monthly Food cost (THB): "))
utilities_thb = float(input("Monthly Utilities cost (THB): "))
insurance_thb = float(input("Monthly Insurance cost (THB): "))
print("\n--- Investment Strategy ---")
fun_percent_input = input("What % of your surplus do you want to spend on fun activities? (e.g., 20 for 20%): ")
fun_percent = float(fun_percent_input) / 100

total_expenses_thb = rent_thb + food_thb + utilities_thb + insurance_thb
total_revenue_thb = salary_usd * exchange_rate

surplus_thb = total_revenue_thb - total_expenses_thb
surplus_usd = surplus_thb / exchange_rate
fun_money_thb = surplus_thb * fun_percent
investment_thb = surplus_thb - fun_money_thb
fun_money_usd = fun_money_thb / exchange_rate
investment_usd = investment_thb / exchange_rate

print("\n==============================================")
print("          MONTHLY EXECUTIVE DASHBOARD         ")
print("==============================================")
print(f"Total Gross Revenue:   {total_revenue_thb:,.2f} THB")
print(f"Total Living Expenses:  {total_expenses_thb:,.2f} THB")
print(f"Net Household Surplus: {surplus_thb:,.2f} THB")
print("----------------------------------------------")
print(f"🎉 Local Fun Money Bucket: {fun_money_thb:,.2f} THB  (${fun_money_usd:,.2f} USD)")
print(f"📈 Dispatched to S&P 500:  {investment_thb:,.2f} THB  (${investment_usd:,.2f} USD)")
print("==============================================")
