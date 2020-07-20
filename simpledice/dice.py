import random


def roll_dice(min_number, max_number):
    random_number = random.randint(min_number, max_number)
    print('Dice rolled and the number is ' + str(random_number))


keep_rolling = ''

max_faces = int(input('Insert a number of faces of your dice:'))
roll_dice(1, max_faces)

while True:
    keep_rolling = input('Would you like to roll again? ( answer with (Y)es or (N)o ) \n').upper()
    if keep_rolling == 'Y':
        roll_dice(1, max_faces)
    elif keep_rolling == 'N':
        break
    else:
        print("Sorry, We don't have this function in our system!")
        break

