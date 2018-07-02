print('만두가게 임금 계산하는 프로그램') #파일 잘 생성되었나 확인용

name = '추미애'
work_start = 9
workd_finish = 18
worked = workd_finish - work_start
wage_per_hour = 7530

#노동법에 의해, worked가 4시간 이상시 마다, 30분의 휴게시간을 고려하는 if문
if worked >= 4:
    break_time = worked // 4 * 0.5
    worked = worked - break_time
    print('{}님은 {}시간 근무합니다. 오늘 일당은 {}원입니다.'.format(name, worked, worked * wage_per_hour))
    print('휴게시간은 {}시간입니다.'.format(break_time))
else:
    print('{}님은 {}시간 근무합니다. 오늘 일당은 {}원입니다.'.format(name,worked, worked * wage_per_hour))