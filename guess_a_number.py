in the list or not.

num = [1,15,65,2,6,9,10]

print('Type q to quit.')

while True:

    input_num = int(input('Enter a Number: '))

    if input_num in num:

        print('You have successfully guessed a number.')

        continue

    elif input_num not in num:

        print('Try Again.')

        continue
