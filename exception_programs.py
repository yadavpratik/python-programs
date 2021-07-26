#use of try and except block
'''a=int(input("enter the first no :"))
b=int(input("enter the second no :"))

print(a/b)'''



'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
    print(a/b)

except:
    print("enter the correct number ")'''

# =============================================================================================================================
#we can use except multiple times
'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
    print(a/b)

except ZeroDivisionError:
    print("number can not be divisible by zero")

except ValueError:
    print("plrase enter the integer number only number")'''

# =============================================================================================================================

#handling error show as messege
'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
    print(a/b)
except ZeroDivisionError as messege:
    print(messege)'''

# =============================================================================================================================

#handling multiple errors in one except block
'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
    print(a/b)

except(ValueError,ZeroDivisionError) as messege:
    print("enter the correct number ",messege)'''

# =============================================================================================================================

#concept of default except block execute only when we forgot about error or any error arrise
 
'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
    print(a/b)

except ZeroDivisionError as messege:
    print("enter the correct number ",messege)

except:
    print("you have done some wrong")'''

# =============================================================================================================================

#use of finally block
'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
    print(a/b)

except(ValueError,ZeroDivisionError) as messege:
    print("enter the correct number ",messege)

finally:
    print("all errors are handle")'''

# =============================================================================================================================

#use of else block
'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
    print(a/b)

except(ValueError,ZeroDivisionError) as messege:
    print("enter the correct number ",messege)

else:
    print("you are genius,you handle all the error")'''
# =============================================================================================================================


#nested try except block
'''try:
    a=int(input("enter the first no :"))
    b=int(input("enter the second no :"))
   
    try:
        print(a/b)
    except(ZeroDivisionError) as msg:
        print("number can't devide by zero",msg)
        
except(ValueError) as msg:
    print("enter the correct number ",msg)'''

# =============================================================================================================================
