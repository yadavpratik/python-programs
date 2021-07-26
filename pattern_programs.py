#print stars in right angle triangle
n=5

'''for i in  range(1,n+1):
    for j in range(1,1+i):
        print("*",end=" ")
    print()'''
# =============================================================================================================================
#simple star print

'''for i in range(1,n+1):
    print("*"*i)

# print name in star pattern
for i in range(1,n+1):
    print("pratik "*i)'''

# =============================================================================================================================

        
#print Daimond by right angle  triangle
'''for i in  range(1,n+1):
    print("-"*((n-i)*2),end=" ")
    for j in range(1,1+i):
        print(i,end=" ")

    for k in range(2,i+1):
        print(i,end=" ")

    print()


for i in  range(1,n+1):
    print("-"*((i-1)*2),end=" ")
    for j in range(1,n+2-i):
        print(i,end=" ")

    for k in range(2,n+2-i):
        print(i,end=" ")
    print()'''

# =============================================================================================================================

#print triangle as lower right angle triangle 
'''for i in  range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()'''
# =============================================================================================================================

#triangle
'''n=5
for i in range(1,n+1):
    print("-"*(n-i),end=" ")

    for j in range(1,i+1):
        print(i,end=" ")
    print()'''
# =============================================================================================================================
# lower triangle
'''m=5
for i in range(1,m):
    print("-"*i,end=" ")
    
    for j in range(1,m-i+1):
        print("*",end=" ")
    print("")'''

# =============================================================================================================================

# diamond
'''n=5
for k in range(1,n):
    print("-"*(n-k),end=" ")
    for l in range(1,k):
        print('*',end=" ")
    print()

for k in range(1,n):
    print("-"*k,end=" ")
    for l in range(1,n-k):
        print('*',end=" ")
    print()'''

# =============================================================================================================================
# printig number,alphabet * in triangle pattern
'''n=5

for i in range(1,n+1):
    print("-"*(i-1),end=" ")
    for j in range(1,n+2-i):
        print(i,end=" ")
    print()

for i in range(1,n+1):
    print("-"*(i-1),end=" ")
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()

for i in range(1,n+1):
    print("-"*(i-1),end=" ")
    for j in range(1,n+2-i):
        print(chr(64+i),end=" ")
    print()

for i in range(1,n+1):
    print("-"*(n-i),"*"*i,end=" ")
    print()'''

# =============================================================================================================================

#print aphabet in daimond pattern Diamond
'''import time
n=15
for i in range(1,n+1):
    print("-"*(n+1-i),end=" ")
    for j in range(1,i+1):
        time.sleep(1)
        print(chr(64+i),end=" ")
    print("-"*(n+1-i),end=" ")
    print()

for i in range(1,n+1):
    print("-"*i,end=" ")    
    for k in range(1,n-i+2):
        time.sleep(1)
        print(chr(69+k),end=" ")
    print("-"*i,end=" ") 
    print()'''

# =============================================================================================================================
# print box

def box(n):
    for i in range(1,n):
        for j in range(1,n):
            if i in range(2,n-1) and j in range(2,n-1):
                print(" ",end=" ")
                
            else:
                print("*",end=" ")
        print()

box(10)


print("="*50)
for i in range(1,20):
    print("="," "*46,"=")

print("="*50)
# =============================================================================================================================
