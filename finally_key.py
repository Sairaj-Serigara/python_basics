try:
    l=[3,4,2,5]
    i=int(input("Enter an index "))
    print(l[i])
except :
    print("Some error has occured")

finally:
    print("this code always executes")
    print("nitj")

# print → just shows something on the screen.
#
# finally → ensures a block of code runs always, used for cleanup actions (like closing files, disconnecting
# from databases, etc.)
