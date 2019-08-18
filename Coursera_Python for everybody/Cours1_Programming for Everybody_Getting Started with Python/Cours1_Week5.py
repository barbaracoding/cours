# Week 4

# Write a program to prompt the user for hours and rate
# per hour using input to compute gross pay.

# Pay the hourly rate for the hours up to 40 and 1.5 times
# the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program
# (the pay should be 498.75). You should use input to read a string
# and float() to convert the string to a number. Do not worry about
# error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h <= 40.0:
    down = h * r
    print(down)

if h > 40.0:
    under = 40.0 * r
    up = h - 40.0
    float(up)
    sup = up * r * 1.5
    pay = under + sup
    float(pay)
    print(pay)

# Write a program to prompt for a
# score between 0.0 and 1.0. If the score is
# out of range, print an error. If the score
# is between 0.0 and 1.0, print a grade using
# the following table:
''''
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
'''
# If the user enters a value out of range, print a suitable
# error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
score = float(score)
if score > 1.0:
    print("Error")

else:
    if score >= 0.9:
        print("A")
    elif score >= float(0.8):
        if score < float(0.9):
            print("B")
        else:
            print("Error")
    elif score >= float(0.7):
        if score < float(0.8):
            print("C")
        else:
            print("Error")
    elif score >= float(0.6):
        if score < float(0.7):
            print("D")
        else:
            print("Error")
    elif score < float(0.6):
        print("F")
