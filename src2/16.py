#! usr/bin/python



#파일 읽기 
file_name = "read.sample.txt"

#강사님이 제일 좋아하는 방법
with open(file_name,"r") as handle:
    for line in handle:
        print(line.strip()) 
        #print(line, end=" ") 이방법도 있음 
#line에도 엔터가 들어가고 있고 
#print에도 엔터가 들어가 있음 
#strip는 원본에서 엔터를 날려버림 그래서 프린트하면 엔터쳐서 나온 것 처럼 됨 

#end해도 마찬가지로 나옴


#또다른 방법 

file_name = "read.sample.txt"

handle = open(file_name, "r")
#as를 쓰냐 안쓰냐 그리고 for에 대한 스페이스가 들어가느냐 안들어가느냐 
for line in handle:
    print(line.strip())
handle.close() 
#마지막에 close를 안써주면 문제가 생김 


#또또 다른 방법 

file_name = "read.sample.txt"

handle = open(file_name, "r")
lines = handle.readlines() #파일 오픈객체가 있는데 readlines를 쓰면 리스트 처럼 생긴게 나오고 for문에 넘기면 하나씩 넘겨지고 하나씩 나오게 됨 
for line in lines:
    print(line.strip())
handle.close()



#with 에 lines를 쓰는 방법 

with open(file_name, 'r') as handle:
    lines = handle.readlines()
    for line in lines:
        print(line.strip())
