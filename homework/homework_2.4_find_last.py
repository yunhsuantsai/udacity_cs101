# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(s, target):
    last = -1
    while True:
        if s.find(target, last + 1) == -1:
            return last
        else:
            last = last + 1



print (find_last('aaaa', 'a'))
print (find_last('aaaa', 'aa'))
print (find_last('aaaa', 'b'))
print (find_last("111111111", "1"))
print (find_last("222222222", ""))
print (find_last("", "3"))
print (find_last("", ""))

#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 2

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0




