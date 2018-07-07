import pandas as pd

import matplotlib.pyplot as plt

#엑셀파일 열기 - xlrd 모듈 필요
df = pd.read_excel('mandoo_management.xlsx', sheet_name='Sheet1')

#칼럼 추가
df['근무시간'] = df['퇴근시간'] - df['출근시간']
#칼럼 추가
df['시간당 만두'] = df['만두생산'] / df['근무시간']
#특정 칼럼기준으로 정렬
df = df.sort_values(by=['시간당 만두', '근무시간'], ascending=[False, False])

#최종 DataFrame 확인
print(df)

#플롯 그리기
df['만두생산'].plot(kind='bar')
plt.show(block=True)





#엑셀로 쓰기 - openpyxl 모듈 필요
df.to_excel('result.xlsx', sheet_name = 'Sheet1')