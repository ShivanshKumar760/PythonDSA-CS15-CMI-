def gcd(m,n):
    i=min(m,n)
    while i>0:
        if (m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
print(f"The gcd of {m} and {n} is {gcd(m,n)}")
