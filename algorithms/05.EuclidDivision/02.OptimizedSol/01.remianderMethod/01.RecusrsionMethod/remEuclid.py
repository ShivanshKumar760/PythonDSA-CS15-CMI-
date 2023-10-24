def gcd(m,n):
    if m<n:
        m,n=n,m 
    if(m%n)==0:
        return(n)
    else:
        return(gcd(n,m%n))

m=int(input("Enter a number 1:"))
n=int(input("Enter a number 2:"))
print(gcd(m,n))
