with open("seek.txt","r") as f:
    f.seek(10)   #start reading from here

    print(f.tell())   #tells from where reding starts
    data=f.read(5)  #from 10 next 5 bytes
    print(data)

with open("sample.txt","w") as f:
    f.write("hellooo world!!!")
    f.truncate(5)


with open("sample.txt","r") as f:
    print(f.read())
