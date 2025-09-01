def Euclidean(a,b):
    if (b==0):
        return a; 
    else:
        return Euclidean(b,(a % b))

a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))

if(a<b):
    a,b=b,a
    
print(Euclidean(a,b))
