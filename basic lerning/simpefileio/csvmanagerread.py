import csv


with open("customers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
