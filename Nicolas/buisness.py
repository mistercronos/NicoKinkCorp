import time

money = 100
yes = 1
Yes = yes
YES = yes

no = 2
No = no
NO = no

cs = 0
ps = 0
m = 0

print("This is a game in wich you create a company and win money!")
print("The game stops when you have $1000000")
print("You start with 100$")
time.sleep(0.2)
understand = input("Would you like to start the game?")
if understand == 'yes' or 1:
    while money < 10000000:
        print("A: Buy")
        print("B: See how much money you have")
        lol = input("")
        if lol == "a" or "A":
            lo = 1
            while lo > 0:
                print("1: Coffee shop ($10 per minute) cost: $50")
                print("2: Pizza shop ($50 per minute) cost: $1000")
                print("3: Mall (1000$ per minute) cost : $100000")
                print("4: Quit")
                x = input("")
                if x == 1:
                    if money < 50:
                        print("Insuficent funds")
                    elif money > 49:
                        money = money - 50
                        cs = cs + 1
                        print("You have $"+money+ "left")
                        print("You now have " + cs + " coffee shops!")
                        #le probleme c que on devient "prisonier" du while loop donc on ne peut pas sortir au main menu
                        while money < 10000000:
                            time.sleep(60.0)
                            money = money + 10
                elif x == 2:
                    if money  < 1000:
                        print("Not enough money. Money left: $" + money)
                    elif money > 999:
                        money = money - 1000
                        while money < 10000000:
                            time.sleep(60.0)
                            money = money + 50
                elif x == 3:
                    if money  < 1000:
                        print("Not enough money. Money left: $" + money)
                    elif money > 99999:
                        money = money - 100000
                        while money < 10000000:
                            time.sleep(60.0)
                            money = money + 1000
                elif x == 4:
                    lo = 0
