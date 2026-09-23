class Customer:
    pass 

class Insurancepolicy:
    pass 


customer = Customer()
insurancepolicy = Insurancepolicy()

customer.insurancepolicy = insurancepolicy 

insurancepolicy.customer = customer 

del customer
del insurancepolicy 

import gc

print(gc.collect())