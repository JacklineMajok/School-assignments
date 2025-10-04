#problem3.py
#Name: Jackline Yom Ajoh Majok
#Date: 23/09/025
#Description: program that run the verse of 99 bottles of beer starting with n bothles

def bottle_verse(n):
    if n > 1:
        print(f"{n} bottles of beer on the wall")
        print(f"{n} bottles of beer")
        print("Take one down, pass it around")
        if n - 1 == 1:
            print("1 bottle of beer on the wall")
        else:
            print(f"{n-1} bottles of beer on the wall")
    elif n == 1:
        print("1 bottle of beer on the wall")
        print("1 bottle of beer")
        print("Take one down, pass it around")
        print("No more bottles of beer on the wall")
    else:
        print("No more bottles of beer on the wall")
        print("No more bottles of beer")
        print("Go to the store and buy some more")
        print("99 bottles of beer on the wall")

bottle_verse(99)
for n in range(99, 0, -1):
    bottle_verse(n)
    print()

