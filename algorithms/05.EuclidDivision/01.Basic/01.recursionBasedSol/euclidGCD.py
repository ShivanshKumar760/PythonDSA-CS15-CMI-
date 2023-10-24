def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        diff=m-n
        #diff>n ? possible case 
        return(gcd(max(n,diff),min(n,diff)))
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
print(gcd(m,n))

