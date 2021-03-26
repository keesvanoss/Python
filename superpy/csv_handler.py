import csv

with open('employee_birthday.txt', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
