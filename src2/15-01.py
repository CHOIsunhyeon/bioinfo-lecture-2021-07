#! usr/bin/python
import sys
if len(sys.argv) !=2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1) 

num = int(sys.argv[1])
try:
    res = a
except ZeroDivisionError as err:
    print(err) 
#오류가 어떤게 나올지 예상문구를 미리 지정해주는 것 ?
