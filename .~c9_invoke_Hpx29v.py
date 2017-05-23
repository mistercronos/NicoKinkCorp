lol = 1
cshops = 1
pshops = 0
malls = 0
money = 100
totalshops = cshops + pshops + malls
a = "You now have "
b =  'coffee shop(s).'
c = 'Your money is now $'
d = ' pizza shop(s).'
e = ' mall(s).'
if lol == 1:

    print("This game is a game that serves to welcome you to the wonderous world of buisness. You will:")
    print("Sell")
    print("Win a million big boys!")
    start = input("Are you ready? Yes/No yes/no ")
    if start == 'Yes' or 'yes':
        print("Good")
        print("Welcome to the world of buisness!")
        while money <= 1000000 or money < 0:
            print("What do you want to do:")
            print("A: Sell")
            print("B: Buy")
            print("C: Quit")
            wtd = input("Enter coresponding letter of choice ")
            if wtd == 'A' or 'a':
                print("Chosen letter: " + wtd)
                if totalshops > 0:
                    print("What would you like to sell?")
                    print("A: Coffee Shops ($25)")
                    print("B: Pizza Shops ($150)")
                    print("C: Malls ($500)")
                    wts = input("Enter coresponding letter of choice ")
                    if wts == 'A' or 'a':
                        print("Chosen letter: " + wtsB
                        if cshops > 0:
                            cshops = cshops - 1
                            money = money + 25
                            print(a, cshops, b, c, money)
                        if cshops == 0:
                            print("You have zero coffee shops")
                    if wts == 'B' or 'b':
                        print("Chosen letter: " + wts)
                        if pshops > 0:
                            pshops = pshops - 1
                            money = money + 150
                            print(a, pshops, d, c, money)
                        elif pshops == 0:
                            print("You have zero pizza shops")
                    elif wts == 'C' or 'c':
                        print("Chosen letter: " + wts)
                        if malls > 0:
                            malls = malls - 1
                            money = money + 500
                            print(a, malls, e, c, money)
                        elif malls == 0:
                            print("You have zero malls")
            elif wtd == 'B' or 'b':
                print("Chosen letter: " + wtd)
                print("What would you like to buy?(you have "  money plus "$)")
                print("A: Coffee shop ($50) ($100 per 5 minutes")
                print("B: Pizza shop")
            elif wtd == 'C' or 'c':
                money = 1000000
                
javascript_1212 = "FFJEIOKHLFHNDKJBNKJBjVKJHKJHDFGJK KJikjvhfovjklvjfkljvflkvdjfvjkgbcfhgujdfhnvghfgjfhbjuchvikshxvcbhiujchxvdhfchvjhkvjhjkhcjkhkzjxvchvxzkjhzkjchkjhkjhjhc"