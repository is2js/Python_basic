f = open( 'first.txt', 'w', encoding='utf-8')
f.write('hello world\n')
f.write('hello File\n')
f.write('한글도 출력하고 싶어요.')
f.close()

#csv : comma separated values
csv_file = open('csv_test_file.csv', 'w', encoding='utf-8')
csv_file.write('1, 3, 5\n')
csv_file.write('7, 9, 11')
csv_file.close()
