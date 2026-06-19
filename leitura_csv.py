import csv

with open('Mental Health Dataset.csv', mode='r') as f:
    dict_reader = csv.DictReader(f, delimiter = ' ')
    list_columns = dict_reader.fieldnames
    for row in list_columns:
        print(row)

