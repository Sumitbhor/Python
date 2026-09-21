from customer.service import ( create_customer,get_customer, update_customer )

from policy.service import (create_policy, get_policy)

from premium.service import (calculate_premium)

from claims.service import (create_claim, process_claim, get_claim_details, get_all_claim_details)


def customer_menu():

    while True:

        print("\n===== CUSTOMER MENU =====")

        print("1. Create Customer")
        print("2. Get Customer")
        print("3. Update Customer")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            create_customer()

        elif choice == "2":
            get_customer()

        elif choice == "3":
            update_customer()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def policy_menu():

    while True:

        print("\n===== POLICY MENU =====")

        print("1. Create Policy")
        print("2. Get Policy")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            create_policy()

        elif choice == "2":
            get_policy()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


def premium_menu():

    while True:

        print("\n===== PREMIUM MENU =====")

        print("1. Calculate Premium")
        print("2. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            sum_insured = float(
                input("Enter sum insured: ")
            )

            result = calculate_premium(sum_insured)

            print("\n===== PREMIUM DETAILS =====")

            print(
                f"Sum Insured : {result['sum_insured']}"
            )

            print(
                f"Premium     : {result['premium']}"
            )

            print(
                f"Tax         : {result['tax']}"
            )

            print(
                f"Total       : {result['total']}"
            )

        elif choice == "2":
            break

        else:
            print("Invalid choice.")


def claims_menu():

    while True:

        print("\n===== CLAIM MENU =====")

        print("1. Create Claim")
        print("2. Process Claim")
        print("3. Get Claim")
        print("4. Get All Claims")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            create_claim()

        elif choice == "2":
            process_claim()

        elif choice == "3":
            get_claim_details()

        elif choice == "4":
            get_all_claim_details()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def main():

    while True:

        print("\n")
        print("================================")
        print("       TFL INSURANCE SYSTEM")
        print("================================")

        print("1. Customer")
        print("2. Policy")
        print("3. Premium")
        print("4. Claims")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            policy_menu()

        elif choice == "3":
            premium_menu()

        elif choice == "4":
            claims_menu()

        elif choice == "5":

            print("Thank you for using TFL Insurance.")

            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()