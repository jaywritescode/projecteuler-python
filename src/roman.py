values = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

def read(numeral):
    # assume the numeral is valid
    if len(numeral) == 0:
        return 0
    if len(numeral) == 1:
        return values.get(numeral)

    fst, snd = numeral[0:2]
    if values.get(snd) > values.get(fst):
        return values.get(snd) - values.get(fst) + read(numeral[2:])
    else:
        return values.get(fst) + read(numeral[1:])

def write(number):
    roman = []

    while number >= 1000:
        roman.append('M')
        number -= 1000
    if number >= 900:
        roman.extend('CM')
        number -= 900
    elif number >= 500:
        roman.append('D')
        number -= 500
    elif number >= 400:
        roman.extend('CD')
        number -= 400

    while number >= 100:
        roman.append('C')
        number -= 100
    if number >= 90:
        roman.extend('XC')
        number -= 90
    elif number >= 50:
        roman.append('L')
        number -= 50
    elif number >= 40:
        roman.extend('XL')
        number -= 40

    while number >= 10:
        roman.append('X')
        number -= 10
    if number == 9:
        roman.extend('IX')
        number -= 9
    elif number >= 5:
        roman.append('V')
        number -= 5
    elif number == 4:
        roman.extend('IV')
        number -= 4

    roman.extend('I' * number)

    return ''.join(roman)


if __name__ == '__main__':
    print(read('MCMLXXXIV'))
    print(write(1984))
