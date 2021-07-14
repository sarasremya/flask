from csv2db import *

with open('data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    line_count = 0

    for row in csv_reader:
        if line_count!=0:
            result = insert2db(name=row[0], address=row[1], postcode=row[2], city=row[3], date=row[5], type=row[6], businessid=row[7])
            if result==False or result==None:
                print('Something went wrong!')
            else:
                print('Processed line number: %s' % line_count)
            
            line_count+=1

        else:
            line_count+=1

