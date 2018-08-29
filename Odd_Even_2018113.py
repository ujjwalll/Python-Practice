# Hyphenator_even.py
# the CS 1110 profs (cs-1110profs-L@cornell.edu)
# Feb 2016

""" Inserts hyphens into a non-empty even-length input string as follows:
The hyphen splits the first and second halves. 
"""
## We've added a number of so-called "debugging" print statements here

s = input('Enter an even-length string: ')
n = len(s)
print ('n is',n)
if n%2 == 0:                           # Line A
    # s has even lengtH
    m = n//2
    print ('even case. m is',m)
    first = s[0:m]                     # Line B
    print ('even case. first is',first)
    second = s[m:]                     # Line C
    print ('even case. second is',second)
    h = first + '-' + second
    # final output
    print (s,'becomes',h)
else:
    m = n//2
    print ('odd case. m is',m)
    first = s[0:m+1]                     # Line B
    print ('odd case, first is',first)
    second = s[m+1:]                     # Line C
    print ('odd case second is',second)
    h = first + '-' + second
    # final output
    print(s,'becomes',h)	
