# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
#day_of_week = current_date_and_time.weekday()

#the discount rate is 10% and the sals tax rate is 6%
discout_rate = .10
tax_rate = .06

#enter the subtotal of pruchase
sub_tot = float(input("Please enter the subtotal: "))

#Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

#if the day of the week is tueday or wensda and the subttotal
#is greater than 50 calculate the discount.

if sub_tot >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = round(sub_tot * discout_rate, 2)
    print(f'Discount amount: {discount: .2f}')
    sub_tot -= discount

#Compute the sales tax
sales_tax = round(sub_tot * tax_rate, 2)
print(f'Sales tax amount: {sales_tax: .2f}')

#Compute the total
total = sub_tot + sales_tax

#print total amount
print(F"Total amount: {total: .2f}")

