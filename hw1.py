import random

rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

total_bill = rice_total + sugar_total + oil_total

total_bill_int = int(total_bill)

total_bill_string = str(total_bill_int)

delivery_charge = random.randint(5, 10)

final_bill = total_bill_int + delivery_charge

print("Rice total: ₹", rice_total)
print("Sugar total: ₹", sugar_total)
print("Oil total: ₹", oil_total)

print("Total bill:", total_bill)
print("Total bill as integer:", total_bill_int)
print("Total bill as string:", total_bill_string)

print("Delivery charge: ₹", delivery_charge)
print("Final bill including delivery: ₹", final_bill)