#operation could perform on file
#r  = read mode   -to only read  file
#w  = write file  -to only write in file
#a  = appned mode -to open existing file im append mode
#r+ = read and write mode - to perform both read and write in file
#w+ = write and read mode mode - to perform both read and write in file
#a+ =append file and read data from file
#x = it open a file in exclusive creation mode
#close() closed function

# =============================================================================================================================


#open file in differnt modes

#1 open file in r = only read mode
'''p=open("test1.txt","r")
print("name of file:",p.name)
print("file mode ",p.mode)
print(p.read())
print()
p.close()'''

# =============================================================================================================================

#2 open file in w = only write mode
# when we use 'w' mode it is override this text on already save text in file  
'''p=open("test.txt","w")
print("name of file:",p.name)
print("file mode ",p.mode)
f.write("write in file")
print("action perform")
print("readable :",f.readable())
print("writable :",f.writable())
print()
p.close()'''

# =============================================================================================================================


#3 open file in r+ = only read and write mode
#when we use 'r+' mode it does not override text 
# on already save text in file it start from after it.
'''p=open("test.txt","r+")
print("name of file:",p.name)
print("file mode ",p.mode)
print(p.read())
p.write("thank you")
print(p.read())
print("readable :",p.readable())
print("writable :",p.writable())
print()
p.close()'''

# =============================================================================================================================


#4 open file in w+ = only write and read mode 
#when we use 'w+' mode it overwrite text 
# on already save text in file it start from starting point.
#alway open blank file
'''p=open("test.txt","w+")
print("name of file:",p.name)
print("file mode ",p.mode)
p.write("write in file after long time  ")
print(p.read())
print("action perform")
print("readable :",p.readable())
print("writable :",p.writable())
print()
p.close()'''

# =============================================================================================================================


#5 open file in a= append mode
#cannot read file on write in file and cannot overwite
'''p=open("test.txt","a")
print("name of file:",p.name)
print("file mode ",p.mode)
f=open("test.txt","a")
f.write("hii hello")
f.close()
print()'''

# =============================================================================================================================

#6 open file in a+= append and read
#a+ mode always start from end point
'''p=open("test.txt","a+")
print("name of file:",p.name)
print("file mode ",p.mode)
print(p.read())
p.write("writing with  mode ")
print(p.read())
p.close()'''

# =============================================================================================================================

#7 open file in x = exclusive creation mode
'''p=open("test1. txt","x")
print("name of file:",p.name)
print("file mode ",p.mode)
p.write("using x mode for writing")
p.close()'''

# =============================================================================================================================


#in built functions

'''f=open("test.txt","r")
print(f.read())
print(f.readline()
print(f.readlines())
f.close()'''

# =============================================================================================================================


# 'with' keyword

'''with open("test.txt","r+") as f:
    print(f.read())
    print("current cursor position in file",f.tell())
    f.write("file open in w+ mode\n")
    print("current cursor position in file",f.tell())
    
    print("file close :",f.closed)
print("file closed :",f.closed)'''

# =============================================================================================================================

#checking eachnewline present in file
'''with open("test.txt","r+") as f:
    for i in range(1,11):
        l=len(f.readline())
        print("current position :",f.tell())
        f.seek(f.tell()-l-1)
        print(f.readline(),f"lenth of readline{i} :",l,)
        t=f.tell()
        f.seek(t)'''

# =============================================================================================================================

#binary file read
'''f1=open("shreeRam.jpg","rb")
img=f1.read()
f2=open("Ramji.jpg","wb")
f2.write(img)'''

# =============================================================================================================================

#woking with csv file

'''import csv
with open("Student_markshhet.csv","w") as f:
    a=csv.writer(f)
    a.writerow(["a","b","c","d","e"])
    print("row inserted ")'''
# =============================================================================================================================

#w=only write mode
# when we use 'w' mode it is override this text on already save text in file  
'''f=open("test.txt","w")

f.write("write in file")

print("action perform")

print("readable :",f.readable())
print("writable :",f.writable())

f.close()'''
# =============================================================================================================================

#r= only read file 
'''p=open("test.txt","r")
print("readable :",p.readable())
print("writable :",p.writable())
print(p.read())'''
# =============================================================================================================================

#r+ =read and write
#when we use 'r+' mode it does not override text 
# on already save text in file it start from after it.
'''p=open("test.txt","r+")
print(p.read())
p.write("thank you")
print("readable :",p.readable())
print("writable :",p.writable())
p.close()'''
# =============================================================================================================================

#w+ =write and read
#when we use 'w+' mode it overwrite text 
# on already save text in file it start from starting point.
'''f=open("test.txt","w+")
f.write("write in file after long time  ")
print(f.read())
print("action perform")
print("readable :",f.readable())
print("writable :",f.writable())
f.close()'''

# =============================================================================================================================

 
