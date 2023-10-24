def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if(m%i)==0 and (n%i)==0:
            mrcf=i
    return(mrcf)

hcf=gcd(18,25)
print(hcf)
