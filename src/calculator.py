#
#           FILE NAME       :       calculator.py
#
#           AUTHOR          :       ANUJ DUGGAL
#           CONTRIBUTORS    :       --
#           DATE CREATED    :       JUNE 7, 2015
#           DATE MODIFIED   :       JUNE 7, 2015
#           VERSION         :       1
#           DESCRIPTION     :       Calculator Program
#

# FUNCTION DEFINITIONS:
def div(n1,n2):
    return n1/n2

def mult(n1,n2):
    return (n1*n2)

def sub(n1, n2):
    return (n1-n2)

def add(num1,num2):
    c=num1+num2
    print "Sum = "+str(c)

# INITIAL MESSAGE:
print "Welcome to Calculator Function"
print "Menu:"
print "1. Add"
print "2. Subtract"
print "3. Multiply"
print "4. Division"

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if choice is 2:
    c = sub(num1, num2)
    print c

if(choice is 1):
    add(num1,num2)

if(choice is 3):
    c = mult(num1,num2)
    print c

if choice is 4:
    c=div(num1,num2)
    print c
    
x = input("dekh le output")
