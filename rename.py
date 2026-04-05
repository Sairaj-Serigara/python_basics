import os


#day 46


# for i in range(0,6):
#         os.rename(f"data/day {i+1}" ,f"data/tutorial {i+1}")   #renames day 1 to tutorial 1

folders=os.listdir("data")
# print(folders)

for folder in folders:
        print(folder)
        # print(os.getcwd())  #current dir
        #os.chdir("/user")    #change dir
        print(os.listdir(f"data/{folder}"))   #list the files inside data