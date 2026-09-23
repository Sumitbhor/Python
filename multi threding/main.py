#normal jindhagi
import time

def get_customer():
    print("Getting customer...")
    time.sleep(2)
    print("Customer received")


def get_policy():
    print("Getting policy...")
    time.sleep(2)
    print("Policy received")


def get_claims():
    print("Getting claims...")
    time.sleep(2)
    print("Claims received")


start = time.time()

get_customer()
get_policy()
get_claims()

end = time.time()

print(f"Total time: {end - start:.2f} seconds")