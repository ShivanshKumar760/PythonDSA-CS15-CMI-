def gcd(m,n):
    if m<n:
        m,n=n,m 
    while m%n!=0:
        m,n=(max(n,m-n),min(n,m-n))
    return n
print(gcd(18,25))
