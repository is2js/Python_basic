#txt는 utf-8인코딩을 직접 해줘야 한글이 안깨진다.
f = open( 'first.txt', 'w', encoding='utf-8')
f.write('hello world\n')
f.write('hello File\n')
f.write('한글도 출력하고 싶어요.')
f.close()

#csv : comma separated values
#csv는 utf-8인코딩시에 엑셀에서 깨져버린다.
csv_file = open('csv_test_file.csv', 'w')
csv_file.write('1, 3, 5\n')
csv_file.write('7, 9, 11')
csv_file.close()
