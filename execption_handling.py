# num=input("enter your number.")
# print(f"multiplication table of {num}")
# try:
#     for i in range(1,11):
#         print(f"{int(num)} x {i} = {int(num)*i}")
#
# except Exception as e :
#     print(e)
#     print("some error has occured")
#
# print("ended")
#here if we use any other type than int it shows the error msg  and executes remaining lines

try:
    num1=int(input("enter your number."))
    a=[6,3]
    print(a[num1])
except ValueError:
    print("Entered input is not an integer")
except IndexError:
    print("this is an index error")
