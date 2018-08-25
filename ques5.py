a= input("enter string:")

import string

(x,y,z)=a.partition(a[0])
(l,m,n)=a.partition(a[-1])

print (m+z+y)
