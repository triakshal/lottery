
import time
from random import randint

while True:
    ask = input('Would you like to roll? (yes/no) ')
    if ask == 'yes':
        num1 = randint(1, 6)
        num2 = randint(1, 6)
        num3 = randint(1, 6)

        print('Rolling...')
        time.sleep(1)
        print(num1,'...')
        time.sleep(1)
        print(num2,'...')
        time.sleep(1)
        print(num3,'...')
        time.sleep(1)


        if num1 == num2 and num2 == num3:
            print('You won the lottery!')
            time.sleep(1)
        elif num1 == num2 or num2 == num3 or num1 == num3:
            decide = randint(1, 2)
            if decide == 1:
                print('Close!')
            else:
                print('Almost!')
        else:
            decide = randint(1, 2)
            if decide == 1:
                print('Try again!')
            else:
                print("You'll win the next one!")
    else:
        num1 = randint(1, 3)
        num2 = randint(1, 4)
        num3 = randint(1, 5)
        if num1 == num2 and num2 == num3:
            print("You would've won that one!")
        time.sleep(1)
        print('Come again next time!')
    time.sleep(1)