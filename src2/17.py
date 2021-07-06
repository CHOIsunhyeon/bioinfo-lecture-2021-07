#! usr/bin/python

file_name = "write_sample.txt"
handel=open(file_name.txt,'w')

handle.write("Hello\n")

handle.write("biobinfomatics\n")
#\n을 붙여주지 않으면 마지막 글에 %이게 붙으니까 \n을 붙여주는게 좋다 
with open(file_name, 'a') as handle:
    handle.write("ken\n") 

#w:걍 다 처음부터 되는거 

#a: 이어서 써지는 것 

#csv
s = "s1,s2,s3" #csv$
#:set list하면 탭문자가 쳐진게 보임 
#space는 그냥 공백임 

print(s.split("\t")) #->리스트로 나옴 
print(data)  #['s1','s2','s3']리스트로 나옴 

#위에는 결과값이 리스트로 나오지만 아래는 그렇지 않다 
with open(file_name, 'a') as handle: #csv(컴마로 분리) ->tsv로 바꾸는 작업 tsv(탭으로 분리)  ->csv로 하려면 ","으로 만들면 된다. 
    handle.write("\t".join(data)+"\n") #->,,중간에 tap이 들어가 문자열을 만든다. **->s1 **s2 ** s3 이 된다. 


#:set nolist로 하면 $가 사라짐 

