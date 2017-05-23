okay = 1
Okay = okay

no = 2
No = no

bad = 3
Bad = bad

good = 4
Good = good

alright = 5
Alright = alright 

been_better = 6
Been_better = been_better

horrible = 7
Horrible = horrible

right = 2

rtd = int(raw_input("Roll the dice! Okay or No..."))

while right != 1:
    if rtd == 1:
        ran = int(raw_input("How are you?"))

        if ran == 1 or 2 or 3 or 4 or 5 or 6 or 7:
            die = 1 or 2 or 3 or 4 or 5 or 6
            right = 1
        else:
            print("I am afraid you did a typo or typed a wrong word. List of correct words:")
            print "Good"
            print "Bad"
            print "Alright"
            print "Okay"
            print "Been_better"
            print "Horrible"
        die = die / 2 * 4 + 2 / 2 
        if die > 6:
            die = die / 3
    
print ("Dice roll is... ") 
print str(die)