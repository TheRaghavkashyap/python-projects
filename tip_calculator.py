print("Welcome to the Tip calculator!")
billTotal = int(input("What is your total bill amount?\n$"))
numOfPeople = int(input("How many people are splitting the bill?\n"))
tipPercent = int(input("What percentage tip would you like to give? 10,12 or 15?\n"))
tip = billTotal * (tipPercent / 100)
amountPerPerson = (billTotal + tip) / numOfPeople
print(f"Each person should pay ${round(amountPerPerson, 2)}")