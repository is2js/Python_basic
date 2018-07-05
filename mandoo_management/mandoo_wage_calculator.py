from employee import Employee
import csv


f = open('employee_list.csv', 'r')
lines = csv.reader(f)

#for문에 들어가기전에, 모든 인스턴스들을 관리할 리스트 생성
employee_list = list()

#for문에 들어가기전에, 첫 줄에서는 작업안하도록 매개변수 생성
i = 0

for line in lines:
    #첫줄에서는 작업안하도록 if문 걸어주기
    if i > 0:
        employee_list.append( Employee(line[0], int( line[1] ), int( line[2] ), int( line[3] )))
    #첫줄 작업안하도록 1단계식 띄워넘기
    i += 1
f.close()

#list를 확인할 때는, len()와, for문을 돌면서 각 요소들 확인
print( len(employee_list) )
for emp in employee_list:
    print(emp.name, emp.work_start, emp.work_finish, emp.worked_hours(), emp.wage_of_the_day())


#세부적으로 확인하는 for문을 그대로 활용해서, 파일 쓰기를 한다.
f_output = open('employee_result.csv', 'w', newline='')
csv_writer = csv.writer(f_output)
csv_writer.writerow(['이름', '출근시간', '퇴근시간', '시급', '근무시간', '일당'])
#확인 복붙 부분
for emp in employee_list:
    csv_writer.writerow([
        emp.name, emp.work_start, emp.work_finish, emp.wage_per_hour, emp.worked_hours(), emp.wage_of_the_day()
    ])
    # f_output.write( '{}, {}, {}, {}, {}, {}\n'.format(
    #     emp.name, emp.work_start, emp.work_finish, emp.wage_per_hour,emp.worked_hours(), emp.wage_of_the_day()))

f_output.close()