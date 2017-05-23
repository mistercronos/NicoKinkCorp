thing = input("Enter at least 3 words seperated by spaces ")
some = thing.split(" ")
x = 1
a = 'Whatever you wrote was'
b = 'in the opposite order.'
if some[-1] == 1:
    print ("Hello")
elif some[-2] == 2:
    print("Hello again")
else:
    print("I don't appreciate what you are doing")
print(a, some[-x], some[-2], some[-3], b)
