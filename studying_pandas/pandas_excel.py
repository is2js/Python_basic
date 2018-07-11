import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager

#matplotlib의 폰트를 지정해주는 방법
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)


#엑셀파일 열기 - xlrd 모듈 필요
df = pd.read_excel('mandoo_management.xlsx', sheet_name='Sheet1')

#칼럼 추가
df['근무시간'] = df['퇴근시간'] - df['출근시간']
#칼럼 추가
df['시간당 만두'] = df['만두생산'] / df['근무시간']
#특정 칼럼기준으로 정렬
df = df.sort_values(by=['시간당 만두', '근무시간'], ascending=[False, False])

#최종 DataFrame 확인
# print(df)
#DF의 이름열-> INDEX로 옮긴다.
df = df.set_index('이름')
#print(df)
#플롯 그리기
df['만두생산'].plot(kind='bar')
print(df['만두생산'])
#플롯 저장하기는 반드시 plt.show로 띄우기전에 먼저 저장하기!
plt.savefig('만두생산.png')
#플롯 띄우기
plt.show(block=True)






#엑셀로 쓰기 - openpyxl 모듈 필요
df.to_excel('result.xlsx', sheet_name = 'Sheet1')