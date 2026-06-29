#loops
# for loop
for i in range(5):
    print("Iteration:",i)

    #while loop
count=0
while count<5:
    print("Count:",count)
    count+=1

#do-while loop
count=0
while True:
    print("Count:",count)
    count+=1
    if count>=5:
        break

#conditional statements and loops together
for i in range(10):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")

#functions
def greet(name):
    return "Hello, "+name+"!"
print(greet("Alice"))
print(greet("Bob"))

#recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n-1)

print(sum_numbers(5))

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Python"))