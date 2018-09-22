a,b,c=(input("Enter 3 number in ascending order  ").split(" "))
f=int(a)
g=int(b)
h=int(c)
if(((g-f)==1 or (h-f)==1)) and ((g-f>=2 or h-f>=2)):
	print("True")
else:
	print("False")
i=int(round(float(a)/10.0)*10)
j=int(round(float(b)/10.0)*10)
k=int(round(float(c)/10.0)*10)
print(i+j+k)

