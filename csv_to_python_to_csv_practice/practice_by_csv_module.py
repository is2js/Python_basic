from employee import Employee
import csv

#플러그인 깔고나서부터는,, 읽기시에만 utf-8인코딩 해주기..ㅠㅠ
f = open('employee_list_utf-8.csv', 'r', encoding='utf-8')
# lines = f.readlines()
lines = csv.reader(f)

employee_list = list()
i=0
for line in lines:
    if i>0:
        # info = line.split(',')
        # employee_list.append( Employee( info[0], int(info[1]), int(info[2]), int(info[3]) ))
        employee_list.append( Employee( line[0], int(line[1]), int(line[2]), int(line[3])) )
    i+=1
f.close()

csv_file = open('result.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# csv_file.write('이름, 출근시간, 퇴근시간, 시급, 근무시간, 일당\n')
csv_writer.writerow([ '이름', '출근시간', '퇴근시간', '시급', '근무시간', '일당'])
for e in employee_list:
    # csv_file.write('{}, {}, {}, {}, {}, {}\n'.format(
    #     e.name, e.work_start, e.work_finish, e.wage_per_hour, e.worked_hours(), e.wage_of_the_day()))
    csv_writer.writerow([
        e.name, e.work_start, e.work_finish, e.wage_per_hour, e.worked_hours(), e.wage_of_the_day()
    ])
csv_file.close()