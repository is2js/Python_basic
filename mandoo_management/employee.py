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