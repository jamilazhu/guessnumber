import random

r = random.randint(1,100)
count = 0
while True:
    count += 1 # count = count + 1 
    num = input('Please enter number: ')
    num = int(num)
    if num == r:
        print('You are correct!!')
        print('This is your ', count , ' guess')
        break
    elif num > r:
        print('Bigger than the answer!')
    elif num < r:
        print('Smaller than the answer!')
    print('This is your ', count , ' guess')
    
        
