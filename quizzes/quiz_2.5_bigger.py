# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(a, b):
    if b > a:
        a = b
    return a

print (bigger(2, 7))
print (bigger(3, 2))
print (bigger(3, 3))

#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3