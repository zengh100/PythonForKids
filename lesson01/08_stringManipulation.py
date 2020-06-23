#https://realpython.com/python-strings/

# Access individual character in a string with index
# Note the index starts from 0.  
a="Hello World"
#print the first character in a
print(a[0])

#print the second character in a
print(a[1])

#print the 7th character in a
print(a[6])


#print the last character (the 11th) in a
print(a[10])

# a simple way to access the last with -1
print(a[1])


# The + Operator concatenates strings
h="Hello"
w="World"
hw = h+w
print(h+w)

#The * operator creates multiple copies of a string
s = 'foo.'
t = s*4
print(t)

#functions related to string
#len(): get length of a string (how many chanracters)

#str(): convert numbers to string

#int(): convert string to integer

#float(): convert string to float

'''
String Slicing
Python also allows a form of indexing syntax that extracts substrings from a string, known as string slicing. If s is a string, an expression of the form s[m:n] returns the portion of s starting with position m, and up to but not including position n:
'''
s='hello'
t=s[1:4]

s='0123456789'
print(s[::2])
print(s[::-2])

s='0123456789'
print(s[1::2])
print(s[-2::-2])

s='iamstring'
print(s[::3])
print(s[::-3])

#split: Splits a string into a list of substrings.
s = 'www.realpython.com'
t = s.split('.')
print(s)
print(t)
