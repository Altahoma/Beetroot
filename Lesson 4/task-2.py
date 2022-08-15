phone_num = input('Enter a phone number: ')

if len(phone_num) == 10 and phone_num.isdigit():
    print('Correct number')
else:
    print('Incorrect number')