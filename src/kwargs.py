def details(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("Your age is", kwargs.get("age"))
details(name="Nik", age=27, brain = "Huge")


# SIMPLE USE CASE FOR ORDERIGN PIZZA
def order(name, address, **toppings):
    print("Order is for: ", name)
    print("Ship it to: ", address)

    price = 11.00
    for key, value in toppings.items():
        price +=2
    print("Total price is: ", price)
    print(toppings)
    return price

my_order = order("Nik", "Lufthnasa", ham=True, cheese = True, sauce =True)

print(my_order)
