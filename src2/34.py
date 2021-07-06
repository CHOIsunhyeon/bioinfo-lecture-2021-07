#!usr/bin/python

data = [3, 1, 1, 2, 0, 0, 2, 3, 3] 
#print(max(a))
#print(min(a))

cnt  =dict()

for elem  in data:
    if elem  not in cnt:
        cnt[elem] = 0
    cnt[elem] += 1
    
print(cnt)
