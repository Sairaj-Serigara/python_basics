x=int(input("Enter the value of x "))

match x:
    case 0:
        print("number is zero")

    case 1:
        print("number is one")

    case 2:
        print("number is graeter than 2")

    case _ if x%2==0:
        print("number is even")

#default
    case _:
        print("number is odd")

