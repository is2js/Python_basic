import pandas as pd

df = pd.read_excel('mandoo_management.xlsx', sheet_name='Sheet1')

#칼럼 추가
df['근무시간'] = df['퇴근시간'] - df['출근시간']
#칼럼 추가
df['시간당 만두'] = df['만두생산'] / df['근무시간']

df = df.sort_values(by=['시간당 만두', '근무시간'], ascending=[False, False])
print(df)

df.to_excel('result.xlsx', sheet_name = 'Sheet1')