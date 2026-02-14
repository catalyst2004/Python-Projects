# Description - The program will act as a calculator and will have all the operations of a calculator.
print("Welcome to the calculator program")
# function to convert variable data type
def convert_number(var):
   try: 
     return int(var)
   except ValueError:
     try:
       return float(var)
     except ValueError:
       print("Invalid number Entered...")
       exit()
# input starts here        
var1 = convert_number(input("Enter the first number:"))
var2 = convert_number(input("Enter the second number:"))
operator = input("Enter the operation you want to perform(+,-,*,/,**(power):")
if operator == "+":
  print(f"The sum of {var1} and {var2} is {var1 + var2}.")
elif operator == "-":
  print(f"The difference of {var1} and {var2} is {var1 - var2}.")
elif operator == "*":
  print(f"The product of {var1} and {var2} is {var1 * var2}.")
elif operator == '/':
  if var2 == 0:
    print("The division is not possible as the divisor is zero.")
  else:
    print(f"The quotient of {var1} and {var2} is {var1 // var2}.")
    if isinstance(var1,int) or isinstance(var2,int):
     print(f"The remainder of {var1} and {var2} is {var1 % var2}")
elif operator == "**": # prints the power of var1^var2
  print(f"The power of {var1} and {var2} is {var1 ** var2}")
else:
  print("Invalid Operator!!")  
