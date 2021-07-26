'''def Hello():  #function called or function creation 
    print("HELLO")
Hello()       #function calling '''


#function with parameters
'''def add(a,b):
    e=a+b         #local variable
    print(e)
add(10,10)'''


# =============================================================================================================================

#function with return keyword
'''def Add(a,b):
    return a+b
print(Add(10,10))'''
    
# =============================================================================================================================

#function wth global keyword
'''def Add(a,b):
    global e     #global variable 
    e=a+b
    return e
Add(10,10)
print(e)    #by global key word we can access "e" anywhere in program'''

# =============================================================================================================================

#function with default value
'''def Add(a=10,b=10,c=10):   #parameters assign default value
    print("a =",a,end=" ")
    print("b =",b,end=" ")
    print("c =",c)
    print()
    return a,b,c

Add(1,2,3)  #calling a function with diffrent value
Add(a=20,b=20,c=20)
Add(20.5,20.5,c=20.5)
Add("Pratik","Murlidhar","Yadav") #passing argument in sequence,#assign in sequence as a,b,c
Add(c="yadav",a=20,b="pratik") '''

# =============================================================================================================================

#returning multiple values
'''def Add(a=10,b=10,c=10):   #parameters assign default value
    
    return a,b,c

a,b,c=Add("pratik",20.5,10000.5)
print("a=",a,"\nb=",b,"\nc=",c)'''


# =============================================================================================================================
# student ,teacher registeration

'''def get_input():
    print("Enter you details :")
    fname = input("Enter the first name :")
    lname = input("Enter the last  name :")

    return fname,lname
    
def register():
    
    def as_student():
        print("Register as student :")
        get_input()
        print("You successfully register as student ")

    def as_teacher():
        print("Register as teacher:")
        get_input()
        print("You successfully register as teacher ")

    print("""Register as 
        1:Student
        2:Teacher"""
         )
    n=int(input("choose option :"))
    if n==1:
        as_student()
    elif n==2:
        as_teacher()
    else:
        print("choose correct option")

register()'''



# =============================================================================================================================

'''def name_fun():
    print("function crated")
    return 'function return '
name_fun()
result=name_fun()
print(result)'''
# =============================================================================================================================


#function doc string used for writing code description
'''def name_fun():
    """function doc string used for writing code description """

    print("function crated")
    return 'function return '
name_fun()
result=name_fun()
print(result)
help(name_fun)'''

# =============================================================================================================================

'''def calculation(a,b):
    def add():
        return a+b
    def sub():
        return a-b

    if a>b:
        result=add()
        print(result)
    else:
        result=sub()
        print(result)'''

# =============================================================================================================================

# kwargs keword
'''def new_fun(**kwargs):
    print(kwargs)
    if 'nihal' in kwargs:
        print("roll no of nihal ",format(kwargs['nihal']))
    else:
        print("invalid input")

new_fun(pratik=123,nihal=143)'''


# =============================================================================================================================

#genrator function

'''def myname():
    yield 'pratik'
    yield 'yadav'

output=myname()
print(type(output))
print(next(output))
print(next(output))'''

# =============================================================================================================================
#lamda function
#sometimes we can declare a funtion without name such type of
#nameless function are called anonymous function or lamda function


'''s=lambda n:n*n 
print(s(4))

a=lambda a,b:a+b
print(a(4,5))

#with normal function
def even(n):
    if n%2==0:
        return True
    else:
        return False

l=[1,4,3,6,7]

print(list(filter(even,l)))

#with lamda function
print(list(filter(lambda X:X%2==0,l)))'''

# =============================================================================================================================

# Recursive function
#function that calls itself is called Recursive function

#use:
#We can reduce the length of code and improve readability
#We can solve complex problem very easily 

#example
'''def factorial(num=1):
    if num==0:
        facto=1
    else:
        facto=num*factorial(num-1)
    return facto

print("Factorial of 10 :",factorial(10))'''

