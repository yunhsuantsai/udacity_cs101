# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# I use bigger to compare 2 number, 
# and use the bigger one to compare with the 
# third number to get the biggest number 

def bigger (x, y):
    if x > y:
        return x
    else: 
        return y

def biggest(a, b, c):
    return bigger(bigger(a,b), c)

print (biggest(3, 6, 9))
print (biggest(6, 9, 3))
print (biggest(9, 3, 6))
print (biggest(3, 3, 9))
print (biggest(9, 3, 9))


#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9