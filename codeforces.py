def res(a,b,c):
   return (a*b*c)/(b*b+c*b*2)
def dis(a,b,c,x):
   return (c*c+x*x)**0.5+((b+c)**2+(a-x)**2)**0.5
t=int(input())
while(t>0):
   t-=1
   a,b,c,x=map(int,input().split())
   m1=dis(a,b,c,res(a,b,c))
   m2=(x/100)*((a*a+b*b)**0.5)
   p=a-a*x/100
   q=b-b*x/100
   m3=dis(p,q,c,res(p,q,c))
   print(m1+m2+m3)