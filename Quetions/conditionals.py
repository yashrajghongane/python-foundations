# Movie Ticket Discount

# Fruit Ripeness Check
fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Yellow":
        print("The fruit is a ripe banana.")
    else:
        print("The fruit is an unripe banana.")
else:
    print("The fruit is not a banana.")

# Weather Check
weather = "Rainy"
if weather == "Sunny":
    print("Go for a walk.")
elif weather == "Rainy":
    print("Stay indoors and read a book.")
elif weather == "Snowy":
    print("Build a snowman.")
else:
    print("Check the weather forecast for more details.")

# Transportation Mode Selection
distance = 4
if distance < 4:
    print("Walk for covering Distance")
elif distance < 16:
    print("Use Bike For Transportation")
else:
    print("Use Car for Transportation")

# Order Coffee
order_size = "small"
extra_shot = True

if extra_shot:
    coffee = order_size + " Coffee With an Extra Shot"
    print(coffee)
else:
    coffee = order_size + " Coffee"
    print(coffee)

# Password Strength Check
password = "pas@3"

if len(password) < 6:
    print("Password is weak")
elif len(password) < 10:
    print("Password is Medium")
else:
    print("Password is Strong")

# Check Leap Year
year = 2036

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Is Leap Year")
else:
    print("Is not Leap Year")

# Recommend Food
pets = "Dog"
age = 2

if pets == "Dog" and age <= 2:
    print("Recommended food is Puppy Food")
elif pets == "Cat" and age >= 5:
    print("Recommended Food is Senior Cat Food")
else:
    print("Give Junior Cat food")
