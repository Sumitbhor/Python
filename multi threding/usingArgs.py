import threading
import time


def get_customer(customer_id):
    print(f"Getting customer {customer_id}")
    time.sleep(2)
    print(f"Customer {customer_id} received")


def get_policy(customer_id):
    print(f"Getting policies for customer {customer_id}")
    time.sleep(2)
    print(f"Policies for {customer_id} received")


def get_claims(customer_id):
    print(f"Getting claims for customer {customer_id}")
    time.sleep(2)
    print(f"Claims for {customer_id} received")


customer_id = 101

t1 = threading.Thread(
    target=get_customer,
    args=(customer_id,)
)

t2 = threading.Thread(
    target=get_policy,
    args=(customer_id,)
)

t3 = threading.Thread(
    target=get_claims,
    args=(customer_id,)
)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Dashboard data ready")