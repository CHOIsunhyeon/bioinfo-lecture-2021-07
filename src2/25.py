#! usr/bin/python



#25~29


'''26
print(a[0::3])

for i in range(0,len(s),3):
    print(s[i]) 
'''

'''27
print(a[:3])
print(a[3:6])

print(a[6:])

for i in range(0,len(s),3): 
    print(s[i:i+3]) 
'''
'''포문처럼 일자로 만들어 나오게 하고 싶어요 
print(a[::-1])
for i in range(len(s)):
    print(f"{s[i]}{s_rev[i]}") 
'''
'''
#28
seq = 'ATGTTATAG'
comp_seq = ""
comp_data = {"A":"T","T":"A","C":"G","G","C"}
for s in seq:
    comp_seq += comp_data[s]
print(seq)
print(comp_seq) 

for i in range(len(seq)):
    s = seq[i]
    cs = comp_seq[i]
    bond = "&"
    if s == "A" or s == "T":
        bond = "="
    print(f"{s}{bond}{cs}")
#a =t g&c 이렇게 변함 
'''
'''
"C" in s
'''

seq1 = 'AGTTTATAG'
for i in range(len(seq1)):
    s =seq[i:i+2]
    print(i,s,s=="TT")

#간단
if seq1  == "TT":
    print(i)
