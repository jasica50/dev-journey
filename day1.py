#practice python basics
#variables and data types
name="Jasica Aggarwal"
age=19
cgpa=7
is_student=True
print("Name:",name)
print("Age:",age)
print("CGPA:",cgpa)
print("Is Student:",is_student)

#strings
first_name="Jasica"
last_name="Aggarwal"
full_name=first_name+" "+last_name
print("Full Name:",full_name)
print("Length of Full Name:",len(full_name))
print("Uppercase Full Name:",full_name.upper())

#conditional statements
marks=85
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
else:    print("Grade: F")

#operators
a=10
b=5
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b) #returns a float
print("Modulus:",a%b) #returns the remainder
print("Exponentiation:",a**b)   #returns a raised to the power of b
print("Floor Division:",a//b) #returns the quotient without the remainder

#comparion operators
x=10
y=20
print("x > y:",x>y) #return true or false
print("x < y:",x<y)
print("x == y:",x==y)
print("x != y:",x!=y)

#logical operators
p=True
q=False
print("p and q:",p and q) #returns true if both are true
print("p or q:",p or q) #returns true if either is true
print("not p:",not p) #returns true if p is false
print("not q:",not q) #returns true if q is false

#loops
#for loop
