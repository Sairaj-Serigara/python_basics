# readline()
# f=open("file_method.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)


# writelines()
# f=open("file_method.txt","w")
# lines=["line1\n","line2\n","line3\n"]
# f.writelines(lines)
# f.close()


f=open("file_method.txt","r")
lines=["line11\n","line12\n","line13\n"]
for line in lines:
    print(line)
f.close()