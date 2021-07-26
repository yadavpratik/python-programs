#ALL ASCII VALUE

for i in range(1,257):
    char=chr(i)
    order=ord(char)
    print(char,end=" ")
    #print(order,"==",char)
# ==============================================================================================================

# FIND ASCII NUMBER FOR ALLPHABET
for char in range(1,300):
    alpha=chr(char)
    position=ord(alpha)
    
    if alpha>='a' and alpha<='z' :
        lower=alpha
        print(position,"-",lower)   

    elif alpha>='A' and alpha<='Z':
        upper=alpha
        print(position,"-",upper)

# PRINT ALPHA CHARACTER FROM ASCII
for char in range(1,300):
    if char>=65 and char<=90:
        print(char,"-",chr(char))
  
    if char>=97 and char <=122:
        print(char,"-",chr(char))
# =================================================================================================================================

# FIND ASCII VALUE OF NUMBERS 0-9
for char in range(1,300):
    number=chr(char)
    position=ord(number)

    for i in range(0,10):
        if number == str(i):
            print(position,"-",number)
            
# PRINT NUMBERS FROM ASCII VALUE
for char in range(1,300):
    if char>=48 and char <=57:
        print(char,"-",chr(char))


#=================================================================================================================================
#predict character Entered from keyboard is
#upeer case
#lower case 
#number 
#or special characters


#without using ASCII VALUE
enter_char=input("enter char:")

if enter_char >='a' and enter_char <='z':
    print("entered character from keyboard is lowercase alphabet:")

elif enter_char >='A' and enter_char<='Z':
    
    print("entered character from  keyboard is uppercase alphabet:")

elif enter_char >='0' and enter_char<='9':
    print("entered character from  keyboard is number:")

else:
    print("entered character from keyboard is special charachter:")


#with using ASCII VALUE
enter_char=input("enter char:")
for char in range(1,300):  
    if char>=65 and char <=90:
        upper=chr(char)
        if enter_char==upper:
            print("entered character from keyboard is upercase alphabet:")

    elif char>=97 and char <=122:
        lower=chr(char)
        if enter_char==lower:
            print("entered character from keyboard is lowercase alphabet:")
    
    elif char>=48 and char <=57:
        number=chr(char)
        if enter_char==chr(char):
            print("entered character from keyboard is number:")
    else:
        special_char=chr(char)
        if enter_char==special_char:
            print("entered character from keyboard is special charachter:")
# ======================================================================================================================================

#predict ASCII VALUE OF ENTERED CHARACHTER 


#without function
enter_char=input("enter char:")
for char in range(1,300):

    all_char=chr(char)

    if all_char >='a' and all_char <='z':
        lower=all_char
        if enter_char==lower:
            print(f"entered character from keyboard : {enter_char}")
            print(f"ASCII VALUE of {enter_char} :{char}")

    elif all_char >='A' and all_char<='Z':
        upper=all_char
        if enter_char==upper:
            print(f"entered character from keyboard : {enter_char}")
            print(f"ASCII VALUE of {enter_char} :{char}")

    elif all_char >='0' and all_char<='9':
        number=all_char
        if enter_char==number:
            print(f"entered character from keyboard : {enter_char}")
            print(f"ASCII VALUE of {enter_char} :{char}")

    else:
        special_char=all_char
        if enter_char==special_char:
            print(f"entered character from keyboard : {enter_char}")
            print(f"ASCII VALUE of {enter_char} :{char}")


#with function
enter_char = input()
value=ord(enter_char)
print(f"Entered Character from keyboard : {enter_char}")
print(f"ASCII VALUE of {enter_char} : {value}")


# ============================================================================================================================================