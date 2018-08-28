# Hyphenator_broken.py
# the CS 1110 profs (cs-1110profs-L@cornell.edu)
# Feb 2016

""" Inserts hyphens into a non-empty odd-length input string as follows:
A hyphen is inserted on either side of the middle character.

Example: "abcde" becomes "ab-c-de"

"""
### This program intentionally has at least one error in it!

s = input('Enter an odd-length string: ')

n = len(s)
if(n==1):
	print('String lenght 1')
elif(n%2!=0):
	m = int(n/2)


	first = s[0:m]


	middle = s[m:m+1]


	second = s[m+1:]


	h = first+'-'+middle+'-'+second

	# final output
	print (s,'becomes',h)	
else:
	print('Invalid Input')	
