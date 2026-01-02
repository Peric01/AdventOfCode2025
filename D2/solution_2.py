import re

invalid = 0
file = open("D2\input.txt", "r")
input = file.readline()
x = re.split(',', input)
for i in x:
    values = re.split('-', i)
    begin = int(values[0])
    end = int(values[1])
    while(begin<=end):
        s_begin = str(begin)
        
        begin +=1
print(invalid)