def check(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return True
            
                
x=check(int(input("ENTER THE NUMBER : ")))
if x:
    print("given number is not prime")
else:
    print("given number is prime ")
	

