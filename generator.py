#generator can be created using yield keyword.yield keyword returns a value from generator and suspends the execution of function untill
# the next value is requested.

def my_gen():
    for i in range (5):
        yield i

gen=my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


for j in my_gen():
    print(j)