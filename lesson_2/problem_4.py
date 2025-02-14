num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1>num2:
    int_part = num1//num2
    remainder = num1%num2
    print("Butun qisim is ", int_part, "Qoldiq is ", remainder)
else:
    int_part = num2 // num1
    remainder = num2 % num1
    print("Butun qisim is ", int_part, "Qoldiq is ", remainder)
