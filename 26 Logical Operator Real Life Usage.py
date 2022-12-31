user_name = 'aouwal'
password = '123456'

input_user = input('Enter username: ')
input_pass = input('Enter password: ')

# and operator

# if input_user == user_name and input_pass == password:
#     print('You have succefully Login.')
# else:
#     print('Something went worng.')

# or Operator

if input_user != user_name or input_pass != password:
    print('Something went worng.')
else:
    print('You have succefully Login.')