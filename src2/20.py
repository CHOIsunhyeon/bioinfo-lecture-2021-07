#! usr/bin/python



import sys
a =" Bio"
b =" Informatics "
c = a + b

print(c)  


'''

class A:
    def __init__(self):
        val=""


a1 =A() ->a1.val 출력하면 '' 나옴 
a2 =A() 

a1.val = "a" 
a2.val= "b"
두개의 val 끼리 합치고 싶다면 
a1.val + a2.val -> ab 하고 나옴 

'''

class A:
    def __init__(self,val):
       self.val =val
    def __add__(self,other):
        return self.val+other.val
    def __mul__(self,other):
        return "__mul__"


a1 = A("a")
a2 = A("b")

print(a1.val+a2.val)   #ab
print(a1 +  a2)  #a1기준으로 더하기를 했는데 self는 자신 othrer(a2) 
#a1 val. + a2 val이 되는 것 
print(a1 * a2) 








#def __div__ -> a1/a2 



 
