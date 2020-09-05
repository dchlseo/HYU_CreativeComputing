### vending machine ###
import random

print('There is a vending machine.')
print("""

    { :::}----------}
    |  | -----------|
    |  |  [!][/][*] |
    |  | ___________|
    |  | enter coin:|
    |  | -----------|
    |  |            |
    |  | -----------|
    |  | |         ||
    |  |  --------- |
    {================}

""")

myCoin = random.randint(10,50) # money in pocket
myTotal = myCoin * 100
print('You currently have %d won in your pocket.(in 100 won coins)' %myTotal)

while True: # entering coin
    try:
        coinIn = int(input('How many 100 won coins will you put in? \n'))
        if coinIn <= myCoin:
            balance = coinIn * 100
        elif coinIn > myCoin:
            print('You don\'t have enough coins! \n' )
            continue
        break
    except:
        print('You can\'t put that into the vending machine!\n' )

print('''
        You have %d WON in the machine.
''' %balance )

# setting drinks inside vending machine
drinks = ['Milk Tea', 'Energy Drink', 'Pepsi']
price = [700, 800, 500]

# menu board
menu = print('''
        (1) %s (2) %s (3) %s
            %d won      %d won          %d won
''' %(drinks[0], drinks[1], drinks[2], price[0], price[1], price[2]))

# choosing drink
while balance > 0:
    myDrink = input('Choose a drink. Press \'q\' to return change.')

    if myDrink == 'q': # returning change & terminate.
        print('The machine return %d won as change. GOOD BYE!' %balance)
        break

    else: # main code
        try:
            myDrink = int(myDrink)
            if 0 < myDrink < 4:
                if balance >= price[myDrink-1]: # payment and return
                    print('CLANK! Here is your %s.' %(drinks[myDrink-1]))
                    balance = balance - price[myDrink-1]
                    print('Remaining coins: %d' %balance)
                    continue

                else: # not enough money
                    print('You do not have enough coins!')
                continue

            else: # wrong input
                print('Enter the number of the drink, or press \'q\' to return change.')
                continue
        except:
            print('Enter the number of the drink.')
            continue
print('GOOD BYE!')
