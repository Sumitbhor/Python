import csv
with open ("data1.csv", "w", newline="") as file :
    writer= csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "Mumbai"])
    writer.writerow(["Bob", 30, "Pune"])

with open("data1.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)