letter="heyy my name is {} and Im from {}"
name="Sairaj"
country="India"
print(letter.format(name,country))

letter1="my name is {1} and Im from {0}"
name1=("name")
country1="Russia"
print(letter1.format(country1,name1))

#or
print(f"my name is {name} and Im from {country} ")

txt="price is {price:.2f}"
print(txt.format(price=0.49999))

price1=99.09999
print(f"price is {price1:.2f}")

print(f"my name is {{name}} and Im from {{country}}")