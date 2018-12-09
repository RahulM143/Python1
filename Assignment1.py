#Q2.  Write a program which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
#in a comma-separated sequence on a single line.
a = 2000
b = 3200
numbers = []
while a <= b:
    if a%7 == 0 and a%5 != 0:
        numbers.append(a)
    a = a + 1 
print(numbers)

#Q3. Write a Python program to accept the user's first and last name and then getting them printed
in the the reverse order with a space between first name and last name.

firstname = input("Please enter your first name: ")
lastname = input ("Please enter your last name: " )
fullname = firstname + " " + lastname
length = len(fullname)
length
n=1
print("Reverse of your name is: ")
while length != 0:
    print (fullname[-n], end ="")
    n +=1
    length -=1

#Q4. Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r cube
r = 12
pi = 3.1415
v = 4/3 * pi* r**3
print("Volume of the Sphere with diameter ", r ," cm is " , v ," cubic cm") 






