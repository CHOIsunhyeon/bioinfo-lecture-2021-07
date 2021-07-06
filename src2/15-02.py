#! usr/bin/python
import sys
if len(sys.argv) !=2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1) 

try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f"{err},ur input : {sys.argv[1]}")#->a를 넣을때 너 숫자가 아닌 문자라고 알려주는 문구를 적을 수 있다. 
    sys.exit(3) 


num = int(sys.argv[1])
try:

    res = 10 / num 
except ZeroDivisionError as err:
    print(err) 
    sys.exit(2) 


#echo $? 하면 오류 넘버가 나옴 3, 2 ->0이 나와야 정상 

#오류가 어떤게 나올지 예상문구를 미리 지정해주는 것

# 메인에 넣기 전에 2~3명이 어프로브를 눌어줘야 메인에 넣을 수있는 기능이 있음 

