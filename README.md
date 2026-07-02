# dev-journey
A structured learning journey through Web Development, Data Structures &amp; Algorithms, C programming and Python as a Computer Science engineering student. This repository contains daily practice code, LeetCode solutions, and project work covered during summer vacations 2026. Built with consistency.
<br>
Author-Jasica Aggarwal
<br>
College-Lovely Professional University
<br>
11th june 2026- Started to learn how to use git and github 
<br>
12th june 2026-learnt whole git and github, commands of github.
<br>
13th june 2026- CSS revision started brushing up all the basics of css.attended 7 hrs lecture to again through css from basics to detail.
<br>
Working continuously on github
<br>
studying python 
learnt upto Recursion will start tomorrow with other topic
my vs code is not working something error in pushing the code but i did practise and so i will commit and push tmr for both days.
<BR>
GIT COMMANDS AND FOLDER PROBLEM IS NOT GETTING RESOLVED SO TODAYS CODE 
<BR>
# Recursive function to find GCD
def gcd(a, b):
    # Base case
    if b == 0:
        return a
    # Recursive call
    return gcd(b, a % b)

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling the recursive function
result = gcd(num1, num2)

# Displaying the result
print("The GCD of", num1, "and", num2, "is", result)
