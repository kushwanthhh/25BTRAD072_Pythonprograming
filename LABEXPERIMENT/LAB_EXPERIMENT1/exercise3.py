print("1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Area of Circle\n"
      "6. Area of Rectangle\n"
      "7. Area of Square")

Operations = int(input("Enter a number: "))

if Operations in (1, 2, 3, 4):

    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    if Operations == 1:
        print("Addition:", a + b)

    elif Operations == 2:
        print("Subtraction:", a - b)

    elif Operations == 3:
        print("Multiplication:", a * b)

    elif Operations == 4:
        print("Division:", a / b)

elif Operations == 5:

    r = float(input("Enter the radius: "))
    print("Area of circle:", (22 / 7) * r ** 2)

elif Operations == 6:

    l = float(input("Enter the length: "))
    b = float(input("Enter the breadth: "))
    print("Area of rectangle:", l * b)

elif Operations == 7:

    s = float(input("Side of square: "))
    print("Area of square:", s ** 2)

else:
    print("Entered number is invalid")
