class Employee:
    #계산식이 필요없는 단순 칼럼은 필드로 선언한다.
    name = None
    wage_per_hour = 7530
    work_start = None
    work_finish = None

    #생성자에는 상수를 제외하고 받았지만, None일 수 있지만, 대입도 되도록 해보자.
    #default값을 =None으로 주면 인자가 없을 시에는 필드인 self.wage_per_hour에 대입하는 식을 안적고
    #만약 인자가 주어진 경우, 어떤 값이라도 None이 아니므로 if wage_per_hour:라는 식으로 인식하여 필드에 대입시킨다.
    def __init__(self, name, work_start, work_finish, wage_per_hour = None):
        self.name = name
        self.work_start = work_start
        self.work_finish = work_finish
        if wage_per_hour:
            self.wage_per_hour = wage_per_hour

    #계산식이 필요한 칼럼(근무시간)은 함수로 정의한다.
    #노동법 준수를 위해 break_time 고려
    def worked_hours(self):
        worked_hours = self.work_finish - self.work_start
        if worked_hours >= 4:
            break_time = ( worked_hours // 4 ) * 0.5
            worked_hours = worked_hours - break_time
        return worked_hours

    #계산식에 또다른 계산식필요칼럼을 포함한 경우에는 함수안에서 함수를 호출할 수 있다.
    def wage_of_the_day(self):
        return self.worked_hours() * self.wage_per_hour

f = open('employee_list.csv', 'r')
lines = f.readlines()

#for문에 들어가기전에, 모든 인스턴스들을 관리할 리스트 생성
employee_list = list()

#for문에 들어가기전에, 첫 줄에서는 작업안하도록 매개변수 생성
i = 0

for line in lines:
    #첫줄에서는 작업안하도록 if문 걸어주기
    if i > 0:
        info = line.split(',')
        #csv파일을 읽어들이고 split으로 쪼개어놓으면 다 문자열로 인식된다.
        #name인자위치를 제외하고 모두 int()함수로 감싸주자.
        employee_list.append( Employee(info[0], int( info[1] ), int( info[2] ), int( info[3] )))
    #첫줄 작업안하도록 1단계식 띄워넘기
    i += 1
f.close()

#list를 확인할 때는, len()와, for문을 돌면서 각 요소들 확인
print( len(employee_list) )
for emp in employee_list:
    print(emp.name, emp.work_start, emp.work_finish, emp.worked_hours(), emp.wage_of_the_day())


#세부적으로 확인하는 for문을 그대로 활용해서, 파일 쓰기를 한다.
f_output = open('employee_result.csv', 'w')
f_output.write('이름, 출근시간, 퇴근시간, 시급, 근무시간, 일당\n')
#확인 복붙 부분
for emp in employee_list:
    f_output.write( '{}, {}, {}, {}, {}, {}\n'.format(
        emp.name, emp.work_start, emp.work_finish, emp.wage_per_hour,emp.worked_hours(), emp.wage_of_the_day()))

f_output.close()