'''Write a program to calculate the cost of a meal at a restaurant.

The cost of the meal depends on the main dish and the time of the day.
Main dishes available:
"paneer tikka": ₹250
"butter chicken": ₹240
"masala dosa": ₹200
Additional discounts:
15% discount for meals ordered during lunchtime (from 12 PM to 3 PM).
Customers can apply vouchers for an additional 10% discount on the total cost.
The restaurant accepts card payments.
For card payments, there's an additional service charge of 5% on the total cost after applying any discounts.
Take the following inputs:
Main dish : str
Time of the day: int: 24-hour format
Whether the customer has a voucher: bool: True/False
Whether the payment is by card: bool: True/False
Calculate and display the total cost of the meal.'''
main_dish = input()
time_of_day = int(input())
has_voucher = input() == "True"
is_card_payment = input() == "True"

if main_dish == "panner tikka":
    cost = 250
elif main_dish == "butter chikcen":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else: # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    exit() 

if time_of_day >= 12 and time_of_day <= 15:
    total_cost = (1 - 0.15) * cost

else:
    total_cost = cost

if has_voucher:
    total_cost *= 0.9  # Apply voucher discount

if is_card_payment: # service charge for card payment
    service_charge = 0.05 * total_cost
    total_cost += service_charge

print(f"{total_cost:.02f}")