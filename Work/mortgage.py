# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_count = 0
extra_payment_start_month = 5*12
extra_payment_end_month = 9*12
extra_payment = 1000


while principal > 0:
    if month_count>=extra_payment_start_month and month_count<=extra_payment_end_month-1:
        new_payment = round(payment+extra_payment,2)
    else:
        new_payment = round(payment, 2)
    principal = round(principal * (1+rate/12) - new_payment, 2)
    total_paid = round(total_paid + new_payment,2)
    month_count += 1
    print(month_count, total_paid, principal)

print("Total paid",total_paid)
print("Months", month_count)

