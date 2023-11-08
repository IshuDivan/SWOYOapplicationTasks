
def roman_numerals_to_int(roman_numeral):
    strings=[]
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    for numbers in range(4000):
        num=numbers
        roman = ''
        while num > 0:
            for i, r in all_roman:
                while num >= i:
                    roman += r
                    num -= i
        strings.append(roman)
    for i in range(len(strings)):
        if strings[i]==roman_numeral:
            return i
    return None