# Developer : Moiseenko V.
# The aim : to choose a suitable semi-acoustic Fender guitar for the buyer

question1 = 'How much money do you want to spend?'
question2 = 'Which color will you choose?'
question3 = 'How many frets do you need?'
question4 = 'Do you need a credit?'
question5 = 'For which number of months?'

print(question1)
price = int(input())
if price < 45_600:
    print('Sorry, but we do not have guitar for your budget')
    exit()
if not price >= 110_000 and price > 45_000:
    print(question2, 'Natural or red?')
    color = str(input(''))
    if color == 'natural':
        print(question3)
        frets = int(input())
        if frets < 21 or frets > 22:
            print('We do not have that guitar')
            exit()
        if frets == 21:
            print('You should to buy FENDER SQUIER CLASSIC VIBE TELE THINLINE MN Natural')
            print('Characteristics :')
            print('price: 45 600 rubles')
            print('material: mahogany')
            print('color: natural')
            print('number of frets: 21')
            print('hand orientation : right-handed')
            print(question4)
            ans = str(input(''))
            if ans == 'yes':
                print(question5)
                cost = 45_600
                per_month = cost / 24
                print('Your monthly payment is', '{:.2f}'.format(per_month), 'rubles.')
                print('Thank you for visit')
            else:
                print('Thank you for your for visiting our shop')
        if not frets == 21:
            print('Your guitar is not found, we are sorry')
    if color == 'red':
        print(question3)
        frets = int(input())
        if frets == 22:
            print('You should to buy FENDER'
                  ' DLX TELE THINLINE MN CAR')
            print(' Characteristics : ')
            print('price :  104 000 rubles')
            print('material: alder')
            print('color: red')
            print('number of frets : 22')
            print('hand orientation : right handed')
            print(question4)
            ans = str(input(''))
            if ans == 'yes':
                print(question5)
                cost1 = 104_000
                per_month = cost1 / 24
                print('Your monthly payment is', '{:.2f}'.format(per_month), 'rubles. Thank you for visiting our shop.')
            else:
                print('Thank you for your visiting'
                      ' our shop')
        else:
            print('Your guitar is not found, '
                  'we are sorry')
    exit()
if not price >= 190_000 and price > 180_000:
    print(question3)
    frets = int(input())
    if frets == 22:
        print('You should to buy FENDER'
              ' TELE THINLINE SUPER DLX RW ORG')
        print('Characteristics : ')
        print('price: 183 000 rubles')
        print('material : rosewood ')
        print('color : orange')
        print('number of frets : 22')
        print('hand orientation : right-handed')
        print(question4)
        ans = str(input(''))
        if ans == 'yes':
            print(question5)
            cost2 = 183_000
            per_month = cost2 / 24
            print('Your monthly payment is', '{:.2f}'.format(per_month), 'rubles. Thank you for visiting our shop.')
        else:
            print('Thank you for your for visiting our shop')
    else:
        print('This guitar does not exist')
    exit()
else:
    print(question3)
    frets = int(input())
    if frets == 22:
        print('You should to buy FENDER'
              'FENDER American Elite Telecaster')
        print('Characteristics :')
        print('price: 195 000 rubles')
        print('material: rosewood ')
        print('color: light blue')
        print('number of frets: 22')
        print('hand orientation: right-handed')
        print(question4)
        ans = str(input(''))
        if ans == 'yes':
            cost3 = 195_000
            per_month = cost3 / 24
            print('Your monthly payment is', '{:.2f}'.format(per_month), 'rubles. Thank you for visiting our shop.')
        else:
            print('Thank you for your for visiting our shop')
    else:
        print('We do not have this guitar')
exit()
