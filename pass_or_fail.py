# Pass or fail
print('Enter your exam score.')
entered_num = input('Your score: ')
try:
    score = int(entered_num)
    if score >= 90:
        print('Congratulations, you have passed the exam!')
    elif score < 90:
        print('Sorry, you have failed the exam.')
except ValueError:
    print('Please enter a valid number.')
