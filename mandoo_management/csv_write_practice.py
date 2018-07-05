import csv

f = open('output.csv', 'w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow( ['첫번째', '두번째', '세번째', '네번째'])
csv_writer.writerow( [1, 2, 3, 4])
f.close()