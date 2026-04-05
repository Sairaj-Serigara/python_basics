name=input("enter your name ")
print("Hello",name ,"welcome to kon banega karod pati");
count=0;

print("Round 1 :")
res1=int(input("Which planet is known as the Red Planet?\noptions\n1.A) Earth\n2.B) Venus\n3.C) Mars\n4.D) Jupiter\n"))
if(res1==1):
    print("wrong answer")
elif(res1==2):
    print("wrong answer")
elif(res1==3):
    print("right answer")
    count+=1;
else:
    print("wrong answer")
while count==1:
    res2=int(input("Who is known as the Missile Man of India ?\noptions\nA) Ratan Tata\nB) A. P. J. Abdul Kalam\nC) C. V. Raman\nD) Vikram Sarabhai\n"))
    if(res2==1):
        print("wrong answer")
        break;
    elif(res2==2):
        print("right answer")
        count+=1;
        break;
    elif(res2==3):
        print("wrong answer")
        break;
    else:
        print("wrong answer")
        break;
if(count==0):
    print("0")
elif(count==1):
    print("1")
else:
    print("sath caroddddd....")