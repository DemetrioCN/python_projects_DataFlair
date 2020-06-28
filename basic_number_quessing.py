import random

print("\n")
print(10*"-", "Number Guessing", 10*"-")
print("\n")

random_num = random.randint(0, 20)
print(random_num)

chaces = 0

while chaces < 5:

    attempts = 3 - chaces + 1   
    number = int(input("Input a number: "))

    if number == random_num:
        print(10*"-", "¡Congratulations!", 10*"-")
        print(f'{number} is equal to  random number\n')
        break

    elif number < random_num:
        print(f'{number} is lower than the random number')
        print(f'You have {attempts} attempts left\n')

    else: # if number > random_num:
        print(f'{number} is bigger than the random number')
        print(f'You have {attempts} attempts left\n')

    chaces += 1


