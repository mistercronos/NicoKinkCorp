import time

money = 100

yes = 1
Yes = yes
YES = yes

no = 2
No = no
NO = no

print("This is a game in wich you create a company and win money!")
print("The game stops when you have $1000000")
print("You start with 100$")
time.sleep(0.2)
understand = input("Would you like to start the game?")
if understand == 'yes':
    while money < 10000000:
        print("A: Buy")
        print("B: See how much money you have")
        lol = input("")
        if lol == "a" or "A":
            while money < 1000000:
                print("1: Coffee shop ($10 per minute) cost: 50$")
                        print("You have $"+money+ "left")
                print("3: Giant mall (200$ per sec) cost : 400$")
                print("4: Quit")
                x = input("")
                if x == 1:
                    if money < 50:
                        print("Insuficent funds")
                    elif money > 49:
                        money = money - 50
                        print("You have $"+money+ "left")
                        
                        while money < 10000000:
                            time.sleep(60)
                            money = money + 10
                elif x == 2:
                    if money  < 1000:
                        print("Not enough money. Money left: $" + money)
                    elif money > 999:
                        money = money - 1000
                        while money < 10000000:
                            time.sleep(60)
                            money = money + 50
                elif x == 4:
                    
                