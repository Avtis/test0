import csv


with open('students.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    new_data = [['id', 'Name', 'titleProject_id', 'class', 'score']]
    for i in reader:
        try:
            new_data.append([str(int(i[0]) + 1), i[1], i[2], i[3], i[4]])
        except:
            pass

    with open('students2.csv', 'w+', encoding='utf-8', newline='') as out_csvfile:
        writer = csv.writer(out_csvfile)
        for row in new_data:
            writer.writerow(row)
with open('students2.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader2 = csv.reader(csvfile)
    for i in reader2:
        print(i)
