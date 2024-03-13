import json
import csv

FOLDER_PATH = "files/"
book = {
    'title': '1984',
    "author": "George Orwell",
    "isbn": "453991-4343",
    "inner_id": "43hj4j3hj43"
}

file = open((FOLDER_PATH + "bookJson.json"), mode="w")  # mode is write

# write date into file:
json.dump(book, file, indent=4)
file.close()  # to close file

# read data from the file:
to_read_file = open((FOLDER_PATH + "bookJson.json"), mode="r")  # mode is read
loaded_data = json.load(fp=to_read_file)
print(type(loaded_data))  # type is dict
print(loaded_data)
to_read_file.close()

# CSV examples
rows = [['name', 'age', 'job'],
        ['John', 28, 'Doctor'],
        ["Michael", 35, 'Engineer'],
        ["Joanna", 22, 'Accounter']]
# write to csv
csv_write_file = open(FOLDER_PATH + "csvPersonas.csv", mode='w')
csv_writer = csv.writer(csv_write_file)
csv_writer.writerows(rows)
csv_write_file.close()

# read from csv
csv_read_file = open(FOLDER_PATH + "csvPersonas.csv", mode='r')
dict_reader = csv.DictReader(csv_read_file)

for row in dict_reader:
    # headers are excluded
    print(row['name'], row["age"], row["job"])

csv_read_file.close()

# add values to csv file
additional_rows = [
    {'name': 'Jack', 'age': 26, 'job': 'Homeless'},
    {'name': 'Rick', 'age': 16, 'job': 'Student'}
]
fields = ['name', 'age', 'job']

# autoclosable resource:
with open(FOLDER_PATH + "csvPersonas.csv", mode='a') as csv_add_file:  # "a" -> add mode
    dict_writer = csv.DictWriter(csv_add_file, fieldnames=fields)
    dict_writer.writerows(additional_rows)

with open(FOLDER_PATH + "csvPersonas.csv", mode='r') as csv_read_file:
    dict_reader = csv.DictReader(csv_read_file)
    for row in dict_reader:
        # headers are excluded
        print(row['name'], row["age"], row["job"])