total_bill = int(input("How much was the total bill? £"))
split_number = int(input("How many people are splitting the bill? : "))
tip_perc = int(input("How much would you like to tip in %? 5, 10 or 15 : "))
tip_perc_real = tip_perc/100

bill_plus_tip = total_bill + (total_bill * tip_perc_real)
bill_split = round(bill_plus_tip/split_number, 2)

print(f"The total bill, plus tip is : £{bill_plus_tip}")
print(f"The total to pay is £{bill_split} each")