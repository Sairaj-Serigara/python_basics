import os

if not os.path.exists("exercise_7"):
    os.mkdir("exercise_7")
    print("exercise_7  created")
#
#
# for i in range(1,10):
#     os.mkdir(f"exercise_7/{i}")
# print("exercise_7 created")

for i in range(1,10):
    os.rename(f"exercise_7/{i}",f"exercise_7/solution{i+1}")
print("solution{i+1} renamed")
