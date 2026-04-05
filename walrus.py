# walrus(:=)--->allows you to assign a value to a variable within a expression
x=True
print(x:=False)
print("\t")

#normal method
# foods=list()
# while True:
#     food=input("what food do you like")
#     if food == "quite":
#         break
#     foods.append(food)

# with help of walrus
Food =list()
while (food :=input("what food do you like")) != "quite":
    Food.append(food)