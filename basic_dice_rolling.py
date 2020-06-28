import random

print("\n")
print(10*"*","Dice Rolling Simulator",10*"*")
print("\n")

answer = 'no'
while answer != 'yes':

    print(15*" ","P L A Y", 15*" ")
    print("\n")

    random_number = random.randint(1,6)
    print('Random numer: ', random_number)
    
    answer = input('Do you want to leave? Write: yes \n if answer is not press ENTER => ')
    print('\n')
