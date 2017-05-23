lenght = input("")
lenght2 = lenght.split(" ")
lenght3 = lenght.split(",")
lenght4 = lenght.split(".")
lenght5 = lenght.split(":")
a = " "
b = "Characters(including spaces):"
c = "Characters(excluding spaces):"
d = "Number of words:"
e = "Number of commas:"
f = "Number of periods:"
g = "Number of colons:"
print(b,len(lenght), c,len(lenght) - lenght.count(a), d,len(lenght2), e,len(lenght3) - 1, f,len(lenght4) - 1, g,len(lenght5) - 1)