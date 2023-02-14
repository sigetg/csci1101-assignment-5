# Write a program to analyze text provided in the Python shell.  Specifically,
# your program must count how many times each of the 26 letters in the English
# alphabet occurs in the provided text.  Uppercase and lowercase letters must be
# counted together, i.e., "A" and "a" both count as the letter A.  Any
# characters that are not one of the 26 letters are ignored.  After all provided
# text has been analyzed your program must print the count of how many times
# each letter appeared, provided that the letter appeared at least once.
#
# Recall from the lecture that you can easily loop over every line provided in
# the shell.  Remember that the user indicates that no more input is coming by
# pressing Ctrl-D in the shell.  You'll get one line of input at a time as a
# string.  Recall also that you can loop over each character in a string easily.
#
# You'll need to use a list to keep track of each of the 26 counts.  The value
# at index 0 will be the count of how many times "A" or "a" appears.  The value
# at index 1 will be the count of how many times "B" or "b" appears, etc, up to
# the value at index 25 being the count of how many times "Z" or "z" appears.
# You could try to use a massive 26-long if/elif block to check each character
# against each letter.  Don't do that!  Instead, we can take advantage of the
# structure of a list - that each element is associated with an integer index.
# You'll need to take each character that you read, once you know it's one of
# the 26 letters, and convert it into an integer.  Specifically, you need to
# find a way to convert the letter "A" into a 0 (the index for counting the
# letter A), the letter "B" into a 1, …, and the letter "Z" into a 25.  Then you
# can use that to index directly into your list of counts to update it.  Look
# into the Python ord() method, and see what it returns for each of the 26
# letters.
#
# When you print out the counts at the end, only print out those counts that are
# least 1.  You have to print the letter with it, so you'll also need to find a
# way to reverse the letter-to-index conversion above: take your index and
# convert it back to the characters "A" to "Z".  Finally, if there are no
# letters at all (the counts are zero for all 26 letters), then print out that
# message so that the user gets at least some output.
#
# Note that the instructor's solution is only 20 lines of Python code.  You
# don't need to hit exactly that target.  Rather, use it as a benchmark for your
# solution.  If you are working towards a solution with a significantly higher
# line count then you are headed in the wrong direction.
#
# Your input and output messages must conform to the following examples:
#
# Enter the text you want analyzed:
# 12345+!@#
# 67890-%^&
# No letters found!
#
# Enter the text you want analyzed:
# asdfASDF
# ASDFasdf
# a's = 4
# d's = 4
# f's = 4
# s's = 4
#
# Enter the text you want analyzed:
# The quick brown
# fox jumps over the
# lazy dog!!!111!
# a's = 1
# b's = 1
# c's = 1
# d's = 1
# e's = 3
# f's = 1
# g's = 1
# h's = 2
# i's = 1
# j's = 1
# k's = 1
# l's = 1
# m's = 1
# n's = 1
# o's = 4
# p's = 1
# q's = 1
# r's = 2
# s's = 1
# t's = 2
# u's = 2
# v's = 1
# w's = 1
# x's = 1
# y's = 1
# z's = 1
#
# Note the order of outputs, capitalization of messages, spacing, etc.

import sys

print("Enter the text you want analyzed:")

letters = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h",  "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in sys.stdin:
    line = line.strip()
    for letter in line:
        for point in range(0, 52, 2):
            if letter == letters[point] or letter == letters[point+1]:
                numbers[point//2]  += 1

x=0
for number in numbers:
    if number != 0:
        x += 1
if x == 0:
    print("No letters found!")
    sys.exit()
        
label_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
x = 0
for number in numbers:
    if number == 0:
        pass
    else:
        print(f"{label_letters[x]}'s = {number}")
    x +=1

