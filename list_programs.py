list1=[1,2,3,"pratik",'subhash',"nihal",'roshan',"'vishal'",'"Nikhil"',1,2,3,50.1,60.2,70.3] 
print("given list :",list1)
print()

# ADD OBJECT IN LIST WITH append() FUNCTION
'''
print("ADD objects 'yadav' in list")
list1.append("yadav")                   
print(list1)
print()'''

# =============================================================================================================================

# ADD OBJECT IN LIST WITH insert() FUNCTON
#INSERTING OBJECT AT PARTICAL INDEX NUMBER
'''print("inserting object 4 at index no 1:")
list1.insert(1,4)                       
print(list1)
print()'''

# =============================================================================================================================
 
#REMOVE OBJECT WITH remove() FUNCTION
'''print("remove object 'subhash' from list :")  
print("remove object by using remove function ")
print("befor using remove method list is:")
print(list1)            
print("after usimg remove method list is :")
list1.remove('subhash')
print(list1)
print()'''

# =============================================================================================================================

#REMEOVE OBJECT WITH pop() FUNCTION

'''print("remove object by using pop function ")
print("befor using pop list is:")
print(list1)
print("here we are deleting object presnt at index no 5 :",list1[5])
list1.pop(5)

print("after usimg pop list is :")
print(list1)'''

# =============================================================================================================================

#REPLACE  AT PERTICULAR INDEX NUMBER
'''print("replace object at particular index number : ")
print("befor replace index no 4 contain :",list1[4]) 
list1[4]="PRATIK"                       
print("after replace index no 4 contain :",list1[4])
print(list1)
print()'''

# =============================================================================================================================
#PRINT THE INDEX NUMBER OF ANY OBJECTS BY USING index() 

'''print("print index number of any object by using 'index()'  :")
print("index no of onject 1:",list1.index(1,0,18))              
print("index no of object 'yadav':",list1.index("yadav",0,18))        
print()'''

# =============================================================================================================================

# PRINT LENGTH OF LIST BY USING__len__()
'''print("print length of list :",list1.__len__())     
print()'''

# =============================================================================================================================

# copy list 
'''print("copy list :")
list2=list1
print(list1)
print(list2)
print()'''

# =============================================================================================================================

# count function in list
'''print("count object in list by count function :")
count=list1.count(1)
print("count of object 1 in list :",count)
print()'''

# =============================================================================================================================
# SORTING LIST
#sort function not suported both str and int  
#sorting should be perform on list if list contain only str value or only int value
'''s=list1.sort()
print(s)
print()'''
# =============================================================================================================================
# REVERSE LIST
#reverse function 
'''print("reverse list :")
list1.reverse()
print(list1)
print()'''

# =============================================================================================================================

#EXTEND METHOD      
#extend method is use to modify orginal list 
# we can extends list,tuple,set,frozenset with other list ,tuple, set and frozenset values

'''print("EXTEND METHOD : ")
dict1={"p":3,"l":5,"m":6.25,"n":8.90}
tuple1=("toupl1","tuple2","tuple3")
set1={"set1","set2","set3"}

print(type(dict1))
print(type(tuple1))
print(type(set1))

# EXTENE LIST WITH DICTONARY
list1.extend(dict1)
print("after extend dictonary :")
print(list1)

#EXTEND LIST WITH TUPLE 
list1.extend(tuple1)
print("after extend tuple :")
print(list1)

# EXTEND LIST WITH SET
list1.extend(set1)
print("after extend sets :")
print(list1)

set2=set1.union(list1)
print(set2)'''

# =============================================================================================================================

#CLEAR LIST
'''print("clear list :")
list1.clear()
print(list1)
print()'''

# =============================================================================================================================

# add objects using list comprehension

'''list1=[1,2,3,4,5,6,7,8,9,10]

print('-'*20)
new_list=[num for num in list1]
print(new_list)'''

#nested list comprehension

'''print('-'*20)
new_list=[[num for num in list1 if num%5==0 ] for x in range(2)]
print(new_list)'''

# =============================================================================================================================

list1=[1,2,3,"pratik",'subhash',"nihal",'roshan',"'vishal'",'"Nikhil"',1,2,3,50.1,60.2,70.3]
print(list1)

# STRING SLICING
'''print(list1[0:])     ,    
print(list1[:14])
print(list1[0:14])
print(list1[:])
print(list1[-1])'''

# =============================================================================================================================

#finding smalllst and second smallest,larget and second largest number from given list
'''num=[]
n=int(input("enter length :"))
for i in range(0,n):
    num.append(int(input("enter number  :")))    
   
print(num)
largest_num=max(num)
print("maximum no=",largest_num)

smallest_num=min(num)
print("default smallest num value=",smallest_num)


for i in range(0,n):
    if num[i]<largest_num and smallest_num!= num[i] :
        largest_num=num[i]
print("second smallest no=",largest_num)

for i in range(0,n):
    if num[i]>smallest_num and largest_num !=num [i]:
        smallest_num=num[i]
       
print("second maximum no=",smallest_num)'''


# =============================================================================================================================
# FIND STUDENT WITH low score by using list

'''Name=[]
Score=[]
Student=[]

n=int(input('ENTER THE NUMBER OF STUDENTS : '))
for i in range(0,n):
    name=input(f"\nEnter name of student{i+1}: ")
    Name.append(name)
    Score.append(float(input(f"enter score of {name} : ")))
    Student.append([Name[i],Score[i]])


for i in Student:
    print(i)

smallest_num=min(Score)
maximum_num=max(Score)

print(f"smallest score: {smallest_num} \nmaximum score: {maximum_num}")
for s in Score:
    if s<maximum_num and s!=smallest_num:
        maximum_num=s
second_small_num=maximum_num
print(f"second smallest score :{second_small_num}")

for nam,sc in Student:
    if sc==second_small_num:
        print('\nstudent name who score second smallest marks ',nam)'''

    
    
           