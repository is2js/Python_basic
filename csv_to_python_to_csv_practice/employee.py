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