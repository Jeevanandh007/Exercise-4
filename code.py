def f4(a,b,n):
  s=0
  i=1
  while i<n:
    if(i%a)==0 or (i%b)==0:
      s=s+i
    i=i+1
  return s

n=int(input("Enter n ")) 
a=int(input("Enter a "))
b=int(input("Enter b "))
s=f4(a,b,n)
print(s)

