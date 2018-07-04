def wage_calculator(work_start, work_finish, wage_per_hour=7530):
    worked_hours = work_finish - work_start
    #노동법에 의해, 근무시간 조정
    if worked_hours >= 4:
        break_time = ( worked_hours // 4 ) * 0.5
        worked_hours = worked_hours - break_time
    wage = worked_hours * wage_per_hour
    return wage, worked_hours

print('만두가게 임금계산하는 프로그램')

#시급
wage_per_hour = 7530
#직원 리스트 -> for문에서는 range + len(리스트) 를 이용해서 접근
employee_list = ['추미애', '홍준표', '안철수', '유승민', '심상정']
#일 시작시간과 종료시간
work_start_list = [ 10, 9, 8, 9, 8 ]
work_finish_list = [ 13, 18, 17, 13, 14 ]


#for문 돌기전에 txt파일 열기
f = open( 'mandoo_wage.txt', 'w', encoding='utf-8')

for i in range(0, len(employee_list)):
    wage_of_the_day, worked_hours = wage_calculator(work_start_list[i],  work_finish_list[i], 8000)
    # txt파일 쓰는 것은 print자리에만 f.write로 바꿔주기 + 줄바꿈(\n) 달아주기
    f.write('{}님은 오늘 {}시간 근무했습니다. 일당은 {}원 입니다.\n'.format(
        employee_list[i], worked_hours, wage_of_the_day
    ))
#for문 끝나고나서 txt파일 닫기
f.close()

print('---- 코드 10,000줄 있다고 가정 ----')

#csv : comma separated values
csv_file = open('mandoo_wage_csv.csv', 'w')
#첫 줄, 칼럼명 미리 써놓기
csv_file.write('이름, 출근시간, 퇴근시간, 근무시간, 일당\n')
for i in range(0, len(employee_list)):
    wage_of_the_day, worked_hours = wage_calculator(work_start_list[i],  work_finish_list[i], 8000)
    csv_file.write('{}, {}, {}, {}, {}\n'.format(
        employee_list[i], work_start_list[i], work_finish_list[i], worked_hours, wage_of_the_day
    ))

csv_file.close()











