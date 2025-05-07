# Write a Python program to do arithmetical operations for addition.
num1 = float(input("Enter the first number for Addition: "))
num2 = float(input("Enter the Second number for Addition: "))
Sum_result = num1 + num2
print(f"Sum : {num1} + {num2} = {Sum_result}")


# Write a Python program to do arithmetical operations for division.
num3 = float(input("Enter the first number for division: "))
num4 = float(input("Enter the second number for division: "))

if num4 == 0:
    print("Error: Division by 0 with not allowed. ")

else:
    div_result = num3 / num4
    print(f"Division : {num3} / {num4} = {div_result}")
