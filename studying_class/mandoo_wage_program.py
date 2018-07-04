class Employee:
    name = '-'
    wage_per_hour = 7530
    work_start = None
    work_finish = None

    #클래스의 생성자
    def __init__(self, name, work_start, work_finish):
        self.name = name
        self.work_start = work_start
        self.work_finish = work_finish


    def worked_hours(self):
        return self.work_finish - self.work_start

    def wage_of_the_day(self):
        return self.worked_hours() * self.wage_per_hour


employee_list = []
employee_list.append( Employee( '조재성', 9, 18) )
employee_list.append( Employee( '추미애', 10, 17) )

f = open('employee_management.csv', 'w')
f.write('이름, 시급, 출근시간, 퇴근시간, 근무시간, 일당\n')
for e in employee_list:
    f.write('{}, {}, {}, {}, {}, {}\n'.format(
        e.name, e.wage_per_hour, e.work_start, e.work_finish,
        e.worked_hours(), e.wage_of_the_day()))
f.close()
