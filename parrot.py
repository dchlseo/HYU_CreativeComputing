# Parrot program 1
print('INSTRUCTIONS: The parrot will repeat anything you say. To quit the program, enter \'q.\'')
while True:
    user_input = str(input('What will you tell the parrot? '))
    if user_input != 'q':
        print('USER: ' + user_input)
        print('PARROT: ' + user_input)
    elif user_input == 'q':
        print('You have quitted the program.')
        break

# parrot program 2
print('INSTRUCTIONS: The parrot will repeat anything you say. You get 5 trials.')
count = 0
while count < 5:
    user_input = str(input('What will you tell the parrot? '))
    print('USER: ' + user_input)
    print('PARROT: ' + user_input)
    count = count + 1
