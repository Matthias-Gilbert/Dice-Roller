def reverse():
    again = 'yes'
    while again.casefold() == 'yes':
        try:
            answer = input('Please enter your string: ')
            rev = answer[::-1]
            print(rev)
            again = input('Would you like to go again? ')
        except ValueError:
            print('Please enter a valid input')
    print("Goodbye have a lovely day")
