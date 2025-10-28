products = [
    {"name": "Laptop", "price": 60000, "rating": 4.5},
    {"name": "Headphones", "price": 1500, "rating": 4.0},
    {"name": "Keyboard", "price": 700, "rating": 3.8},
    {"name": "Mouse", "price": 400, "rating": 4.2},
    {"name": "Monitor", "price": 12000, "rating": 4.7}
]

'''discounted_prices=list(map(lambda currentProduct: {**currentProduct,"price":currentProduct["price"]*0.9 },products))
print (discounted_prices)   

updatedrating=list(map(lambda p:{**p, "rating": p["rating"]*2 },products))
print (updatedrating)
premium= list(filter( lambda p : p["price"]>5000,products))
print(premium)'''
print()

premium= list(map( lambda p : p["price"]>5000,products))
print(premium)
print()