#! usr/bin/python
#gzip 파일 읽기 
#gzip으로 압축 후 파일명이 gz이면 바로 읽히지 않음 
import gzip 

file_name= "covid19.fasta.gz"
data = dict() #data = {}


#with gzip.open(file_name,"rb") as handle: 라면 바이너리 파일이라 이상하게 나옴그래서 
with gzip.open(file_name, 'rt') as handle:
    for line in handle:
       #line = line.decode("utf-8")
        if line.startswith(">"):
            continue
    for base in line.strip():
        if base not in data:
            data[base] =0
        data[base] +=1

print(data) 
'''
#startswith (">") 
첫번째 줄을 검사했는데 >이걸로 시작을 하니까 continue로 해서 
for문으로 올라가서 두번째 라인부터 검사를 시작
또 마지막은 엔터가 쳐져있어서 line.strip으로 엔터를 날릴꺼
그럼 for문에 문자열 하나하나 넘어오게됨 
base는 a가 데이터에 들어있는가? 딕션너리가 빈거니까 안들어가 있음 
data[base] =0이 실행됨 그리고 그다음 data[base] +=1은 이미 들어가있는건 딕션너리에 밸류값 이 카운트되서 올라감 

'''

