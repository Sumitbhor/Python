import csv
with open ("customers.csv", "w", newline="") as file :
    writer= csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "Mumbai"])
    writer.writerow(["Bob", 30, "Pune"])

