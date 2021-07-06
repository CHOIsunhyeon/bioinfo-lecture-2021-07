#! usr/bin/python
#파일 없다는 오류 말고 오류를 핸들링하기 ! 
#없는 파일을 읽으려하면 filenotfoundeorror이 나오는데 
#없을 때 어떤 문구가 나오게 되는지 
#except 다른에러까지  못잡게 되서 꼭 구체화 시켜서 쓰는게 좋다 
import sys

#with (open("ahhaha.txt", 'r') as handle:

#    data = handle.readlines()

#print(data)


try:
    with open("ahhaha.txt",'r') as handle:
         data =handle.readlines()

except FileNotFoundError as err:
    print("파일이 엇음err") 
    sys.exit() 

print(data) 



