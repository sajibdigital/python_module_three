marks = int(input('Enter your Marks: '))
weight = int(input('Enter your Weight: '))

# --- Or Operator

# if marks >= 80 or weight <= 20:
#     print('You will get a chocklet.')
# else:
#     print('You get less marks and over weight.')
 
# --- Not Operator

if not marks <= 79 or not weight >= 20:
    print('You will get a chocklet.')
else:
    print('You get less marks and over weight.')
 