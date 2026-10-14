grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append("cake")
print (grocery_list)    

def remove_last_item(item):
    if grocery_list:
        grocery_list.pop()
    else:
        print("grocery list is empty")

print (grocery_list)    
    
display_item = lambda item: print(f"Item: {item}")

def count_characters(items):
    if not items: 
        return 0
    return len(items[0]) + count_characters(items[1:])

add_item("butter")
print("Grocery List:")
for item in grocery_list:
    display_item(item)

remove_last_item()

print("\nUpdated Grocery List:")
for item in grocery_list:
    display_item(item)

print("\nTotal characters:", count_characters(grocery_list))


