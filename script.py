name = input('What is your name?')
print('Hello,' + name + ' we are about to find out your zodiac sing!')
print('--------------------')
birthday = int(input('What is your birthday?'))
print('--------------------')
month = int(input('What is your birthmonth? (Please, enter intergers only)'))
print('--------------------')

if month == 1:
    sign = 'Capricorn' if (birthday < 20) else 'Aquarius'
elif month == 2:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 3:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 4:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 5:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 6:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 7:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 8:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 9:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 10:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
elif month == 11:
    sign = 'Aquarius' if (birthday < 19) else 'Pisces'
    print('Your Zodiac sign is: ' + sign)
