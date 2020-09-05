#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The Lumberjack and the Bear
import random 
print('You are the Lumberjack.')
print("Let's chop the tree.")
chop = 0
bear_timing = random.randint(1,10)
while chop < bear_timing:
    attack = str(input("PRINT 'Z' TO CHOP THE TREE."))
    if attack.lower() == 'z':
        chop = chop + 1
        print('You have chopped the tree %d times.' %chop)
    else:
        print("PRINT 'Z' TO CHOP THE TREE.")
        
print('A BEAR appeared from the woods!') 
while True:
    fight_or_flight = input('Will you Run?(1), or will you fight?(2)')
    if fight_or_flight == '1': # RUN
        run = 'RUN '
        count = 1
        while count <= 3:
            print( run*count + ' for your life!!!!')
            count = count + 1
        live_or_die = random.randint(0,1)
        if live_or_die == 1:
            print('Phew... You survived to live another day!')
        elif live_or_die == 0:
            print('Awww... The bear chopped your head off..')
            print('GAME OVER!')
        break
        
    elif fight_or_flight == '2': # FIGHT
        print('You have chose to FIGHT.')
        print('You must kill the bear within 6 turns.')
        bear_health = int(100)
        turn = 1
        print('BEAR(health: %d)' %bear_health)
        
        while turn <= 6:
            attack = str(input("TURN %d: PRINT 'Z' TO ATTACK." %turn))
            if attack.lower() == 'z':
                damage = random.randint(1,30)
                bear_health = bear_health - damage
                turn = turn + 1
                print('You did %d damage to the BEAR!' %damage)
                if bear_health > 0:
                    print('BEAR(health: %d)' %bear_health)
                else:
                    print('BEAR(health: 0)')
                    print('You have killed the BEAR!')
                    break
            else:
                continue
        if turn > 6:
            print('You have failed to kill the BEAR.')
            print('GAME OVER!')   
        else: 
            print('You have acquired BEAR SKIN.')
    else:
        print('You can either RUN, or FIGHT.')
        continue
    break


# In[59]:





# In[ ]:





# In[ ]:




