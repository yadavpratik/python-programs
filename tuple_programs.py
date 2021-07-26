tuple1=(1,2,3,"pratik",'subhash',"nihal",'roshan',"'vishal'",'"Nikhil"',1,2,3,50.1,60.2,70.3)

print("given tuple :")
print(tuple1)
print()

# =============================================================================================================================

#OPERATION SHOULD BE PERFORM ON TUPLE

#print lenth of list by using __len__() and len() function 
'''print("lenght of tuple by len() ",len(tuple1))
print("length of tuple by __len__() :",tuple1.__len__())     
print()'''

# =============================================================================================================================


#index() use to print index number of any object in tuple
'''print("print index number of any object by using 'index()'  :")
print("index no of onject 1:",tuple1.index(1,0,18))              
print("index no of object 'yadav':",tuple1.index("yadav",0,18))        
print()'''

# =============================================================================================================================

# copy tuple 
'''print("copy tuple :")
tuple2=tuple1
print("tuple1 :",tuple1)
print("tuple2 :",tuple2)
print()'''

# =============================================================================================================================
#concatination by function and by operator
'''tuple2=(4,2,5)
print("concatination by operator :",tuple1+tuple2)
print("concatination by function :",tuple1.__add__(tuple2))
print()'''

# =============================================================================================================================


# count function in tuple
'''print("count element in tuple by count function :")
count=tuple1.count(1)
print("count of object 1 in tuple :",count)
print()'''

# =============================================================================================================================


#OPERATION SHOULD BE PERFORM ON TUPLE BY TYPECASTING IN LIST
list1=list(tuple1)

#ADD OBJECTS IN LIST
'''print("ADD objects 'yadav' in list")
list1.append("yadav")                   
print(tuple(list1))
print()'''

#INSERTING OBJECT AT PARTICAL INDEX NUMBER
'''print("inserting object 4 at index no 1:")
list1.insert(1,4)                       
print(tuple(list1))
print()'''

#REMOVE OBJECT FUNCTION
'''print("remove object 2 from list :")                
list1.remove(2)
print(tuple(list1))
print()'''

#REPLACE OBJECT AT PERTICULAR INDEX NUMBER in tuple
'''print("replace object at particular index number : ")
print("befor replace index no 4 contain :",list1[4]) 
list1[4]="PRATIK"                       
print("after replace index no 4 contain :",list1[4])
print(tuple(list1))
print()'''

#EXTEND METHOD
#extend method is use to modify orginal list we add any tuple,set,frozenset in list
'''print("EXTEND METHOD : ")
dict1={"p":3,"l":5,"m":6.25,"n":8.90}
tuple1=("toupl1","tuple2","tuple3")
set1={"set1","set2","set3"}

print(type(dict1))
print(type(tuple1))
print(type(set1))

list1.extend(dict1)
print("after extend dictonary :")
print(tuple(list1))
list1.extend(tuple1)
print("after extend tuple :")
print(tuple(list1))
list1.extend(set1)
print("after extend sets :")
print(tuple(list1))

print()'''


#CLEAR TUPLE
'''print("clear tuple :")
del(tuple1)
print(tuple1)
print()'''
