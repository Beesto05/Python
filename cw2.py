header = """bookstore         """

book1 = "BOOK: {}\t₹{}".format("Python Basics", 450)
book2 = "BOOK: {}\t₹{}".format("Data Science Intro", 600)

total = 450 +600
total_amount = "TOTAL:\t\t₹{}".format(total)

thank_you = "\nTHANK YOU FOR SHOPPING WITH US!"

receipt = header + "\n" + book1 + "\n" + book2 + "\n" + total_amount + thank_you

print(receipt.upper())

