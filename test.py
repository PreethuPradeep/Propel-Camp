n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
if n1<n2:
    N=n1
else:
    N=n2
gcd=0

for n in range(2,N+1):
    if n1%n==0 and n2%n==0:
        if gcd<n:
            gcd=n
        else:
            break
    else:
        n+=1
print(gcd)