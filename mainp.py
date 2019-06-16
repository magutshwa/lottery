import random
from hashlib import new

# Request numbers from the user.
print("\nEnter your lucky numbers between one and thirty\n")
g1 = int(input("First number: "))
while g1 < 1 or g1 > 30:
    print("\nOut of range!")
    g1 = int(input("Try again: "))

g2 = int(input("\nSecond number: "))
while g2 < 1 or g2 > 30 or g2 == g1:
    if g2 == g1:
        print("\nYou cannot enter the same number twice!")
        g2 = int(input("Try again: "))
    else:
        print("\nOut of range!")
        g2 = int(input("Try again: "))


g3 = int(input("\nThird number: "))
while g3 < 1 or g3 > 30 or g3 == g2 or g3 == g1:
    if g3 == g2 or g3 == g1:
        print("\nYou cannot enter the same number twice!")
        g3 = int(input("Try again: "))
    else:
        print("\nOut of range!")
        g3 = int(input("Try again: "))


# Generate three random numbers from 1 to 30.
def lnumbers():
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    c = random.randint(1, 30)
    if b == a:
        b = new.random.randint(1, 30)
    if c == b or c == a:
        c = new.random.randint(1, 30)
    return a, b, c


# Call the random numbers.
numbs = lnumbers()
win1 = numbs[0]
win2 = numbs[1]
win3 = numbs[2]

# Compare user numbers to random numbers.
cor1 = 0
cor2 = 0
cor3 = 0
ncount = 0
if win1 == g1 or win1 == g2 or win1 == g3:
    cor1 = win1
    ncount += 1
if win2 == g1 or win2 == g2 or win2 == g3:
    cor2 = win2
    ncount += 1
if win3 == g1 or win3 == g2 or win3 == g3:
    cor3 = win3
    ncount += 1

# Display the results.
print("\nYour numbers are ", g1, g2, g3)
print("The winning numbers are: ", win1, win2, win3)
print("You\'ve got " + str(ncount) + " number(s) correct.")
print(cor1, cor2, cor3)
