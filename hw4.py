
fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Water", "Juice", "Milk"]

fruits.append("Orange")
vegetables.insert(1, "Onion")
beverages.pop()

inventory = [fruits, vegetables, beverages]

print(fruits[:2])
print(vegetables[-1])

lengths = [len(x) for x in fruits]
print(lengths)

print("Water" in beverages)

items = (fruits[0], vegetables[0], beverages[0])
print(items)
