menu={"pizza":190,
      "burger":100,
      "coffee":50}
print(f"Welcome to our restaurant\nhere is the menu")
pizz_cost=190
bur_cost=100
coffee_cost=50
total=0
pizz_orders=[]
bur_orders=[]
coffee_orders=[]
pizz_quantities=[]
bur_quantities=[]
coffee_quantities=[]

while True:
    for item ,cost in menu.items():
        print(f" {item}    {cost}")
    order=input("enter your oder." ).lower()
    if order not in menu.keys():
        print("sorry that doesn't exist")
    else:
        quantity=int(input("enter your quantity."))
        print(f"{order} of quantity {quantity} is added")
        if order=="pizza":
            total = total + pizz_cost * quantity
            (pizz_orders.append(order))
            pizz_quantities.append(quantity)


        if order=="burger":
            total=total+bur_cost*quantity
            (bur_orders.append(order))
            bur_quantities.append(quantity)

        if order=="coffee":
            total=total+coffee_cost*quantity
            (coffee_orders.append(order))
            coffee_quantities.append(quantity)

        s=input("do you want to add other recipe  y/n").lower()
        if s=="n":
            break

print(pizz_orders,pizz_quantities)
print(bur_orders,bur_quantities)
print(coffee_orders,coffee_quantities)

print("total" ,total)
