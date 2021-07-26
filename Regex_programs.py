# what is regular Expression ?
#   1. The regular expressions can be defined as the sequence of characters 
#      which are used to search for a pattern in a string.
#   
#   2. The module re provides the support to use regex in the python program. 
#   3. The re module throws an exception if there is some error while using the regular expression.



# To understand the RE analogy, MetaCharacters are useful, important and will be used in functions of module re. 
# There are a total of 14 metacharacters and will be discussed as they follow into functions: 

#   \   Used to drop the special meaning of character following it 
#   []  Represent a character class
#   ^   Matches the beginning
#   $   Matches the end
#   .   Matches any character except newline
#   ?   Matches zero or one occurrence.
#   |   Means OR (Matches with any of the characters separated by it.
#   *   Any number of occurrences (including 0 occurrences)
#   +   One or more occurrences
#   {}  Indicate number of occurrences of a preceding RE to match.
#   ()  Enclose a group of REs



#  Import the re module

from os import name
import re

# basic finctions available in re module
# re.match()
# re.compile()
# re.findall()
# re.finditer()
# re.fullmatch()
# re.escape()
# re.search()
# re.split()
# re.sub()
# re.subn()

# Function compile() 
#  Regular expressions are compiled into pattern objects,
#  which have methods for various operations such as searching for pattern 
#  matches or performing string substitutions. 
 
p='''
Regular expressions are compiled into pattern objects,
which have methods for various operations such as searching for pattern 
matches or performing string substitutions. 
'''

# =============================================================================================================================

name='Pratik @3$%^&*()yadav pratik 11111 22222 33333'

# '''FINDALL FUNCTION '''
'''find=re.findall('\w',name)   #find all alphanumerric charachter in present complete string
print(find)

find=re.findall('\W',name)   #find all character Except alphanumerric charachter present in complete string
print(find)

find=re.findall('\d',name)   #find only digits present in complete string
print(find)

find=re.findall('\D',name)   #find all character Except digits present in complete string
print(find)

find=re.findall('\s',name)     #find all spaces present in complete string
print(find)

find=re.findall('\S',name)     #find all character Except spaces present in complete string
print(find)

find=re.findall('\A',name)
print(find)

find=re.findall('\Z',name)
print(find)

find=re.findall('\b',name)
print(find)

find=re.findall('\B',name)
print(find)'''

# =============================================================================================================================

# ''' SEARCH FUNCTION '''
name='@$%^&*()yadav pratik 11111 22222 33333'
'''Search=re.search('\w',name)
print(Search)

Search=re.search('\W',name)
print(Search)

Search=re.search('\d',name)
print(Search)

Search=re.search('\D',name)
print(Search)

Search=re.search('\s',name)
print(Search)

Search=re.search('\S',name)
print(Search)

Search=re.search('\A',name)
print(Search)

Search=re.search('\Z',name)
print(Search)

Search=re.search('\b',name)
print(Search)

Search=re.search('\B',name)
print(Search)'''

# =============================================================================================================================

# ''' MATCH FUNCTION '''
'''name='yadav pratik 11111 22222 33333'
obj=re.compile('[yadav]',re.I)
print(obj.match(name))


matchs=re.match('\W',name)
print(matchs)

matchs=re.match('\d',name)
print(matchs)

matchs=re.match('\D',name)
print(matchs)

matchs=re.match('\s',name)
print(matchs)

matchs=re.match('\S',name)
print(matchs)

matchs=re.match('\A',name)
print(matchs)

matchs=re.match('\Z',name)
print(matchs)

matchs=re.match('\b',name)
print(matchs)

matchs=re.match('\B',name)
print(matchs)'''



# =============================================================================================================================
# reggex examples

'''def validation():
    miss =0
    if re.findall('\W',name):
        if not re.findall('\s',name):
            miss=1

    if re.findall("[0-9]",name):
        miss=1


    if miss==0:
        print('valid name')
    else:
        print('invalid name')'''

# =============================================================================================================================
# password validation

'''from stdiomask import getpass

def create_password():
    print("\n\t--------Create Password--------\n")
    miss=0
    Pass  = getpass(" ENTER PASWWORD   :")
    Pass=paswword_validate(Pass)
    cpass = getpass("\n CONFIRM PASWWORD :")
    cpass=paswword_validate(Pass)
    if Pass==cpass:
        print("\n\t---Pasword  Created Sucessfully---")
    else:
        print("\n","-"*40)
        print("\t-----PASWWORD DID NOT MATCH----")
        print("\t\tTRY AGAIN :")
        Pass=create_password()

    return Pass

def paswword_validate(Pass):
    if not len(Pass)>=8:
        print('\nPassword lenth must be eight character or more')
        miss=1

    if re.search('\s',Pass):
        print("\nPassword not cotain any space ")
        miss=1
        
    if not re.search('[a-z]',Pass):
        print("\npassword must contains atleast one lowercase letters")
        miss=1
    if not re.search('[A-Z]',Pass):
        print("\npassword must contains atleast one uppercase letters")
        miss=1
    if not re.search('[0-9]',Pass):
        print("\npassword must contains atleast one digits")
        miss=1
    if not re.search('[@]',Pass):
        print("\nPassword must contains only '@' special symbols")
        miss=1

    if miss==0:
        return True'''
    
# =============================================================================================================================

# name string validation
'''def names_validation():
    miss =0
    name=input("\nENTER NAME              : ")

    if re.findall('\W',name):
        if not re.findall('\s[A-Za-z]',name):
            miss=1
    if re.findall("[0-9]",name):
        miss=1

    if name!='' and miss==0 :
        print('valid name ')

    else:
        print('invalid name')
        print("\nEnter again :")
        name=names_validation()
    return name'''
# =============================================================================================================================
# mobile number validation

'''def mob_validate():
    miss=0
    
    mob=input("\nENTER MOBILE NUMBER     : ")
    if not re.findall('\D',mob):
        if len(mob)==10:
            print("valid number ")
        else:
            print("\nmobile number must contain 10 digit")    
            mob=mob_validate()
    else:
        print("\nEnter mobile number in digits only")
        mob=mob_validate()

    return mob'''

# =============================================================================================================================
# email validation
'''import validate_email

def email_validation():
         
    mail=input("\nENTER EMAIL ID          : ")

    if validate_email(mail):
        print("Valid Email")
    else:
        print("Invalid Email")
        print("\nEnter again :")
        mail=email_validation()

    return mail'''


# =============================================================================================================================