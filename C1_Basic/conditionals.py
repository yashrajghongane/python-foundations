# Conditional Statement
# If Statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
# Shorthand If Statement
if age >= 18: print("You can vote now.")
print("\n")
# If-Else Statement
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
# Shorthand If Statement
if age > 18: print("Eligible to Vote.")
print("\n")
# Nested If Statement
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is non-positive.")

# Shorthand If-Else Statement
result = "Even" if num % 2 == 0 else "Odd"
print("The number is", result)
print("\n")

# Elif Statement
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:   
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")   
print("\n")
# Match-Case Statement
day = input("Enter a day of the week: ")
match day:
    case "Monday":
        print("Start of the work week.")
    case "Wednesday":
        print("Midweek day.")
    case "Friday":
        print("End of the work week.")
    case _:
        print("Just another day.")  