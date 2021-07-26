set1={1,3,"pratik",'subhash',"nihal",'roshan',1,50.1,60.2,70.3}
print(set1)
print()

#OPERATION SHOULD BE PERFORM ON SET
# =============================================================================================================================

#ADD OBJECT IN SET
'''print("add oject by using add function :",end=" ")
set1.add(2)
print(set1)
print()'''
# =============================================================================================================================

#UPDATE FUNCTION
'''print("updating set ",end=" ")
set1.update([2, 3, 4])
print(set1)
print()'''
# =============================================================================================================================

#DISCARD FUNCTION
'''print("remove object '4' by using discard function :",end=" ")
set1.discard(4)
print(set1)
print()'''
# =============================================================================================================================

#REMOVE FUNCTION
'''print("remove object 'pratik' by using remove function :",end=" ")
set1.remove("pratik")
print(set1)
print()'''
# =============================================================================================================================

#POP FUNCTION
'''print("pop object :",set1.pop())
print("given set :",set1)
set1.pop()
print(set1)
print()'''
# =============================================================================================================================

#print lenth of list by using __len__() and len() function 
'''print("lenght of set by len() ",len(set1))
print("length of set by __len__() :",set1.__len__())     
print()'''

# =============================================================================================================================

# copy set 
'''print("copy set :")
set2=set1
print("set1 :",set1)
print("set2 :",set2)
print()'''
# =============================================================================================================================

#CLEAR SET 
'''print("clear set :",end=" ")
set1.clear()
print(set1)
print()'''
# =============================================================================================================================

#SETS CAN BE USED TO CARRY OUT MATHEMATICAL SET OPERATIONS
#LIKE UNION, INTERSECTION, DIFFERENCE AND SYMMETRIC DIFFERENCE. 
#WE CAN DO THIS WITH OPERATORS OR METHODS.

'''set1={1,3,"pratik",'subhash',"nihal",'roshan'}
set2={"'vishal'",'subhash','"Nikhil"',1,50.1,60.2,70.3}
tuple1=(4,)

print("set1 :",set1)
print("set2 :",set2)
print()'''


#UNION FUNCTION 
#NOTE:SIMILARLY WITH SET UNION(), IN LIST AND TUPLE WE USE CONCATINATION METHOD

'''print("UNION FUNCTION :") 
Union=set1.union(set2)   
print("union of two sets :",Union)

Union=set1.union(tuple1)                
print("union of set and tuple :",Union)       
print()

print("UNION OPERATOR (|) :")
Union=set1|set2                          
print(Union)
print()'''
# =============================================================================================================================
# Intersection function
#NOTE:Intersection of A and B is a set of elements that are common in both the sets.
#Intersection is performed using & operator. Same can be accomplished using the intersection() method.

'''print("INTERSECTION FUNCTION ")
INTER=set1.intersection(set2)
print("similar objects in sets : ",INTER)
print()

print("INTERSECTION OPERATOR (&): ")
INTER=set1&set2
print("similar objects in sets : ",INTER)      
print()'''                 

# =============================================================================================================================
# differnce function
# Difference of the set B from set A(A - B) is a set of elements that are only in A but not in B. 
# Similarly, B - A is a set of elements in B but not in A.
# Difference is performed using - operator. Same can be accomplished using the difference() method.

'''print("DIFFERENCE OF SET1 AND SET2\n")
print(" DIFFERENCE FUNCTION : ")
DIFF=set1.difference(set2)
print(" OBJECT PRESENT IN SET1 BUT NOT IN  SET2: ",DIFF)
print()

print(" DIFFERENCE OPERATOR (-):")
DIFF=set1-set2
print(" OBJECT PRESENT IN SET1 BUT NOT IN  SET2: ",DIFF)
print()

print("DIFFERENCE OF SET2 AND SET1")
print("  DIFFERENCE FUNCTION : ")
DIFF=set2.difference(set1)
print("  OBJECT PRESENT IN SET2 BUT NOT IN  SET1: ",DIFF)
print()


print("  DIFFERENCE OPERATOR (-): ")
DIFF=set2-set1
print("  OBJECT PRESENT IN SET2 BUT NOT IN  SET1: ",DIFF)
print()'''

# =============================================================================================================================
# symmetric_difference function
#Symmetric Difference of A and B is a set of elements in A and B but not in both (excluding the intersection).
#Symmetric difference is performed using {^} operator. 
#Same can be accomplished using the method symmetric_difference().

'''print("DIFFERENCE OF SETS BY USING SYMMETRIC_DIFFERENCE FUNCTION : ")
SYMM_DIFF=set1.symmetric_difference(set2)
print("OBJECT ARE NOT PRESENT IN BOTH SET: ",SYMM_DIFF)
print()

print("DIFFERENCE OF SETS BY USING SYMMETRIC_DIFFERENCE OPERATOR (^): ")
SYMM_DIFF=set1^set2
print("OBJECT ARE NOT PRESENT IN BOTH SET: ",SYMM_DIFF)
print()'''
