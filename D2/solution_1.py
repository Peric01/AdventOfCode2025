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
        check = str(begin)
        check_len = len(check)
        half_len = int(check_len/2)
        if not(check_len%2):
            if(check[:half_len] == check[half_len:]):
                invalid += begin
        begin +=1
print(invalid)