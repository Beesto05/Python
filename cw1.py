import random

apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

total_volumes = apple_juice + orange_juice + grape_juice
print(total_volumes)
print(int(total_volumes))
print("total volume of juice sold: " + str(total_volumes)+"liters")
additional_bonus_liters = random.randint(5,10)
final_total = total_volumes + additional_bonus_liters 
print(final_total)
