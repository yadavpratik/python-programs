#normal class declaration
#without constructor
'''class Example:
    #data memeber declaration
    #inside class data member no need self keyword while declaring
    a=10
    b=20
    c=30

    def num(self):
        print("a=",self.a)
        print("b=",self.b)
        print("c=",self.c)

e=Example()      #create object for assign temporary memory
e.num() '''     #acessing method of class

# =============================================================================================================================


#class with default constructor
'''class Example1:
    print("class run")
    a=10
    def __init__(self):    #constructor declaration
        print("cunstructor run ")

        #inside constructor we declare data member with self keyword
        self.a=10.1
        self.fname='pratik'
        self.lname='yadav'
        rollno=1020

    def my_name(self):      #method or member function 
        print("my name is:",self.fname ,""+ self.lname)


e1=Example1()
print("a from contructor :",e1.a)
print("a from class :",Example1.a)   #acess data memeber from class
e1.my_name()  '''     #access member function from class

# =============================================================================================================================

#class with paramaterized constructor
'''class Example2:
    def __init__(self,name,roll):
        self.n=name
        self.r=roll

    def data(self):
        print("name",self.n)
        print("roll=",self.r)


e2=Example2('pratik',102)     #passing arguments to paramaterized constructor
e2.data()'''

# =============================================================================================================================

#instance veriable
#instance variable could be decleare inside constructor,
#inside instance method(member function) and outside class
# example
'''class Example3:

    #instance variable inside constructor
    def __init__(self):
        self.name='pratik'      #instance variable declearation
        self.rollno=102
        self.branch='bscit'
        self.mob=9130410796

    #instance variable declare inside instance method or member function
    def info(self):
        self.emailid="p123@gmail.com"

e3=Example3()       

e3.info()           #first call member function to access instance variable declare inside it
print(e3.emailid)
e3.subject='python'  
print(e3.__dict__)'''

# =============================================================================================================================

#STATIC VARIABLE
#static variable has declare inside class and outside method or constructor
'''class Example5:

    clg='GH RAISONI UNIVERSITY' #static varaible

    def __init__(self):
        self.name='pratik' #instance variable
        Example5.branch='Bscit' #static variable
    
    def info(self):
        self.roll_no=103 #instance variable
        Example5.rollno=102 #static variable

        print('static rollno=',Example5.rollno)
        print("instance roll_no=",self.roll_no)

e5=Example5()
print(e5.clg)
print(Example5.clg)
print(e5.branch)
print(Example5.branch)
e5.info()
print(e5.rollno)'''

# =============================================================================================================================

#instance variable and static variable use
'''class Example4:
    clg='GH RAISONI UNIVERSITY' #static varaible

    def __init__(self):
        self.name='pratik' #instance variable
        

principal=Example4()
teacher=Example4()
student=Example4()


principal.clg='gh raisoni' #Static object can be change with obj 
print("principal",principal.clg,".....",principal.name)
print("teacher",teacher.clg,".....",teacher.name)
print("student",student.clg,".....",student.name)
print()

principal.name='pratik yadav' 
Example4.clg='GHRU'

print("principal",principal.clg,".....",principal.name)
print("teacher",teacher.clg,".....",teacher.name)
print("student",student.clg,".....",student.name)


a=Example4()
print("principal",a.clg,".....",a.name)'''


# =============================================================================================================================

#instancce, static and class method

'''class Example6:


    def __init__(self):
        self.name="pratik"
        print("this is constructor or also called as instance method")


    def instance_Method(self):
        print("the method which contain instance variable called as instance method")
        print(self.name)

    @staticmethod
    def staticmethods(fname,lname):
        print("this ia static method",fname+lname)
        print()

    @classmethod
    def classMethod():
        print("this is class method")

Example6.staticmethods('pratik','yadav')


e6=Example6()
e6.instance_Method()
e6.staticmethods('sagar','turkar')
e6.classMethod()'''

# =============================================================================================================================

#varible declaration and scope of assceesing variable 

'''class A():
    a=1
    
    print("this is class")
    def __init__(self):
        print("this is init constructor")
        self.num(5)
        self.b=2
        print(self.a)
        print(self.b)
        print(self.c)

    print("contructor called")
    print("a:",a)
    
    def num(self,d):
        print("this is num method :")
        self.c=d

    def nums(self):
        print("this is nums method ")
        print(self.a)
        print(self.c)
        print(self.c)

    
obj=A()
obj.nums()
obj.num(5)'''
# =============================================================================================================================
# Object Oriented Programing
# variables  in class are attributes
# Function in class are Methods

#dog class example
'''class Dog():

   def __init__(self,dog_breed,name,tail):
       self.dog_breed = dog_breed
       self.name = name
       self.tail = tail

my_dog = Dog(dog_breed= 'Hunter',name='shaka',tail='Tail')

print("dog breed :",my_dog.dog_breed)
print("name :",my_dog.name)
print("Tail :",my_dog.tail)'''



'''class Name():

   def __init__(self,name):
    print("my name is ",name)

my_name=Name(name="pratik")'''

# =============================================================================================================================

#car class example
'''class Car():
    """blueprint for car"""
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print(self.company,"started")

    def stop(self):
        print(self.company,"stopped")

    def accelarate(self):
        print(self.company,"accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print(self.company,"gear changed",gear_type)
        " gear related functionality here"

maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

print(maruthi_suzuki.color)
print(maruthi_suzuki.company)
maruthi_suzuki.start()
maruthi_suzuki.accelarate()
maruthi_suzuki.change_gear(2)
maruthi_suzuki.stop()
audi.start()
audi.change_gear(2)
audi.stop()'''

# =============================================================================================================================

'''class check:

    def __init__(self ,num):
        self.num1=num
        print("check class is created")


    def test1(self):
        print("this is test1 :")
        print(f"this is my {self.num1} class check")
        self.sum=self.num1+self.num1

    def test2(self,num2):
        print("this is test2 :")
        print(f"this is my {num2} class check")
        self.sum=num2+num2
            
c1=check(2)
c1.test1()
print(c1.sum)
c1.test2(4)
print(c1.sum)'''


# =============================================================================================================================
# class example
#student information collection with class
'''class Student:

    def __init__(self):
        self.fname=input("Enter first name :")
        self.lname=input("Enter last name :")
        self.Rollno=input("Enter Roll no :")
        self.course=input("Enter course :")
        self.clg=input("Enter college Name :")
        self.mob=input("Enter mobile number :")
        print()

    def display(self):
        print("your name :",self.fname,self.lname,sep=" ")
        print("Roll no :",self.Rollno)
        print("course name :",self.course)
        print("college name :",self.clg)
        print("Mobile number :")
        print()


s1=Student()
s1.display()
s2=Student()
s2.display()'''



#same example with with function
'''def student():
    fname=input("Enter first name :")
    lname=input("Enter last name :")
    Rollno=input("Enter Roll no :")
    course=input("Enter course :")
    clg=input("Enter college Name :")
    mob=input("Enter mobile number :")
    print()
    return fname,lname,Rollno,course,clg,mob

def display(fname,lname,Rollno,course,clg,mob):
    print("your name :",fname,lname,sep=" ")
    print("Roll no :",Rollno)
    print("course name :",course)
    print("college name :",clg)
    print("Mobile number :",mob)
    print()



fname,lname,Rollno,course,clg,mob=student()
display(fname,lname,Rollno,course,clg,mob)


fname,lname,Rollno,course,clg,mob=student()
display(fname,lname,Rollno,course,clg,mob)'''