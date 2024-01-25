print('Welcome to the Tip Calculator')

bill = float(input('What was the total bill? shs'))

tip = int(input('How much tip would you like to give? shs'))

people = int(input('How many people to split the bill?'))

tip_as_percentage = tip / 100
total_tip = tip_as_percentage * tip_as_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people

final_amount = '{:.2f}'.format(bill_per_person)

print(f'Each member should pay: shs{final_amount}')
