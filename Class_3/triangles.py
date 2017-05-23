print "Hey! You look like you didn't learn your math lessons! How about I tell you what your triangle is? Good!"
ic = input ("I am going to ask you measurments. I need to know if you are going to measure in inches or in centimeters. (Type 1 for INCHES and/or 2 for CENTIMETERS)")
if ic == 1:
    side1 = input ("Now secondly i'm going to ask you the lenght of the first side of your triangle. Only type the number, so if it's 3 inches, tell me 3.")
elif ic == 2:
     side1 = input ("Now secondly i'm going to ask you the lenght of the first side of your triangle. Only type the number, so if it's 3 centimeters, tell me 3.")
side2 = input ("So. Same thing just this time I would like you to give the lenght of the second side.")
side3 = input ("One last time but with the third side.")
happy = 1
while happy == 1:
    rec = input ("Now I need to know. Does your triangle contain a right angle?(Type 1 for YES and/or 2 for NO)")
    if rec == 1:
        print ("Your triangle is a 'right triangle'");
        happy = 2
    elif rec == 2:
        print "Solving"
        happy = 2
    elif rec != 1:
        if rec != 2:
            print "That was not an option. Please enter a valid option."
if side1 != side2:
    if side2 != side3:
        print "Your triangle is 'scalene'"
    elif side2 == side3:
        print "Your triangle is 'isoscele'"
elif side1 == side2:
    if side2 == side3:
        print "Your triangle is 'equilateral'"
    elif side2 != side3:
        print "Your triangle is 'equilateral'"
elif side1 == side3:
    if side1 != side2:
        print "Your triangle is 'isoscele'"
    elif side1 == side2:
        print "Your triangle is 'equilateral'"