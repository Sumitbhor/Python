#mentos jindhagi
import threading 
import time 

def get_customer():
    print("Getting customer")
    time.sleep(2)
    print("Customer received")

def get_policy():
    print("Getting policy...")
    time.sleep(2)
    print("policy received")

def get_claims():
    print("getting claims ....") 
    time.sleep(2)
    print("claims recevied") 

start = time.time()

t1 = threading.Thread(target = get_customer)
t2 = threading.Thread(target=get_policy)
t3 = threading.Thread(target= get_claims)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()

print(f"Total time: {end - start:.2f} seconds")