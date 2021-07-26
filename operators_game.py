class operation():
    def Input(self):
        tuple1 = ("Arithmetic","comparison")
        self.op=[('+',"*","-",'/','//','%','**'),("==","!=","<=",">=","<",">")]


        self.a = int(input("\nEnter first  number : "))
        self.b = int(input("Enter second number : "))
        print("\nYour value are store in the variable a and b")
        print("a = ",self.a)
        print("b = ",self.b)

        print("\nDatatype of variables are : ")
        print("a = ",type(self.a))
        print("b = ",type(self.b))
        print("\nSELECT OPERTION ")
        self.Print(tuple1)
        
    def Print(self,value):
        self.value=value
        x=0
        for i in self.value:
            print("\t\t",x,":",i)
            x+=1
        self.n=int(input("chosse number :"))


    def arithmatic(self):
        print('\nSELECT OPERATOR ')
        self.Print(self.op[self.n])
        
        self.result=(
        self.a+self.b,
        self.a*self.b,
        self.a-self.b,
        self.a/self.b,
        self.a//self.b,
        self.a//self.b,
        self.a**self.b)

    def comparision(self):
        print('\nSELECT OPERATOR ')
        self.Print(self.op[self.n])
        
        self.result=(
        self.a==self.b,
        self.a!=self.b,
        self.a<=self.b,
        self.a>=self.b,
        self.a<self.b,
        self.a>self.b)

    
class run(operation):
    def runs(self):
        print('lets test all arithmatic and comparision operators with two integer number')
        self.Input()
        self.run()
  
    def run(self):
        if self.n==0:
            self.arithmatic()
        elif self.n==1:
            self.comparision()
        else:
            print("choose correct option :")

        for j in range(0,len(self.result)):
            if self.n==j:
                print("result =",self.result[j])
        
        choice=input('you want to continue [y/n]: ')
        if choice=='y':
            self.Input()
            self.run()
        else:
            exit()



obj=run()
obj.runs()
        


