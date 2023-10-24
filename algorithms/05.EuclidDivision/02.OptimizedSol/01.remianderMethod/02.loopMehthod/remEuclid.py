def gcd(m,n):
    if m<n:
        m,n=n,m 
    while(m%n)!=0:
        m,n=n,m%n 
    return n 

m=int(input("Enter The first number :"))
n=int(input("Enter The second number :"))
print(gcd(m,n))
