# exception = An event that interrupts the flow of a program
#       (zero division error, type error, value error)
#       1. try, 2. exception, 3. finally


try:
    number = int(input("enter a number: "))
    print(1/number)

except ZeroDivisionError:
    print("You cant divide by zero. ")

except ValueError:
    print("enter only numbers. ")

finally:
    print("do some cleanup")