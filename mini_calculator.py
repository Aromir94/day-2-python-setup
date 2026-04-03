print("Mini Calculator")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

print("\nResults")
print("---------")
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")

if second_number != 0:
    division = first_number / second_number
    print(f"{first_number} / {second_number} = {division}")
else:
    print("Division by zero is not allowed.")






