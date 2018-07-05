import csv

#읽기 - 자동으로 split된 리스트로 가져옴
f = open('employee_list.csv', 'r')

lines = csv.reader(f)

for line in lines:
    print(line)

f.close()