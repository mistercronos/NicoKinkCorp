lol = 1
donegrades = 0
while lol == 1:
    numofgrades = input("Enter the number of grades you would like to calculate the mean of ")
#Grade 1
    grade1 = input("Enter grade ")
    donegrades = donegrades + 1
    if donegrades == numofgrades:
        lol = 2
    elif donegrades != numofgrades:
#Grade 2
        grade2 = input("Enter grade ")
        donegrades = donegrades + 1
        if donegrades == numofgrades:
            lol = 2
        elif donegrades != numofgrades:
#Grade 3
            grade3 = input("Enter grade ")
            donegrades = donegrades + 1
            if donegrades == numofgrades:
                lol = 2
            elif donegrades != numofgrades:
#Grade 4
                grade4 = input("Enter grade ")
                donegrades = donegrades + 1
                if donegrades == numofgrades:
                    lol = 2
                elif donegrades != numofgrades:
#Grade 5    
                    grade5 = input("Enter grade ")
                    donegrades = donegrades + 1
                    if donegrades == numofgrades:
                        lol = 2
                    elif donegrades != numofgrades:
#Grade 6    
                        grade6 = input("Enter grade ")
                        donegrades = donegrades + 1
                        if donegrades == numofgrades:
                            lol = 2
                        elif donegrades != numofgrades:
#Grade 7
                            grade7 = input("Enter grade ")
                            donegrades = donegrades + 1
                            if donegrades == numofgrades:
                                lol = 2
                            elif donegrades != numofgrades:
#Grade 8
                                grade8 = input("Enter grade ")
                                donegrades = donegrades + 1
                                if donegrades == numofgrades:
                                    lol = 2
                                elif donegrades != numofgrades:
#Grade 9
                                    grade9 = input("Enter grade ")
                                    donegrades = donegrades + 1
                                    if donegrades == numofgrades:
                                        lol = 2
                                    elif donegrades != numofgrades:
#Grade 10
                                        grade10 = input("Enter grade ")
                                        donegrades = donegrades + 1
                                        if donegrades == numofgrades:
                                            lol = 2
                                        elif donegrades != numofgrades:
#Grade 11
                                            grade11 = input("Enter grade ")
                                            donegrades = donegrades + 1
                                            if donegrades == numofgrades:
                                                lol = 2
                                            elif donegrades != numofgrades:
#Grade 12
                                                grade12 = input("Enter grade ")
                                                donegrades = donegrades + 1
                                                if donegrades == numofgrades:
                                                    lol = 2
if numofgrades == 1:
    print(grade1)
elif numofgrades == 2:
    print((grade1 + grade2) / 2)
elif numofgrades == 3:
    print((grade1 + grade2 + grade3) / 3)
elif numofgrades == 4:
    print((grade1 + grade2 + grade3 + grade4) / 4)
elif numofgrades == 5:
    print((grade1 + grade2 + grade3 + grade4 + grade5) / 5)
elif numofgrades == 6:
    print((grade1 + grade2 + grade3 + grade4 + grade5 + grade6) / 6)
elif numofgrades == 7:
    print((grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7) / 7)
elif numofgrades == 8:
    print((grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8) / 8)
elif numofgrades == 9:
    print((grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9) / 9)
elif numofgrades == 10:
    print((grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9 + grade10) / 10)
elif numofgrades == 11:
    print((grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9) / 11)
elif numofgrades == 12:
    print((grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9) / 12)