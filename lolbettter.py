from datetime import datetime
import time
y = 324
money = 100
lo = 342432
yes = 1
a = 2
A = 2
print("this is a game in wich you create a company and win money!")
print("the game stops when you have 10000$")
print("you start with 100$")
time.sleep(0.2)
understand = input("do you know the rules?")
if understand == 1:
    while money < 100000 and money > 0:
        print"A: Buy"
        print"B: See how much money you have"
        lol = input("")
        if lol == "a" or "A":
            while lo > 0:
                print"1:Coffee market(10 dollars per sec) cost: 50$"
                print"2:Return to the main menu"
                print"3:Giant mall(200$ per sec)cost : 400$"
                print"4:Small mall(100$ per sec)cost: 200$"
                x = input("")
                if x == "1":
                    money -= 50
                    while y == 324:
                        money += 10
                        time.sleep(1.0)
                elif x == "2":
                    lo = 0
                elif x == "3":
                    money -= 400
                    while y == 324:
                        money += 200
                        time.sleep(1.0) 
                    if money <= 0:
                        lo = 0
                    print"you lost"
                elif x == "4":
                    money -= 200
                    while y == 324:
                        money += 100
                        time.sleep(1.0)

            