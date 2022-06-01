def my_gen():
    """Un ejemplo de generadores"""

    print("helo world!")
    n = 0
    yield

    print("helo heaven!")
    n = 1
    yield

    print("helo hell!")
    n = 2
    yield

a = my_gen()
print(next(a)) #hello world!
print(next(a)) #hello heaven!
print(next(a)) #hello hell!
# print(next(a)) StopIteration


#Generator expression
my_list = [0, 1, 4, 7, 9, 10]

my_second_list = [x*2 for x in my_list] #list comprehension
my_second_gen = (x*2 for x in my_list) #generator expression
