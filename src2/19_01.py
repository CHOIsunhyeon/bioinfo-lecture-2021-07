#! usr/bin/python

import sys
#값을 아무것도 안넣을때
#try:
#    val = int(input("Enter:"))
#except ValueError as err:
#    print(err)
#    sys.exit() 





#값이  0일 때 
#try:
#    print(10/val) 
#except ZeroDivisionError  as err:
#    print("err")
#    sys.exit()


#위 두개의 오류를 합치기 
try:
    val= int(input("Enter: "))
    print(10/val)
except ZeroDivisionError as err1:
    print(err1)
    sys.exit()
except ValueError as err2:
    print(err2)
    sys.exit() 

