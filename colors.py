class bcolors:
    #Purple
    A = '\033[95m'
    #Blue
    B = '\033[94m'
    #Yellow
    C = '\033[93m'
    #Green
    D = '\033[92m'
    #Red
    E = '\033[91m'
    #Grey
    F = '\033[90m'
    #Bold
    G = '\033[1m'
    #Underline
    H = '\033[4m'
    #Highlight
    I = '\033[3m'
    #
    
    #Blank
    ENDC = '\033[0m'
print(bcolors.A + "Hello!" + bcolors.B + " Hello!" + bcolors.C + " Hello!" + bcolors.D + " Hello!" + bcolors.E + " Hello!" + bcolors.F + " Hello!" + bcolors.ENDC + " Hello!"  + bcolors.G + " Hello!" + bcolors.H + " Hello! " + bcolors.I +  " Hello!" + bcolors.ENDC)