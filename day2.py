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

