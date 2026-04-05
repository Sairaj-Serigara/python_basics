f=open("name.txt","r")
print(f)
text=f.read()
print(text)
f.close()


f1=open("name1.txt","w")
f1.write("hello world")
f1.close()


f1=open("name1.txt","a")
f1.write("good morning")
# f1.close()


with open("name1.txt","w"):#as f ...opens the file then closes it
    f1.write("good night")
#by using we can skip writing of close()