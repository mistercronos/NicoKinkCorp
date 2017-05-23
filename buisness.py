lol = 1
cshops = 1
pshops = 0
malls = 0
money = 100
totalshops = cshops + pshops + malls
a = "You now have "
b =  'coffee shop(s).'
c = 'Your money is $'
d = ' pizza shop(s).'
e = ' mall(s).'
a1 = 'a'
b1 = 'b'
c1 = 'c'
d1 = 'd'
yes = 'yes'
if lol == 1:

    print("This game is a game that serves to welcome you to the wonderous world of buisness. You will:")
    print("Sell")
    print("Win a million big boys!")
    start = input("Are you ready? yes/no ")
    if start == yes:
        print("Good")
        print("Welcome to the world of buisness!")
        while money <= 1000000:
            print("What do you want to do:")
            print("A: Sell")
            print("B: Buy")
            print("C: Quit")
            wtd = input("Enter coresponding letter of choice (No capitals) ")
            if wtd == a1:
                print("Chosen letter: " + wtd)
                if totalshops > 0:
                    print("What would you like to sell?")
                    print("A: Coffee Shops ($25)")
                    print("B: Pizza Shops ($150)")
                    print("C: Malls ($500)")
                    wts = input("Enter coresponding letter of choice (No capitals) ")
                    if wts == a1:
                        print("Chosen letter: A")
                        if cshops > 0:
                            cshops = cshops - 1
                            money = money + 25
                            print(a, cshops, b, c, money)
                        elif cshops == 0:
                            print("You have zero coffee shops")
                    elif wts == b1:
                        print("Chosen letter: B" )
                        if pshops > 0:
                            pshops = pshops - 1
                            money = money + 150
                            print(a, pshops, d, c, money)
                        elif pshops == 0:
                            print("You have zero pizza shops")
                    elif wts == c1:
                        print("Chosen letter: C")
                        if malls > 0:
                            malls = malls - 1
                            money = money + 500
                            print(a, malls, e, c, money)
                        elif malls == 0:
                            print("You have zero malls")
                    else:
                        print("ERROR")
            elif wtd == b1:
                print("Chosen letter: B")
                print(c, money)
                print("A: Coffee shop (Cost: $50) (You get: $500 of interest)")
                print("B: Pizza shop")
                wtb = input("Enter coresponding letter of choice (No capitals)")
                if wtb == a1:
                    print("Chosen letter: A")
                    if money > 50:
                        money = money - 50
                        cshops = cshops + 1
                        print(a, cshops, b)
                            

            elif wtd == c1:
                print("Thank you for playing this game")
                print("See you soon!")
                money = 1000000
                
