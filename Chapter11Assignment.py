import re
handle = open('mbox-short.txt')
num=[]
for line in handle:
    num+=re.findall('[0-9]+',line)
num=list(map(int,num))
print(sum(num))
