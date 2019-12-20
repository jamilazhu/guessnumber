import random

r = random.randint(1,100)
while True:
    num = input('Please enter number: ')
    num = int(num)
    if num == r:
        print('You are correct!!')
        break
    elif num > r:
        print('Bigger than the answer!')
    elif num < r:
        print('Smaller than the answer!')

        
