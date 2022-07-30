import csv

data1 = []
data2 = []

with open("bright_stars.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data1.append(row)

with open("dwarf_stars.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data2.append(row)

headers1 = data1[0]
stars_data1 = data1[1:]

headers2 = data2[0]
stars_data2 = data2[1:]

headers = headers1+headers2
stars_data = stars_data1 + stars_data2

for index, data_row in enumerate(stars_data2):
    stars_data.append(stars_data1[1:]+stars_data2[1:])

with open("merged_dataset.csv", "a+") as h:
    csv_writer = csv.writer(h)
    csv_writer.writerow(headers)
    csv_writer.writerows(stars_data)

with open("merged_dataset.csv") as input, open("merged_dataset1.csv", "w", newline = '') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if(any(field.strip() for field in row)):
            writer.writerow(row)