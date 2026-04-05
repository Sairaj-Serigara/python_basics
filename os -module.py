import os
if  not os.path.exists("data"):    #cretes folder named data
    os.mkdir("data")

for i in range(0,6):
        os.mkdir(f"data/day {i+1}")      #inside data cretes 6 folders