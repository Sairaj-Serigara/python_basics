a="Sairaj"
b="!!Devadiga!!!"
c="Sairaj!! Devadiga  !!!"
print(a.upper())
print(a.lower())

print(b)
print(b.rstrip("!"))
print(b.lstrip("!"))

print(c.split(" "))

#capitalize changes the some silly errors like upper case or etc..
Heading="introduction To pYthon"
Heading1="introductiontopython"
print(Heading.capitalize())

#center
print(Heading.center(50))

#count
print(Heading.count("o"))

#endswith
print(Heading.endswith("on"))
print(Heading.endswith("ro",3,5))
print(Heading.startswith("in"))
print(Heading.endswith("in",3,5))

#find
print(Heading.find("on"))
print(Heading.find("ddd"))

#index
print(Heading.index("on"))

#alnum
#it may contians A-Z,a-z,0-9,and no puctuations like space or something
print(Heading1.isalnum())
print(Heading.isalnum())

#isalpha
print(Heading1.isalpha())

#islower
print(Heading1.islower())
print(Heading1.isupper())

#printable
name="MY name is sairaj"
name1="My name is sairaj\n"
print(name.isprintable())
print(name1.isprintable())

#isspace
space="  "
print(name.isspace())
print(space.isspace())

#title->first letter should be caps
title="Introduction To Pythonn"
title1="Introduction to Pythonn"
print(title.istitle())
print(title1.istitle())

#swapcase
print(title1.swapcase())

#title
print(title1.title())