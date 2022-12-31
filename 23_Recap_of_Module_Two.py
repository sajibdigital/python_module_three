#---23 Recap of Module Two----

# print('I\'m Going \n\tto Malyesia Tour.')

number = 5
guess = float(input('Enter your Number: '))

# if guess == number:
#     print('Yeah, you have guessed correct number.')
# elif guess > number:
#     print('You have entered larger number.')
# else:
#     print('You have entered smaller number.')

# method two

if guess != number:
    if guess > number:
        print('You  have entered larger number.')
    else:
        print('You have entered smaller number.')
else:
    print('You have won the game.')


