info={"name":"sai","age":18}
info.update({"name":"sairaj"})
info.update({"age":19})
print(info)

#s1.update(s2)

# info.popitem()    #removes last key value
# print(info)

del info["age"]
print(info)