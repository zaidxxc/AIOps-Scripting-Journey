# Movie Ticket Booking Calculator - Workshop Level 1
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'
is_member = False
is_weekend = False

# 1. Eligibility Check
if age > 17:
    print('User is eligible to book a ticket')

# 2. Discount Logic
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')

# 3. Extra Charges Logic
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges applied')

# 4. Final Calculation
if age >= 21 or (age >= 18 and (show_time != 'Evening' or is_member)):
    service_charges = 5 if seat_type == 'Premium' else 3 if seat_type == 'Gold' else 1
    final_price = base_price + service_charges + extra_charges - discount
    print(f'Final price of ticket: {final_price}')
else:
    print('Ticket booking failed due to restrictions')