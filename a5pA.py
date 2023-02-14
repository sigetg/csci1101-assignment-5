# Write a program to determine which numbers in a set are greater than the
# average of that set.  Your program must first prompt the user for an integer
# count of how many numbers are in the set.  A count value of less than 1 is an
# error.  You can assume that the input is an integer.  Then, prompt the user to
# enter count values each on their own line.  You'll have to store the values in
# a list.  Once you have the full set of numbers, calculate the average then
# print each value that is strictly greater than the average.
#
# There are several important details you must handle in this program.  It's
# possible that you could have no values that are greater than the average,
# in which case you'll print a message to that effect (to below for formatting).
# Otherwise, print how many values there are above the average.  It's time to
# start dealing with proper natural language issues.  If there is exactly one
# number above the average then you'll print "1 number above average:".  Note
# the singular form for the word "number".  If there are multiple numbers above
# the average then you'll have to print "... numbers above average:", noting the
# plural form "numbers".  Again, see below for full formatting requirements.
# Finally, when you print the values that are greater than the average (to three
# decimal places), you also have to print that value's location in the set -
# using normal person logic.  That is, the first value given to you by the user
# is number 1, the second is number 2, and so on.
#
# Your input and output messages must conform to the following examples:
#
# How many numbers will you enter? 0
# You must provide at least 1 number!
#
# How many numbers will you enter? 3
# Enter your 3 numbers, each on their own line:
# 1.5
# 1.5
# 1.5
# Average = 1.500
# No values above the average.
#
# How many numbers will you enter? 5
# Enter your 5 numbers, each on their own line:
# 1
# 2
# 3
# 4
# 100
# Average = 22.000
# 1 number above average:
# Number 5: 100.000
#
# How many numbers will you enter? 6
# Enter your 6 numbers, each on their own line:
# 0.5
# 10
# 10
# 10
# 10
# 10
# Average = 8.417
# 5 numbers above average:
# Number 2: 10.000
# Number 3: 10.000
# Number 4: 10.000
# Number 5: 10.000
# Number 6: 10.000
#
# Note the order of inputs, capitalization of messages, spacing, etc.
import sys

a = int(input("How many numbers will you enter? "))

if a < 1:
    print("You must provide at least 1 number!")
    sys.exit()
    
numbers = []
print(f"Enter your {a} numbers, each on their own line:")

c = a
while c > 0:
    numbers.append(float(input()))
    c -=1

total = 0
for number in numbers:
    total += number

average = total / a
print(f"Average = {average:.3f}")

above_avg = 0
for number in numbers:
    if number > average:
        above_avg += 1

if above_avg == 1:
    print(f"{above_avg} number above average:")
elif above_avg > 1:
    print(f"{above_avg} numbers above average:")
else:
    print("No values above the average.")

b = 1
for number in numbers:
    if number > average:
        print(f"Number {b}: {number:.3f}")
    b += 1
