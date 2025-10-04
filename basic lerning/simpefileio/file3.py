import csv

class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def add_row(self, row):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def display_csv(self):
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


csv_file = CSVHandler("data1.csv")

while True:
    print("\nCSV Menu")
    print("1. Display CSV")
    print("2. Add Row")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        csv_file.display_csv()

    elif choice == "2":
        # Step 1: Take input from user
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")

        # Step 2: Store in an object (list in this case)
        row_obj = [name, age, city]

        # Step 3: Pass object to class method
        csv_file.add_row(row_obj)
        print("Row added successfully!")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")

