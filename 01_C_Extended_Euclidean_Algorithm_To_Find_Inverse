a=int(input("Enter N"))
b=int(input("Enter number to find inverse in GF(N)"))

r1 = a
r2 = b

t1 = 0
t2 = 1

while(r2>0):
    q = int(r1/r2)

    r = r1-q*r2
    r1 = r2
    r2 = r

 

    t = t1-q*t2
    t1 = t2
    t2 = t

gcd = r1

t = t1

print("gcd is : ",gcd)

print("inverse is : ",t%a)

    
