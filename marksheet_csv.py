#function for getting input from user
#input=[ name,roll no,email,address,p1,p2,p3,p4,p5,total,percentage,result]
import csv
name=input("Enter name           :")
rollno=input("enter roll number  :")
emailid =input("Enter Emailid    :")
address=input("Enter your Address:")
p=[]

for i in range(1,6):
    m=float(input(f"enter mark of p{i} :"))
    p.append(m)
print(p)
total=sum(p)
print(total)
percent=total/5

for i in p:
    if i<40:
        result="Fail"
    else:
        result="Pass"

with open("Student_markshhet.csv","w") as f:
    a=csv.writer(f)
    a.writerow(['Name','Roll no','Email Id','Address','P1',
                'P2','P3','P4 ','P5','total','percentage','result'])
    
    print("row inserted ")
    a.writerow([name,rollno,emailid,address,p[0],p[1],p[2],p[3],p[4],
                total,f"{percent}%",result])
    
    print("value inserted ")

