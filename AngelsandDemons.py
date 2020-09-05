# game introduction
def intro():
    print('''

There are two cards faced down.
One is the ANGEL, and the other is the DEMON.
If you pick the ANGEL, you will be rewarded with fortune.
If you pick the DEVIL, you lose your most precious belonging.
You can repeat this game as much as you want.

''')

    start = input('Press enter to continue...')

def drawAngel():
    print('''

     ==
  <^\()/^>
   \/  \/
    /  \
    `''`

    ''')

def drawDemon():
    print('''

       , ,, ,
| || |    ,/  _____  \.
\_||_/    ||_/     \_||
 ||       \_| . . |_/
 ||         |  L  |
,||         |`==='|
|>|      ___`>  -<'___
|>|\    /             \
\>| \  /  ,    .    .  |
 ||  \/  /| .  |  . |  |
 ||\  ` / | ___|___ |  |     (
(( || `--'  | _______ |  |     ))  (
(  )\|| (  )\ | - --- - | -| (  ( \  ))
(\/  || ))/ ( | -- - -- |  | )) )  \((
( ()||((( ())|         |  |( (( () )

    ''')

def main():
    import random
    import time

    while True:
        choice = input('Which card will you choose? (1) or (2): ')
        fate = random.randint(1,2) # assign fate: if choice == fate --> print(ANGEL)

        # checking input
        try:
            choice = int(choice)
            if choice == 1 or choice == 2:
                print('You have chosen CARD %d.' %choice)

                # COUNT DOWN
                countdown = 3
                while countdown > 0:
                    print(countdown)
                    time.sleep(1)
                    countdown = countdown - 1

            else:
                print('Choose from cards 1 or 2.')
                continue
        except ValueError:
            continue
        # compare
        if choice == fate:
            drawAngel()
            print('You picked the ANGEL! You are now a millionaire!')
            break
        elif choice != fate:
            drawDemon()
            print('You picked the DEMON. You have lost the game.')
            break

def goStop():
    # go or stop?
    while True:
        goStop = input('Would you like another go? \'y\' to go, \'n\' to stop')
        try:
            if goStop.lower() == 'y':
                main()
            elif goStop.lower() == 'n':
                print('Good bye.')
                break
        except ValueError:
            continue
#### MAIN PROGRAM ####

intro()
main()
goStop()
