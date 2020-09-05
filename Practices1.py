#!/usr/bin/env python
# coding: utf-8

# In[10]:


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


# In[22]:


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


# In[24]:


# parrot program 2
print('INSTRUCTIONS: The parrot will repeat anything you say. You get 5 trials.')
count = 0
while count < 5:
    user_input = str(input('What will you tell the parrot? '))
    print('USER: ' + user_input)
    print('PARROT: ' + user_input)
    count = count + 1


# In[31]:


# shape drawing
shape = '*'
count = 1
while count <= 5: 
    print(shape*count)
    count = count + 1


# In[43]:


# counting from 1 to 100
count = 1
total = 0
while count<=100:
    total += count
    count = count +1
print(total)    


# In[50]:


# Lottery generator: random int
import random
count = 1
while count <= 6:
    num = random.randint(1,45)
    print('number ' + str(count)+ ': ' + str(num))
    count=count+1
        
print(allnum)    


# In[57]:


# Lottery (no duplicates)
import random
num = random.sample(range(1,45), 6) # no duplicates
count = 1
for i in num:
    print('Number ' + str(count) + ': ' + str(i))
    count = count + 1


# In[64]:


# Piggy Bank program: add 100 won each time to bank
print('This is my Piggy Bank!')
bank = 0
sign = '$'
count = 1
while bank < 700:
    bank += 100
    print(sign*count + ' New coin! There is ' + str(bank) + ' won in the bank.')
    count = count + 1
print('The pig is very full!')


# In[76]:


# Login Program: enter correct password (case insensitive)
password = 'python'
while True:
    user_input = input('Enter your password: ')
    user_input = user_input.lower()
    if user_input == password:
        print('Login successful.')
        break
    else:
        print('Invalid password.')


# In[82]:


# Random Number Generator: user assigned range
import random
print('This is a random number generator.')
print('You can set a range from which you want the number generated.')
print('WARNING: the number must range from 1 to 1000.')
while True:
    low_num = int(input('Enter the low number: '))
    if low_num >= 1:
        high_num = int(input('Enter the high number: '))
        if high_num > low_num:
            ranNum = random.randint(low_num, high_num)
            break
        else: 
            print('Error! Check your range!')
    elif low_num <= 0: 
        print('Enter a number from 1 to 1000.')
print('Your random number is: ' + str(ranNum))        


# In[105]:


# calculator program: sum, average(mean), range, median
print('This program calculates the sum, average, range and median of all the numbers you entered.')
print('To quit, type \'q\'. ')
user_num = []
while True:
    num = input('Please enter a number: ')
    if num == 'q':
        break
    else:
        try:
            user_num.append(int(num))
        except ValueError:
            print('ERROR: YOU MUST ENTER A NUMBER!')
print('Your numbers: ' + str(user_num)) 
minNum = min(user_num)
maxNum = max(user_num)
totalNum = 0
for i in user_num:
    totalNum = totalNum + i
meanNum = totalNum / len(user_num)

# finding median number
med = len(user_num) 
user_num.sort()
if med % 2 == 0: # if even number
    med1 = user_num[med//2]
    med2 = user_num[med//2-1]
    medNum = (med1+med2)/2
else:
    medNum = user_num[med//2]


print("Sum: " + str(totalNum))
print("Range: " + str(minNum) + '~' + str(maxNum))
print("Mean: " + str(meanNum))
print("Median: " + str(medNum))


# In[1]:


# 99 dan program
print('구구단, 구구단, 구구단, 구구단')
print('Enter a number from 1 to 9.')
dan = int(input('NUMBER: '))
count = 1
while count <= 9:
    print(str(dan)+' * ' + str(count) + ' = ' + str(dan*count))
    count = count + 1


# In[103]:





# In[ ]:




