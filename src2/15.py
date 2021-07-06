#! usr/bin/python
import sys 
sample =sys.argv[1] 
 #sys.argv는 리스트임 

print(f"processing: {sample}")
##처리 분석 
print(f"end: {sample}")  


#[0]은 py가 들어가있고 
#[1]은 비어 있어서 지금  인덱스 에러가 날꺼임 

#그래서 설명서를 만들어보자 

if len (sys.argv) != 2:
    print(f"python {sys.argv[0]} [sample]")
    sys.exit() #->오류보다는 샘플 이름을 넣으라고 문구가 뜸
#이게 맨 위로 올라가야함 

#sys.exit(1)

#echoi $? ->0이 아니면 모두 비정상 코드인데 1번으로 종료된거면 아규먼트 안맞아서 종료 이런식으로 만들어줄 수 있음 

