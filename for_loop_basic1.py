# Basic - Print all integers from 0 to 150.
for x in range(0, 151, 1):
    print("Basic: " + str(x))

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range(5, 1005, 5):
    print("Multiples of 5: " + str(y))


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for z in range(1, 101):
    if (z % 10 == 0):
        print("Coding Dojo")
    elif (z % 5 == 0):
        print("Coding")
    else:
        print(z)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for a in range(0, 500001):
    if (a % 2 != 0):  # checks if odd
        sum += a  # adds to sum if odd
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
for w in range(2018, 0, -4):
    print(w)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for p in range(lowNum, highNum + 1):
    if (p % mult == 0):
        print(p)
