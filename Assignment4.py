#Question 1

Score= float(input("Please enter your marks "))

if Score<25:
    print("Your final grade is F")
elif Score>=25 and Score<45:
    print("Your final grade is E")
elif Score>=45 and Score<50:
    print("Your final grade is D")
elif Score>=50 and Score<60:
    print("Your final grade is C")
elif Score>=60 and Score<80:
    print("Your final grade is B")
elif Score>=80 and Score<=100:
    print("Your final grade is A")
else:
    print("Error: You cannot have the entered number of marks!")
    
    
#Question 2

Yr= int(input("Please enter year: "))

if Yr % 100 == 0:
    if Yr % 400 == 0:
        print("The year ",year," is a leap year!")
    else:
        print("The year ",year," is not a leap year :(")
elif Yr % 4 == 0:
    print("The year ",year," is a leap year!")
else:
    print("The year ",year," is not a leap year :(")


#Question 3

from random import randint

for loop_variable in range(10):
    n1 = randint(0,10)
    n2 = randint(0,10)
    if int(input('Question: ' + str(n1) + ' x ' + str(n2) + ' = ')) == n1 * n2: print('Right!')
    else: print('Wrong. The answer is ', n1 * n2)


#Question 4

number=1
while number<200:
    if number%5 == 2 and number%6 == 3 and number%7 == 2:
        print("The number is: " + str(number))
    number = number + 1
