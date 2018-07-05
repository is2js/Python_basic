class Employee:
    name = None
    work_start = None
    work_finish = None
    wage_per_hour = 7530

    def __init__(self, name, work_start, work_finish, wage_per_hour=None):
        self.name = name
        self.work_start = work_start
        self.work_finish = work_finish
        if wage_per_hour:
            self.wage_per_hour = wage_per_hour

    def worked_hours(self):
        return self.work_finish - self.work_start
    def wage_of_the_day(self):
        return self.worked_hours() * self.wage_per_hour

f = open('employee_list.csv', 'r')
lines = f.readlines()

employee_list = list()

i=0
for line in lines:
    if i>0:
        info = line.split(',')
        employee_list.append( Employee( info[0], int(info[1]), int(info[2]), int(info[3]) ))
    i+=1
f.close()

csv_file = open('result.csv', 'w')
csv_file.write('이름, 출근시간, 퇴근시간, 시급, 근무시간, 일당\n')
for e in employee_list:
    csv_file.write('{}, {}, {}, {}, {}, {}\n'.format(
        e.name, e.work_start, e.work_finish, e.wage_per_hour, e.worked_hours(), e.wage_of_the_day()))
csv_file.close()