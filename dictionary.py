info={
    "name":"sai",
    "age":19
}
print(type(info),info)
print(info["name"])#throws error if value not present
print(info.get("name"))#does not throws error if value is not present

print(info.values())
print(info.keys())

for key in info:
    print(info[key])

print(info.items())

for key,value in info.items():
    print(f"the corresponding of {key} is {value}")